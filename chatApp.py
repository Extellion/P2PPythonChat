from Tkinter import *
from server import Server
import socket
import thread

from gui import launchGUI


class App(Frame):
  
  def __init__(self, root):
    Frame.__init__(self, root)#init de classe parente Frame
    self.server = Server(root)
    launchGUI(self.server)


def main():
  root = Tk()
  App(root)
  root.mainloop()

if __name__ == '__main__':
  main()  