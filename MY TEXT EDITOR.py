#import necessary libraries
from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename
#setup root window
window = Tk()
window.title("My Text Editor")
window.geometry("800x600")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
    """OPEN A FILE FOR EDITING"""
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    text_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_edit.insert(END, text)
        input_file.close()
        window.title(f"My Text Editor - {filepath}")
    #FUNCTIONS TO SAVE FILE
def save_file():
    #save the current file
    filepath = asksaveasfilename(defaultextension = "txt",
                                 filetypes=[("Text Files", "*.txt"),
                                             ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text.edit.get(1.0, END)
        output_file.write(text)
    window.title(f"My Text Editor - {filepath}")
#add widget in the application
text_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1,column=0,sticky="ew", padx=5)

fr_buttons.grid(row=0,column=0,sticky="ns")
text_edit.grid(row=0,column=1,sticky="nsew")

window.mainloop()
