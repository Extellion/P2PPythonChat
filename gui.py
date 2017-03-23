from Tkinter import *


def launchGUI(self):
    # title of the GUI
    self.root.title('ONTESTPUTAIN')

    # screen size
    ScreenSizeX = self.root.winfo_screenwidth()
    ScreenSizeY = self.root.winfo_screenheight()

    # frame size
    self.FrameSizeX = 800
    self.FrameSizeY = 600

    # position of the frame inside the screen
    FramePosX = (ScreenSizeX - self.FrameSizeX) / 2
    FramePosY = (ScreenSizeY - self.FrameSizeY) / 2

    # form of the frame (width x height + offset x + offset y) parameters %s* are like the calcul taken in the parantheses(cf: %s(0) = (self.FrameSizeX) x %s(1) = (self.FrameSizeY))
    self.root.geometry("%sx%s+%s+%s" % (self.FrameSizeX, self.FrameSizeY, FramePosX, FramePosY))
    self.root.resizable(width=False, height=False)

    # padding x and Y
    padX = 10
    padY = 10

    # Parent Frame of the section that will be used to as a reference
    parentFrame = Frame(self.root)
    parentFrame.grid(padx=padX, pady=padY,
                     stick=E + W + N + S)  # EWNS as for East West North Sud used to extends elements from both sides to fill the row

    parentFrameIP = Frame(parentFrame)

    # A dedicated frame for the chat group
    readChatGroup = Frame(parentFrame)
    self.receivedChats = Text(readChatGroup, bg="white", width=60, height=30, state=DISABLED)
    self.friends = Listbox(readChatGroup, bg="white", width=30, height=30)
    self.receivedChats.grid(row=0, column=0, sticky=W + N + S, padx=(0, 10))
    self.friends.grid(row=0, column=1, sticky=E + N + S)

    # Dedicated frame for the input text
    writeChatGroup = Frame(parentFrame)
    self.chatVar = StringVar()
    self.chatField = Entry(writeChatGroup, width=80, textvariable=self.chatVar)
    clientSetButton = Button(parentFrameIP, text="Add", width=10, command=self.handleAddClient)
    self.chatField.grid(row=0, column=0, sticky=W)

    # variable declaration/attribution
    self.nameVar = StringVar()
    self.serverIPvar = StringVar()
    self.serverPortVar = StringVar()
    self.clientIPvar = StringVar()
    self.clientPortVar = StringVar()
    self.nameVar.set("TITI")
    self.serverIPvar.set("127.0.0.1")
    self.serverPortVar.set('8796')
    self.clientIPvar.set('127.0.0.1')
    self.clientPortVar.set("1945")
    self.statusLabel = Label(parentFrame)
    # creation of the elements that will be displayed
    serverAdress = Label(parentFrameIP, text="Set: ")
    serverPortField = Entry(parentFrameIP, width=5, textvariable=self.serverPortVar)
    nameField = Entry(parentFrameIP, width=10, textvariable=self.nameVar)
    serverPortField = Entry(parentFrameIP, width=5, textvariable=self.serverPortVar)
    serverSetButton = Button(parentFrameIP, text="Set", width=10, command=self.handleSetServer)
    serverIPfield = Entry(parentFrameIP, width=15, textvariable=self.serverIPvar)
    addClientLabel = Label(parentFrameIP, text="Add friend: ")
    clientIPfield = Entry(parentFrameIP, width=15, textvariable=self.clientIPvar)
    clientPortField = Entry(parentFrameIP, width=5, textvariable=self.clientPortVar)
    chatButton = Button(writeChatGroup, text="Send", width=10, command=self.handleSendChat)

    # grid is used to attach elements for them to be displayed physically on the frame
    serverAdress.grid(row=0, column=0)
    nameField.grid(row=0, column=1)
    serverIPfield.grid(row=0, column=2)
    serverPortField.grid(row=0, column=3)
    serverSetButton.grid(row=0, column=4, padx=5)
    addClientLabel.grid(row=0, column=5)
    clientIPfield.grid(row=0, column=6)
    clientPortField.grid(row=0, column=7)
    clientSetButton.grid(row=0, column=8, padx=5)
    chatButton.grid(row=0, column=1, padx=5)

    parentFrameIP.grid(row=0, column=0)
    readChatGroup.grid(row=1, column=0)
    self.statusLabel.grid(row=3, column=0)
    writeChatGroup.grid(row=2, column=0, pady=10)