from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x200")


def msg():
    messagebox.showwarning("ALERT", "STOP! VIRUS DETECTED")

#ADDING BUTTON WIDGET TO WINDOW
button = Button(window, text="A VIRUS HAS ENTRED YOUR COMPUTER", command=msg)

button.place(x=89, y=80)

#ENTRING THE MAIN LOOP
window.mainloop()