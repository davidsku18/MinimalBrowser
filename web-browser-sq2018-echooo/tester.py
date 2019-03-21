from tkinter import *
from PIL import Image, ImageTk

def add_image():
    text.image_create(END,img) #example 1
    text.insert(END, "Hello")

root=Tk()

img = PhotoImage(file = "forwardIcon.gif")
text = Text(root)
text.pack(padx = 20, pady = 20)

b = Button(root, text = "Insert", command = add_image)
b.pack()



root.mainloop()
