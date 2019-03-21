from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import os, sys, getURL, requests, urllib.request, time, math, os.path
import tkinterBackground
import base64
import shutil
import webbrowser

currentIndex = 0
history = ["https://google.com"]
nav = False 
links={}
titles = {}
images = []
givenHtml = ""
imgSrcLink = ""

def is_downloadable(h):
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower() or 'html' in content_type.lower():
        return False
    return True

def textDisplay(htmlFile, links):
    text = str(htmlFile)

    #weird "&amp;" and "\'" text for our browser...
    text = text.replace("&amp;", "&")
    text = text.replace("\\\'", "\'")
    text = text.replace("&#8211;", "-")
    text = text.replace("&#8217;", "'")

    ###print(text)

    #will store actual text that is printed out
    gatheredText = ""

    #find the h1-header in the simple html file, where
    #the contents of "Hello!" will be printed out
    reachEndOfText = False
    i = 0

    dirs = "Pictures"
    
    while reachEndOfText == False:
        
        idxPTagPos = text.find("<p>", i)
        idxH1TagPos = text.find("<h1>", i)
        idxH2TagPos = text.find("<h2>", i)
        idxH3TagPos = text.find("<h3>", i)
        idxH4TagPos = text.find("<h4>", i)
        idxH5TagPos = text.find("<h5>", i)
        idxH6TagPos = text.find("<h6>", i)

        idxATagPos = text.find("<a ", i)

        idxImgTagPos = text.find("<img ", i)

        """
        if there are no particular tags that are found,
        then change the "not-found" value to infinite
        (to help out with the conditional statements)
        """
        
        if idxPTagPos == -1:
            idxPTagPos = math.inf
        if idxH1TagPos == -1:
            idxH1TagPos = math.inf
        if idxH2TagPos == -1:
            idxH2TagPos = math.inf
        if idxH3TagPos == -1:
            idxH3TagPos = math.inf
        if idxH4TagPos == -1:
            idxH4TagPos = math.inf
        if idxH5TagPos == -1:
            idxH5TagPos = math.inf
        if idxH6TagPos == -1:
            idxH6TagPos = math.inf

        if idxATagPos == -1:
            idxATagPos = math.inf

        if idxImgTagPos == -1:
            idxImgTagPos = math.inf

        #print content within P-tag (if it comes before other tags)
        if (           
                idxPTagPos < idxH1TagPos and idxPTagPos < idxH2TagPos and
                idxPTagPos < idxH3TagPos and idxPTagPos < idxH4TagPos and
                idxPTagPos < idxH5TagPos and idxPTagPos < idxH6TagPos and
                idxPTagPos < idxATagPos and
                idxPTagPos != math.inf
            ):
                idxPTagEnd = text.find("</p>", idxPTagPos)

                #special case if a strong-tag, script-tag is in a p-tag
                findPossibleStrongTag = text.find("<strong>", idxPTagPos)
                findPossibleScriptTag = text.find("<script", idxPTagPos)                
                if findPossibleStrongTag == -1:
                    findPossibleStrongTag = math.inf
                if findPossibleScriptTag == -1:
                    findPossibleScriptTag = math.inf

                #special case if an a-tag is in a p-tag
                if idxATagPos < idxPTagEnd:
                    idxATagBeginText = text.find("\">", idxATagPos)
                    idxATagEndText = text.find("</a>", idxATagBeginText)

                    gatheredText = gatheredText + text[idxATagBeginText + 2 : idxATagEndText] + "\n"  
                    i = idxPTagEnd

                #strong-tag
                elif findPossibleStrongTag < idxPTagEnd:
                    idxStrongTagEndText = text.find("</strong>", findPossibleStrongTag)

                    gatheredText = gatheredText + text[findPossibleStrongTag + 7 : idxStrongTagEndText] + "\n"  
                    i = idxPTagEnd

                #script-tag
                elif findPossibleScriptTag < idxPTagEnd:
                    #don't print out scripts to screen...
                    i = idxPTagEnd
        
                else:
                    gatheredText = gatheredText + text[idxPTagPos + 3 : idxPTagEnd] + "\n"  
                    i = idxPTagEnd

        #print content within H1-tag
        elif (
                idxH1TagPos < idxPTagPos and idxH1TagPos < idxH2TagPos and
                idxH1TagPos < idxH3TagPos and idxH1TagPos < idxH4TagPos and
                idxH1TagPos < idxH5TagPos and idxH1TagPos < idxH6TagPos and
                idxH1TagPos < idxATagPos and
                idxH1TagPos != math.inf
            ):
                idxH1TagEnd = text.find("</h1>", idxH1TagPos)

                #special case if an a-tag is in a h1-tag
                if idxATagPos < idxH1TagEnd:
                    idxATagBeginText = text.find("\">", idxATagPos)
                    idxATagEndText = text.find("</a>", idxATagBeginText)

                    gatheredText = gatheredText + text[idxATagBeginText + 2 : idxATagEndText] + "\n"  
                    i = idxATagEndText
                else:
                    gatheredText = gatheredText + text[idxH1TagPos + 4 : idxH1TagEnd] + "\n"  
                    i = idxH1TagEnd

        #print content within H2-tag
        elif (
                idxH2TagPos < idxPTagPos and idxH2TagPos < idxH1TagPos and
                idxH2TagPos < idxH3TagPos and idxH2TagPos < idxH4TagPos and
                idxH2TagPos < idxH5TagPos and idxH2TagPos < idxH6TagPos and
                idxH2TagPos < idxATagPos and 
                idxH2TagPos != math.inf
            ):
                idxH2TagEnd = text.find("</h2>", idxH2TagPos)

                #special case if an a-tag is in a h2-tag
                if idxATagPos < idxH2TagEnd:
                    idxATagBeginText = text.find("\">", idxATagPos)
                    idxATagEndText = text.find("</a>", idxATagBeginText)

                    gatheredText = gatheredText + text[idxATagBeginText + 2 : idxATagEndText] + "\n"  
                    i = idxATagEndText
                else:
                    gatheredText = gatheredText + text[idxH2TagPos + 4 : idxH2TagEnd] + "\n"    
                    i = idxH2TagEnd

        #print content within H3-tag
        elif (
                idxH3TagPos < idxPTagPos and idxH3TagPos < idxH1TagPos and
                idxH3TagPos < idxH2TagPos and idxH3TagPos < idxH4TagPos and
                idxH3TagPos < idxH5TagPos and idxH3TagPos < idxH6TagPos and
                idxH3TagPos < idxATagPos and
                idxH3TagPos != math.inf
            ):
                idxH3TagEnd = text.find("</h3>", idxH3TagPos)
                
                #special case if an a-tag is in a h3-tag
                if idxATagPos < idxH3TagEnd:
                    idxATagBeginText = text.find("\">", idxATagPos)
                    idxATagEndText = text.find("</a>", idxATagBeginText)

                    gatheredText = gatheredText + text[idxATagBeginText + 2 : idxATagEndText] + "\n"  
                    i = idxATagEndText
                else:
                    gatheredText = gatheredText + text[idxH3TagPos + 4 : idxH3TagEnd] + "\n"     
                    i = idxH3TagEnd

        #print content within H4-tag
        elif (
                idxH4TagPos < idxPTagPos and idxH4TagPos < idxH1TagPos and
                idxH4TagPos < idxH2TagPos and idxH4TagPos < idxH3TagPos and
                idxH4TagPos < idxH5TagPos and idxH4TagPos < idxH6TagPos and
                idxH4TagPos < idxATagPos and
                idxH4TagPos != math.inf
            ):
                idxH4TagEnd = text.find("</h4>", idxH4TagPos)

                #special case if an a-tag is in a h4-tag
                if idxATagPos < idxH4TagEnd:
                    idxATagBeginText = text.find("\">", idxATagPos)
                    idxATagEndText = text.find("</a>", idxATagBeginText)

                    gatheredText = gatheredText + text[idxATagBeginText + 2 : idxATagEndText] + "\n"  
                    i = idxATagEndText
                else:
                    gatheredText = gatheredText + text[idxH4TagPos + 4 : idxH4TagEnd] + "\n"       
                    i = idxH4TagEnd

        #print content within H5-tag
        elif (
                idxH5TagPos < idxPTagPos and idxH5TagPos < idxH1TagPos and
                idxH5TagPos < idxH2TagPos and idxH5TagPos < idxH3TagPos and
                idxH5TagPos < idxH4TagPos and idxH5TagPos < idxH6TagPos and
                idxH5TagPos < idxATagPos and
                idxH5TagPos != math.inf
            ):
                idxH5TagEnd = text.find("</h5>", idxH5TagPos)

                #special case if an a-tag is in a h5-tag
                if idxATagPos < idxH5TagEnd:
                    idxATagBeginText = text.find("\">", idxATagPos)
                    idxATagEndText = text.find("</a>", idxATagBeginText)

                    gatheredText = gatheredText + text[idxATagBeginText + 2 : idxATagEndText] + "\n"  
                    i = idxATagEndText
                else:
                    gatheredText = gatheredText + text[idxH5TagPos + 4 : idxH5TagEnd] + "\n"       
                    i = idxH5TagEnd
        
        #print content within H6-tag
        elif (
                idxH6TagPos < idxPTagPos and idxH6TagPos < idxH1TagPos and
                idxH6TagPos < idxH2TagPos and idxH6TagPos < idxH3TagPos and
                idxH6TagPos < idxH4TagPos and idxH6TagPos < idxH5TagPos and
                idxH6TagPos < idxATagPos and
                idxH6TagPos != math.inf
            ):
                idxH6TagEnd = text.find("</h6>", idxH6TagPos)

                gatheredText = gatheredText + text[idxH6TagPos + 4 : idxH6TagEnd] + "\n"         
                i = idxH6TagEnd

                #special case if an a-tag is in a h6-tag
                if idxATagPos < idxH6TagEnd:
                    idxATagBeginText = text.find("\">", idxATagPos)
                    idxATagEndText = text.find("</a>", idxATagBeginText)

                    gatheredText = gatheredText + text[idxATagBeginText + 2 : idxATagEndText] + "\n"  
                    i = idxATagEndText
                else:
                    gatheredText = gatheredText + text[idxH6TagPos + 4 : idxH6TagEnd] + "\n"         
                    i = idxH6TagEnd


        #print content within A-tag (if it comes before other tags)
        if (           
                idxATagPos < idxH1TagPos and idxATagPos < idxH2TagPos and
                idxATagPos < idxH3TagPos and idxATagPos < idxH4TagPos and
                idxATagPos < idxH5TagPos and idxATagPos < idxH6TagPos and
                idxATagPos < idxPTagPos and
                idxATagPos != math.inf
            ):
                idxATagBeginText = text.find("\">", idxATagPos)
                idxATagEndText = text.find("</a>", idxATagBeginText)

                findPossibleSpanTag = text.find("<span", idxATagBeginText)
                
                if findPossibleSpanTag == -1:
                    findPossibleSpanTag = math.inf

                if idxATagEndText < findPossibleSpanTag:
                
                    hyperlinkBeginPos = text.find("href=", idxATagPos)
                    hyperlinkEndPos = text.find("\"", hyperlinkBeginPos + 6)

                    hyperlink = text[hyperlinkBeginPos + 6 : hyperlinkEndPos]
                  
                    title = text[idxATagBeginText + 2 : text.find("<", idxATagBeginText + 2)]
                    
                    link = Label(displayText, text=title, fg="blue", cursor="hand2")
                    link.pack()
                    link.bind("<Button-1>", clickevent)
                    links[link]= hyperlink
 
 #                  gatheredText = gatheredText + text[idxATagBeginText + 2 : idxATagEndText] + "\n"  
                    gatheredText = gatheredText + "\n"
                    
                i = idxATagEndText
                
        #if we reach the end of the html-file, then we have completely
        #found all the text that we need to display!
        elif (
                idxPTagPos == math.inf and idxH1TagPos == math.inf and
                idxH2TagPos == math.inf and idxH3TagPos == math.inf and
                idxH4TagPos == math.inf and idxH5TagPos == math.inf and
                idxH6TagPos == math.inf and idxATagPos == math.inf
            ):
                reachEndOfText = True

    return gatheredText
