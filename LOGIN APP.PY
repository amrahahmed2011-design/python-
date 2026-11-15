from tkinter import *
root = Tk()
root.title("LOGIN APP")
root.geometry("400x400")
#create a frame
frame = Frame(master = root , height = 200 , width = 360 , bg = "purple")
#add widgets
#add labels
lbl1 = Label(frame,text = "Username",width = 12 , bg = "medium orchid",fg = "white")
lbl2 = Label(frame,text = "gmail id",width = 12 , bg = "medium orchid",fg = "white")
lbl3 = Label(frame,text = "Password",width = 12 , bg = "medium orchid",fg = "white")
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame,show = "*")
#function to display message
def display():
    name = name_entry.get()
    greet = "HEY! " + name
    message = "Welcome to the login app"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    #text_box to display message
text_box = Text(bg = "white",fg = "black")
#add button when pressed message will display
btn = Button(text = "CREATE ACCOUNT",command = display , bg = "light blue",fg = "black")
#arrange all the widgets
frame.place(x = 20 , y = 0)
lbl1.place(x = 20 , y = 20)
name_entry.place(x = 150 , y = 20)
lbl2.place(x = 20 , y = 80)
email_entry.place(x = 150 , y = 80)
lbl3.place(x = 20 , y = 140)
pass_entry.place(x = 150 , y = 140)
btn.place(x = 130 , y = 210)
text_box.place(y=250)
root.mainloop()
