from tkinter import *
def quit ():
    import sys ; sys . exit ()
5
root = Tk ( )
lbl = Label ( root , text = "Press the button below to exit" )
lbl . pack ()
btn = Button ( root , text = "Quit" , command = quit )
btn . pack () 
10
root . mainloop ( )