def clickevent(event):
        global barEntry
        global searchBar
        global links
        clickable = links[event.widget]
        for key in links.keys():
                key.destroy()
                #del links[key]
        links={}
        barEntry.set(clickable)
        #searchBar = Entry(window, textvariable = barEntry, width="60")
        openLink(clickable)

#print out the text of a simple html file that displays the text "Hello!"
#the test will work with the given htm-file called "hello_textDisplay.htm"

#keeps track of how many links we have
linkNum = 0

def getImageTags(html, givenHtml):
        global imgSrcLink
        global givenHTML
        global images
        
        text = str(html)

        #weird "&amp;" and "\'" text for our browser...
        text = text.replace("&amp;", "&")
        text = text.replace("\\\'", "\'")
        text = text.replace("&#8211;", "-")
        text = text.replace("&#8217;", "'")

        i = 0

        reachEndOfText = False
        while reachEndOfText == False:
            idxImgTagPos = text.find("<img ", i)

            if idxImgTagPos == -1:
                idxImgTagPos = math.inf

            if (idxImgTagPos != math.inf):
                idxSrcStart = text.find("src=\"", idxImgTagPos)
                idxSrcEnd = text.find("\"", idxSrcStart + 6)

                idxFoundHttp = text.find("http", idxSrcStart)

                if idxFoundHttp < idxSrcEnd:
                        images.append(text[idxSrcStart + 5 : idxSrcEnd])
                        #print(text[idxSrcStart + 5 : idxSrcEnd])

                else:
                        if text[idxSrcStart + 5 : idxSrcEnd][0:1] == '/' and text[idxSrcStart + 5 : idxSrcEnd][0:2] != "//":
                                images.append(givenHtml + text[idxSrcStart + 5 : idxSrcEnd])
                                imgSrcLink = givenHtml + text[idxSrcStart + 5 : idxSrcEnd]
                        if text[idxSrcStart + 5 : idxSrcEnd][0:1] != '/' and text[idxSrcStart + 5 : idxSrcEnd][0:2] != "//":
                                images.append(givenHtml + "/" + text[idxSrcStart + 5 : idxSrcEnd])
                                imgSrcLink = givenHtml + "/" + text[idxSrcStart + 5 : idxSrcEnd]
                        if text[idxSrcStart + 5 : idxSrcEnd][0:2] == "//":
                                images.append("http:" + text[idxSrcStart + 5 : idxSrcEnd])
                                imgSrcLink = "http:" + text[idxSrcStart + 5 : idxSrcEnd]
                        print(images)

                i = idxImgTagPos + 5

            elif (idxImgTagPos == math.inf):
                reachEndOfText = True

