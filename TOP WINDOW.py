#import nessasary libraries
from tkinter import *

root = Tk()
root.title("main window")
root.geometry("400x300")

def topwin():
    top = Toplevel()
    top.title("top window")
    top.geometry("200x150")

    l2 = Label(top, text="this is top window")
    l2.pack()

    top.mainloop()

l = Label(root, text="this is main window")
btn = Button(root, text="open top window", command=topwin)
#arranging widgets
l.pack()
btn.pack()

root.mainloop()