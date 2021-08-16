import socket
from threading import Thread

class Client:

    def __init__(self, running):
        """Start the socket configurations

            define how the client will connect to the server
            in this case we use TCP/IPV4 methods
        """
        
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.run = running
        
    def on_connect(self, Ip, Port, username):
        """
        Joins the server

        Parameters:

        :param Ip: takes the Server Ip from which the client will connect
        :param Port: takes the Port where the server is located in
        :param username: takes the username that the client will use on
         the server (Room)

        Joins to the server port/Ip, and creates a connection between
        the client and the host computer with the data that the client passed
        through the program.
        """

        self.CLIENT_IP = Ip
        self.CLIENT_PORT = Port
        self.username = username
        
        try:
            self.client.connect((self.CLIENT_IP,self.CLIENT_PORT))
            print("connected")
            self.client.send(self.username.encode('utf-8'))
            

        except socket.error as err:
            print(err)
            self.on_connect()

    def on_receive_message(self):
        """
            Receives the Server messages

            Starts listening for messages
            and when the client receive one from the server,
            this method will decode, print and yield the message
            (it will return the message without breaking the loop,
            yield instead of returning the first argument and breaking
            the loop, it keeps the data in a generator obj, that then
            we could iterate through to get the messages)
        """
        while self.run:
            try:
                self.message = self.client.recv(2040).decode('utf-8')
                print(self.message)
                yield f"{self.message}"

            except socket.error as err:
                print(f'el error: \n\n {err}')
            


    def on_sending_message(self, message):
        """Sends the message to the server

            Parameters:

            :param message: takes the message that will be
             sended to the server

            when called, this method will send the message on the
            next format:

            UserName:
                message
            

        """
        self.client.send(f"{self.username}:\n   {message}\n\n".encode('utf-8'))