def add_image(img):
    displayText.image_create(END,image=img)
    
def openLink(webAddress= None):
        t0 = time.time()
        global currentIndex
        global history
        global nav
        global links
        global titles
        global images
        global imgSrcLink
        links={}

        dirs = "Pictures"

        displayText.delete(1.0, END)
        for key in links.keys():
                key.destroy()
        links={}
        
        r_html = ""
        
        if webAddress==None:
                response = getURL.getURL(barEntry.get())
                givenHtml = barEntry.get()
                received_html=response

                r_html = response

                if os.path.exists(dirs):
                        shutil.rmtree(dirs)
                os.mkdir(dirs)

                getImageTags(str(received_html), givenHtml)
                print(imgSrcLink)

                i = 0
                for image in images:
                        r = requests.get(image, allow_redirects=True)
                        if is_downloadable(r):
                            f = open(dirs + "/" + str(i) + "." + r.headers['content-type'].replace("image/", ""), "wb")
                            f.write(r.content)
                            f.close()
                            i += 1

                received_html=textDisplay(received_html, links)

                if nav == False:
                        history.append(barEntry.get())
                        currentIndex = currentIndex+1
                t1 = time.time()-t0
                
                print(str(t1))
                               
        else:
                response = getURL.getURL(webAddress)
                received_html=response
                r_html = response
                received_html=textDisplay(received_html, links)

                print(imgSrcLink)

                if nav == False:
                        history.append(webAddress)
                        currentIndex = currentIndex+1
                t1= time.time()

        if len(images) != 0:
            for image in os.listdir(dirs):
                photo = Image.open(dirs + "/" + image)
                img = ImageTk.PhotoImage(photo)
                add_image(img)

        displayText['background'] = tkinterBackground.getBackground(r_html)
        print(displayText['background'])
        displayText.insert(0.0, received_html)
        
