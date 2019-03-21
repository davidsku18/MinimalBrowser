import re

def getImageTags(html, arr=[]):
    regexString = "<img\s[^>]*?src\s*=\s*['\"]([^'\"]*?)['\"][^>]*?>"
    if re.search(regexString, html):
        for m in re.finditer(regexString, html):
            arr.append(m.group()[5:-1])
    print(arr)
    return arr


#'src="[^ ]*\.(jpeg|jpg|png|gif|webp|svg)"'
#<img\s[^>]*?src\s*=\s*['\"]([^'\"]*?)['\"][^>]*?>

""" download all images into some kind of directory
set image from directory
tell to print everything up until that point
call image from directory and print it
continue text display

import tkinter

def add_image():
    text.image_create(tk.END,image=img) #example 1
    text.insert(tk.END, "Hello")

root. tk.TK()

text tk.Text(root)
text.pack(padx = 20, pady = 20)

tk.Button(root, text = "Insert", command = add_image).pack()

img = tk.PhotoImage(file = "forwardIcon.gif")

root.mainloop()
b64img = Image.open(BytesIO(urllib.request.urlopen(imgURL).read()))
"""

img = tk.PhotoImage(file = imgURL)
imgURL = received_html + .png
