from Tkinter import *
from ttk import *
import socket
import thread

class ChatClient(Frame):
  
  def __init__(self, root):
    Frame.__init__(self, root);
    self.root = root;
    self.launchGUI();

  def launchGUI(self):
    #title of the GUI
    self.root.title('ONTESTPUTAIN');
    
    #screen size
    ScreenSizeX = self.root.winfo_screenwidth()
    ScreenSizeY = self.root.winfo_screenheight()
    
    #frame size
    self.FrameSizeX  = 800
    self.FrameSizeY  = 600
    
    #position of the frame inside the screen
    FramePosX   = (ScreenSizeX - self.FrameSizeX)/2
    FramePosY   = (ScreenSizeY - self.FrameSizeY)/2
    
    #form of the frame (width x height + offset x + offset y) parameters %s* are like the calcul taken in the parantheses(cf: %s(0) = (self.FrameSizeX) x %s(1) = (self.FrameSizeY))
    self.root.geometry("%sx%s+%s+%s" % (self.FrameSizeX,self.FrameSizeY,FramePosX,FramePosY))
    
    # padding x and Y
    padX = 10
    padY = 10
    
    # Parent Frame of the section that will be used to as a referend
    parentFrame = Frame(self.root)
    #EWNS as for East West North Sud used to extends elements from both sides to fill the row
    parentFrame.grid(padx=padX, pady=padY, stick=E+W+N+S)
    parentFrameIP = Frame(parentFrame)
    
    #variable declaration/attribution
    self.nameVar = StringVar()
    self.serverIPvar = StringVar()
    self.serverPortVar = StringVar()
    self.clientIPvar = StringVar()
    self.clientPortVar = StringVar()
    self.nameVar.set("lol")
    self.serverIPvar.set("127.0.0.1")
    self.serverPortVar = set('127.0.0.1')
    self.clientIPvar.set('127.0.0.1')
    self.clientPortVar.set("1945")

    #creation of the elements that will be displayed
    serverAdress = Label(parentFrameIP, text="Set: ")
    serverPortField = Entry(parentFrameIP, width=5, textvarible=self.serverPortVar)
    nameField = Entry(parentFrameIP, width=10, textvariable=self.nameVar)
    serverIPfield = Entry(parentFrameIP, width=15, textvariable=self.serverIPvar)
    clientIPfield = Entry(parentFrameIP, )
    
    #grid is used to attach elements for them to be displayed physically on the frame
    serverAdress.grid(row=0, column=0)
    nameField.grid(row=0, column=1)
    serverIPfield.grid(row=0, column=2)
    parentFrameIP.grid(row=0, column=0)

def main():
  root = Tk()
  app = ChatClient(root)
  root.mainloop()  

if __name__ == '__main__':
  main()  