def goForward():
    global currentIndex
    global history
    global nav
    global barEntry
    if (currentIndex+1)<len(history):
        nav = True
        currentIndex = currentIndex+1
        barEntry.set(history[currentIndex])
        openLink(history[currentIndex])
    else:
        print("Cannot go foward")   

def goBack():
        global currentIndex
        global history
        global nav
        global barEntry
        if (currentIndex-1)>=0:
                nav = True
                currentIndex = currentIndex-1
                barEntry.set(history[currentIndex])
                openLink(history[currentIndex])
        else:
                print("Cannot go back")

def refresh():
        global currentIndex
        global history
        global nav
        nav = True
        openLink(history[currentIndex])
        
#Gets font and size arguments
def manipulateFont(*args):
        fontString = (font.get(), fontSize.get())
        return fontString
        writeNewFont = (font.get() + " " + fontSize.get())
        with open("fontSettingsFile.txt", "w") as f:
                f.write(str(writeNewFont))

#Gets the saved font and size from a file
def readFontFile():
        if os.path.isfile('fontSettingsFile.txt'):
                with open('fontSettingsFile.txt') as f:
                        readNewFont = f.readline()
                        searchBar.config(font=readNewFont)
                        openURL.config(font=readNewFont)
                        back.config(font=readNewFont)
                        forward.config(font=readNewFont)
                        refresh.config(font=readNewFont)
                        setFont.config(font=readNewFont)
                        fontOptions.config(font=readNewFont)
                        fontSizeOptions.config(font=readNewFont)
                        displayText.config(font=readNewFont)
                print("Font settings file exists, the font is " + readNewFont)
        else:
                print("Font settings file doesn't exist")

