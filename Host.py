import socket
from threading import Thread
import sys


class Host:
    def __init__(self, Ip, Port,Running):
        """Gets the user data


            Parameters:

            :param Ip: takes the host Ip (127.0.0.1)
            :param Port: takes the host Port (>1023)


            takes the user parameters and creates a list that will
            keep the online users, then it calls the on_Creating_connection
            to start a connection with the user inputs
        """

        self.IP = Ip
        self.PORT = Port
        self.OnlineUsers = {}
        self.run = Running

        Thread(target=self.on_creating_connection, daemon=True).start()


    def on_creating_connection(self):
        """
        Creates the connection

        this method is automatically called, and creates
        a socket (Connection), on the user local IP,
        and then it calls the on_Created class attribute 
        """
        try:
            self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server.bind((self.IP,self.PORT))
            print('listening')
            self.server.listen(5)
            self.on_created()

        except socket.error as Err:
            print(Err)
    
    def on_created(self):
        """
        Adds the users

        this class is automatically called.
        it waits for a connection, and when some one joins
        this method keeps (Append) the client ip/port on the OnlineUsers list
        and creates a thread that will be used for sending messages to
        the server.

        the ip and port are first received in the self.clientIp/clientAddr
        and then they are appended to the dictionary (OnlineUsers)

        then the on_message method is called with the argument of the
        client Ip
        """

        while self.run:
            self.clientIp, self.clientAddr = self.server.accept()
            self.OnlineUsers[self.clientAddr] = self.clientIp

            Thread(target=self.on_message, args=[self.clientIp]).start()
    
    def on_message(self, clientIp):
        """
        Sends and receive the messages

        Parameters:
        
        :param clientIp: Takes the clientIp from the one
         the server will receive and send messages

        takes the client ip and start listening for messages,
        also it will transmit every message received from the client
        and will then send to all the clients the message
        """

        username = self.message = clientIp.recv(2040).decode("utf-8")

        #loops through the clients Ips (key=Ports, values=Ips)
        #and sends a "Welcome" message
        for user in self.OnlineUsers.values():
                user.send(f' [{username}] Joined the Room \n'.encode('utf-8'))

        try:
            while self.run:
                #waits for a message
                
                self.message = clientIp.recv(2040)
                print(self.message)

                #transmit the message to all the users on the Online Dict
                for user in self.OnlineUsers.values():
                    user.send(self.message)

        except socket.error as err:
            print(f'el error \n{err}')
            print(f"{username} ha abandonado la sala")
            try:
                for user in self.OnlineUsers.values():
                        user.send(f"[{username}] Leaved the chat".encode("utf-8"))
                        pass
            except socket.error as err:
                print(f'otro error \n {err}')
            
            