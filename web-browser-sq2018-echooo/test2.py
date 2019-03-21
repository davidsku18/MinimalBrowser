from tkinter import *
from PIL import Image, ImageTk
import requests, re

def add_image():
    text.image_create(END, image=img) # Example 1
    text.insert(END, "Hello")

def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

root = Tk()

text = Text(root)
text.pack(padx = 20, pady = 20)

b = Button(root, text = "Insert", command = add_image).pack()


url = 'http://www.google.com/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png'
r = requests.get(url, allow_redirects=True)
w = r.headers['content-type'].replace("image/", "")
filename = get_filename_from_cd(r.headers.get('content-disposition'))
open(str(0) + "." + w, 'wb').write(r.content)


photo = Image.open(str(0) + "." + w)
img = ImageTk.PhotoImage(photo)

root.mainloop()