"""Creates the window"""
window = Tk()
window.title("Simple Browser")
window.geometry("2000x1000")

"""Button image assignments"""
forwardIcon = PhotoImage(file="forwardIcon.gif")
backIcon = PhotoImage(file="backIcon.gif")
refreshIcon = PhotoImage(file="refreshIcon.gif")

"""Creates frames for layouts"""
buttonFrame = Frame(window)
buttonFrame.pack()
textFrame = Frame(window)
textFrame.pack(side=BOTTOM)

barEntry = StringVar()
searchBar = Entry(window, textvariable = barEntry, width="60")

"""Creates the buttons and commands for"""
openURL = Button(window, text="Open", command=openLink)
back = Button(buttonFrame, compound=TOP, image=backIcon, text="Back", command=goBack)
forward = Button(buttonFrame, compound=TOP, image=forwardIcon, text="Forward", command=goForward)
refresh = Button(buttonFrame, compound=TOP, image=refreshIcon, text="Refresh")
setFont = Button(window, text="Set Font", command=readFontFile)

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

displayText = Text(textFrame, padx = "250", yscrollcommand=scrollbar.set)
scrollbar.config(command=displayText.yview)

"""Option Menu widget for font"""
font = StringVar(window)
font.set("Times")
font.trace("w", manipulateFont)
fontOptions = OptionMenu(window, font, "Arial", "Times", "Helvetica")

"""Option Menu widget for font size"""
fontSize = StringVar(window)
fontSize.set("12")
fontSize.trace("w", manipulateFont)
fontSizeOptions = OptionMenu(window, fontSize, "12", "13", "14", "15")

searchBar.pack(side=TOP)
#label.pack(side=RIGHT)
openURL.pack(side=TOP)
back.pack(side=LEFT)
forward.pack(side=LEFT)
back.pack(side=LEFT)
refresh.pack(side=LEFT)
fontOptions.pack(side=TOP)
fontSizeOptions.pack(side=TOP)
setFont.pack(side=TOP)
displayText.pack(side=BOTTOM)

if __name__=="_main__":
        window.mainloop()
