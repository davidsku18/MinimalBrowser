#print out the text of a simple html file that displays the text "Hello!"
#the test will work with the given htm-file called "hello_textDisplay.htm"

import math
from tkinter import *


#keeps track of how many links we have
linkNum = 0



def textDisplay(htmlFile, links, titles):

    #####only if we have a separate text-file
    ##f = open(htmlFile, 'r')
    ##text = f.read()

    ###delete weird beginning characters of htm-file
    ##text = text[3:]

    text = str(htmlFile)

    #weird "&amp;" and "\'" text for our browser...
    text = text.replace("&amp;", "&")
    text = text.replace("\\\'", "\'") 

    ###print(text)

    #will store actual text that is printed out
    gatheredText = ""

    #find the h1-header in the simple html file, where
    #the contents of "Hello!" will be printed out
    reachEndOfText = False
    i = 0

##    noMorePTags = False
##    noMoreH1Tags = False
##    noMoreH2Tags = False
##    noMoreH3Tags = False
##    noMoreH4Tags = False
##    noMoreH5Tags = False
##    noMoreH6Tags = False
    
    while reachEndOfText == False:
        
        idxPTagPos = text.find("<p>", i)
        idxH1TagPos = text.find("<h1>", i)
        idxH2TagPos = text.find("<h2>", i)
        idxH3TagPos = text.find("<h3>", i)
        idxH4TagPos = text.find("<h4>", i)
        idxH5TagPos = text.find("<h5>", i)
        idxH6TagPos = text.find("<h6>", i)

        idxATagPos = text.find("<a ", i)

        #if there are no particular tags that are found,
        #then change the "not-found" value to infinite
        #(to help out with the conditional statements)
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


                ########print(text[idxATagBeginText + 2 : idxATagEndText])
                #print("begin: " + str(idxATagBeginText))
                #print("end: " + str(idxATagEndText))

                ###print(text[idxATagBeginText + 3 : idxATagEndText])



                hyperlinkBeginPos = text.find("href=", idxATagPos)
                hyperlinkEndPos = text.find("\"", hyperlinkBeginPos + 6)

                ##print("begin: " + str(hyperlinkBeginPos) + "   end: " + str(hyperlinkEndPos))

                hyperlink = text[hyperlinkBeginPos + 6 : hyperlinkEndPos]
                ##print(hyperlink)

                title = text[idxATagBeginText + 2 : idxATagEndText]
                ####basicUI.callback(<"Button-"+str(linkNum)+">", hyperlink, text[idxATagBeginText + 2 : idxATagEndText])
                
##                link = Label(basicUI.displayText, text=title, fg="blue", cursor="hand2")
##                link.pack()
##                link.bind("<Button-1>", basicUI.clickevent)
                links[link]= hyperlink
                titles[link] = title

                
                #linkNum = linkNum + 1
                #text[idxATagBeginText + 2 : idxATagEndText]
                
                
                gatheredText = gatheredText + text[idxATagBeginText + 2 : idxATagEndText] + "\n"  
                i = idxATagEndText


                



                

                findPossibleSpanTag = text.find("<span", idxATagBeginText)
                
                if findPossibleSpanTag == -1:
                    findPossibleSpanTag = math.inf

                if idxATagEndText < findPossibleSpanTag:
                    gatheredText = gatheredText + text[idxATagBeginText + 2 : idxATagEndText] + "\n"  

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

#############################################################################
###### Below is the code for getting rid of a-tags and script-tags ##########
###### ... as well as other extra tags ######################################
#############################################################################

##    reachEndOfText = False
##    i = 0
##
##    noMoreATags = False
##    
##    while reachEndOfText == False:
##
##        idxATagPos = text.find("<a ", i)
##        
##        #if there are no particular tags that are found,
##        #then change the "not-found" value to infinite
##        #(to help out with the conditional statements)
##        if idxATagPos == -1:
##            idxATagPos = math.inf
##
##        #print content within P-tag (if it comes before other tags)
##        if (           
##                #idxPTagPos < idxH1TagPos and idxPTagPos < idxH2TagPos and
##                #idxPTagPos < idxH3TagPos and idxPTagPos < idxH4TagPos and
##                #idxPTagPos < idxH5TagPos and idxPTagPos < idxH6TagPos and
##                idxATagPos != math.inf
##            ):
##                idxATagBeginText = text.find("\">", idxATagPos)
##                idxATagEndText = text.find("</a>", idxATagBeginText)
##
##                print("begin: " + str(idxATagBeginText))
##                print("end: " + str(idxATagEndText))
##
##                ###print(text[idxATagBeginText + 3 : idxATagEndText])
##
##                #gatheredText = gatheredText + text[idxATagBeginText + 3 : idxATagEndText] + "\n"  
##                i = idxATagEndText
##                
##        #if we reach the end of the html-file, then we have completely
##        #found all the text that we need to display!
##        elif (
##                idxATagPos == math.inf
##            ):
##                reachEndOfText = True









#############################################################################
###### Return the completed code to be printed ##############################
#############################################################################
        
    #####f.close()

    #########TEST PRINT#########
    #print(gatheredText)
    
    return gatheredText


#########TEST THE FUNCTION#########
#textDisplay("hello_textDisplay.htm")










