
def placeholderImageVideo(html):

    f = open(html, 'r')
    text = f.read()

    #look for all image-tags, and add an "image placeholder"
    reachEndOfText = False
    i = 0
    while reachEndOfText == False:
        idxImgTag = text.find("<img", i)
  
        if idxImgTag != -1:

            idxImgTagEnd = text.find(">", idxImgTag)
            

            textBeforeImgTag = text[:idxImgTag]
            textAfterImgTag = text[idxImgTagEnd + 1:]

            text = textBeforeImgTag + "<p>IMAGE PLACEHOLDER</p>" + textAfterImgTag            
            i = text.find("</p>", idxImgTag)
            
        else:
            reachEndOfText = True

    #look for all video-tags, and add a "video placeholder"
    reachEndOfText = False
    i = 0
    while reachEndOfText == False:
        idxVideoTag = text.find("<video", i)
  
        if idxVideoTag != -1:

            idxVideoTagEnd = text.find("</video>", idxVideoTag)

            textBeforeVideoTag = text[:idxVideoTag]
            textAfterVideoTag = text[idxVideoTagEnd + 8:]

            text = textBeforeVideoTag + "<p>VIDEO PLACEHOLDER</p>" + textAfterVideoTag            
            i = text.find("</p>", idxVideoTag)
            
        else:
            reachEndOfText = True

    f.close()
    
    return text
