from tkinter import *
from datetime import date
#creating a window
window = Tk()
window.title("My First Window")
window.geometry("800x800")
#add widgets 
#add labels
lbl = Label(window, text="Hello ",fg = "light pink", bg = "dark blue",height= 3,width = 300)
name_lbl = Label(text = "full name",bg = "light blue")
name_entry = Entry()
def display():
    name = name_entry.get()
    #declaring a global variable
    global message
    message = "WELCOME TO THE APPLICATION!!\nTODAYS DATE IS: "
    greet = "HELLO " + name
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box = Text(height = 3) 
btn = Button(text = "BEGIN", command = display,height = 1,bg = "light green",fg = "black")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()