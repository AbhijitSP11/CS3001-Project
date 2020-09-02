from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.geometry("4930x3346")

root.title("Galaxy")

image1 = ImageTk.PhotoImage(Image.open(r"C:\Users\Abhijit\Desktop\board game.png"))
label = Label(image = image1)
label.pack()

def click():
    label = Label(root, text = "Hello")
    label.pack()

def instruction():
    inst = Label(root, text = """ """)

    inst.pack()
Button1 = Button(root, text = "Play Game", command = click, pady = 10, padx = 25, fg = "white", bg = "orange")
Button2 = Button(root, text = "Instructions", command = instruction, pady = 10, padx = 22, fg = "white", bg = "orange")
# Button3 = Button(root, text = "", command = click, pady = 10, padx = 25)
Button4 = Button(root, text = "Exit", command = click, pady = 10, padx = 44, fg = "white", bg = "orange")
Button1.pack()
Button2.pack()
# Button3.pack()
Button4.pack()

root.mainloop()
