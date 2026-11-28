from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Calculator")
root.geometry("400x300")
root.config(bg="light green")

#adding image ad lables to the window
upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
img = ImageTk.PhotoImage(upload)

l1 = Label(root, image=img,bg="light green")
l1.place(x=180, y=20)

l1 = Label(
    root,
    text="hello user, welcome to denomination calculator",
    bg = "light green",   
)
l1.place(relx=0.5, y=340,anchor=CENTER)
