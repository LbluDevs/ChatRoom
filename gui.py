from Host import *
from Client import *
import socket, random
from tkinter import *
from Events import events
from threading import Thread
import sys


class MainWindow(Tk):
    ScreenWd = 400
    SCreenHg = 600
    deepBlue = '#67C7FF'
    lightBlue = '#E6F6FF'
    creamBlue = '#CDECFF'
    deepCreamBlue ='#D6E6EF'

    def __init__(self):

        super().__init__()
        self.iconbitmap('Images\ChatRoomIcon.ico')
        self.title('ChatRoom')
        self.geometry("400x600")
        self.resizable(False,False)
        self.build()
        self.client_conn  = Client()
        self.mainloop()
        

    @staticmethod
    def randomPort():
        return random.randint(2030,65535)

    def build(self):
        self.image_Loader()
        self.ScreenFrames()
        self.ScreenBackgrounds()
        self.joinWindow()
        self.chat_screen()
        self.event_Handler()

    def image_Loader(self):
        self.CreatebtnBg = PhotoImage(file='images/CreateButton.png')
        self.EntryBg = PhotoImage(file='images/entryBg.png')
        self.JoinBtnBg = PhotoImage(file='images/joinButton.png')
        self.SendBtnbg = PhotoImage(file='images/sendBtnBg.png')
        self.SendEntryBg = PhotoImage(file='images/SendEntryBg.png')
        self.ChatViewerBg = PhotoImage(file='images/TextViewerBg.png')
    

    def ScreenFrames(self):

        self.JoinFrame = Frame(
                self,width=self.ScreenWd,
                height=self.SCreenHg
             )
        self.JoinFrame.place(x=0, y=0)

        self.ChatFrame = Frame(self,width=self.ScreenWd, height=self.SCreenHg)

    def ScreenBackgrounds(self):
        self.JoinBg = Canvas(
                self.JoinFrame,
                width=self.ScreenWd,
                height=self.SCreenHg,
                highlightthickness=0,
                bg=self.deepBlue
                )

        self.JoinBg.place(x=0, y=0)

        self.ChatBg = Canvas(
                    self.ChatFrame,
                    width=self.ScreenWd,
                    height=self.SCreenHg,
                    highlightthickness=0,
                    bg= self.deepBlue
                )
        self.ChatBg.place(x=0, y=0)

    def joinWindow(self):
        
        #titles

        self.Title = self.JoinBg.create_text(
            200,
            70,
            text='ChatRoom',
            font=('Roboto',34, 'bold'),
            justify='center',
            fill=self.lightBlue
        )
        
        self.Subtitle = self.JoinBg.create_text(
            200,
            120,
            text='Chat with Friends\nLocally!',
            font=('Roboto', 14, 'bold'),
            justify='center',
            fill=self.creamBlue
        )

        #entries Texts

        #username Label
        self.UsernameLabel = self.JoinBg.create_text(
                120,
                190,
                text="Username",
                font=('Roboto', 13, 'bold'),
                fill = self.lightBlue
             )

        #Ip Label
        self.IpLabel = self.JoinBg.create_text(
                123,
                290,
                text="Ip Address",
                font=('Roboto', 13, 'bold'),
                fill = self.lightBlue
             )

        #Port Label
        self.PortLabel = self.JoinBg.create_text(
                103,
                390,
                text="Port",
                font=('Roboto', 13, 'bold'),
                fill = self.lightBlue
             )

        #Entries

        #username entry
        self.UsernameEntry = Entry(
                self.JoinFrame,
                width=26,
                relief='flat',
                font=('Roboto',12,'bold'),
                bg=self.lightBlue,
                fg=self.deepBlue
               )
        self.UsernameEntry.place(x=80, y=220)
        self.UsernameEntry.focus()

        #Entry bg
        self.JoinBg.create_image(200, 230, image=self.EntryBg)

        #ip entry
        self.IpEntry = Entry(
                self.JoinFrame,
                width=26,
                relief='flat',
                font=('Roboto',12,'bold'),
                bg=self.lightBlue,
                fg=self.deepBlue
               )
        self.IpEntry.place(x=80, y=320)
        #Entry bg
        self.JoinBg.create_image(200, 330, image=self.EntryBg)

        #port entry
        self.PortEntry = Entry(
                self.JoinFrame,
                width=26,
                relief='flat',
                font=('Roboto',12,'bold'),
                bg=self.lightBlue,
                fg=self.deepBlue
               )
        self.PortEntry.place(x=80, y=420)
        #Entry bg
        self.JoinBg.create_image(200, 430, image=self.EntryBg)

        #Buttons
        
        #Join Button
        self.JoinButton = Button(
                self.JoinFrame,
                text='Join',
                width=162,
                height=48,
                relief='flat',
                bd=0,
                bg=self.deepBlue,
                activebackground=self.deepBlue,
                image = self.JoinBtnBg,
                font=('Roboto',9,'bold'),
                command= lambda: Thread(target=self.on_joining_server).start()
             )


        self.JoinButton.place(x=115, y=500)

        #Create Button
        self.CreateButton = Button(
                self.JoinFrame,
                text='Create',
                width=15,
                height=1,
                relief='flat',
                bd=0,
                bg=self.deepBlue,
                activebackground=self.deepBlue,
                fg=self.creamBlue,
                activeforeground=self.lightBlue,
                font=('Roboto',11,'bold'),
                command = self.on_hosting
             )

        self.CreateButton.place(x=126, y=560)


    def chat_screen(self):

        #Message Viewer
        self.message_viewer = Text(
                self.ChatFrame,
                width= 26,
                height=21,
                padx=30,
                pady=40,
                relief='flat',
                font=('Roboto', 12, 'bold'),
                bg=self.deepCreamBlue,
                fg=self.deepBlue,
              )
        self.message_viewer.place(x=50,y=20)

        #chatView Bg
        self.ChatBg.create_image(
            202,
            260,
            image=self.ChatViewerBg
        )

        #Message entry

        self.message_entry = Text(
            self.ChatFrame,
            width=28,
            height=2,
            relief='flat',
            font=('Roboto', 10, 'bold'),
            bg=self.lightBlue,
            fg=self.deepBlue,
        )

        self.message_entry.place(x=85,y=540)
        self.message_entry.focus()
        #msg entry bg

        self.ChatBg.create_image(
            187,
            556,
            image=self.SendEntryBg
        )



        #Message Button
        self.sendButton = Button(
                self.ChatFrame,
                text=">",
                width=52,
                height=52,
                bd=0,
                bg=self.deepBlue,
                activebackground=self.deepBlue,
                relief='flat',
                image = self.SendBtnbg,
                command= self.sending_message
               )
        self.sendButton.place(x=310, y=532)


    #---------------Button Events-------------------#

    def on_hosting(self):
        #gets the host ip and inserts it on the entry
        hostIp = socket.gethostbyname(socket.gethostname())
        self.IpEntry.insert(0,hostIp)

        #generates a random port and place it on the entry
        self.PortEntry.insert(0,self.randomPort())
        print('Create a server')

        self.JoinButton.config(
                text='Create',
                command=self.on_creating_server,
                image=self.CreatebtnBg
              )
              
        events.on_hover(self.JoinButton,text='Create a Room!', text_bf='Create')

        self.CreateButton.place_forget()
    

    def on_creating_server(self):
        Ip = self.IpEntry.get()
        Port = int(self.PortEntry.get())
        

        Host(Ip,Port)
        print('hosting')
        Thread(target =self.on_joining_server).start()
    
    def on_joining_server(self):
        
        Ip = self.IpEntry.get()
        Port = int(self.PortEntry.get())
        userName = self.UsernameEntry.get()

        if Ip and Port and userName:
            self.JoinFrame.place_forget()
            self.ChatFrame.place(x=0, y=0)

            self.client_conn.on_connect(Ip, Port, userName)

            for msg in self.client_conn.on_receive_message():
                print(msg)
                self.message_viewer.insert(END, f"{msg}\n")
                self.message_viewer.see(END)
            


    def sending_message(self):
        self.userMessage = self.message_entry.get('1.0', END).strip()
        self.client_conn.on_sending_message(self.userMessage)
        self.message_entry.delete('1.0', END,)

    #---------------User Events-------------#

    def event_Handler(self):
        #Button Events

        #Create Button event
        events.on_hover(self.CreateButton,text='Create a Room!', text_bf='Create')
    
        #joinButton event
        events.on_hover(self.JoinButton,text='Join a Room!', text_bf='Join')

        #Entries Events

        #username entry event
        events.on_enter_pressed(self.UsernameEntry, self.IpEntry)

        #Ip Entry event
        events.on_enter_pressed(self.IpEntry, self.PortEntry)

        #send entry event
        events.on_enter_pressed_send(self.message_entry, self.sending_message)

        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    def on_exit(self):
        self.destroy()
        sys.exit(0)
MainWindow()


