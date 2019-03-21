from tkinter import *
import parseCSS
import getURL

from urllib.parse import urlsplit

def getCSSFiles(html, arr=[]):
    regexString = '<link[^>]*?href="([^"]+)">'
    if re.search(regexString, html):
        for m in re.finditer(regexString, html):
            arr.append(m.group().strip())
    
    regexString = 'href="([^"]+)"'
    for i in range(0, len(arr)):
        #print('rel="stylesheet"' in arr[i])
        if re.search(regexString, arr[i]):
            for m in re.finditer(regexString, arr[i]):
                arr[i] = m.group().strip()[6:-1]
    return arr

def getInlineCSS(html, arr=[]):
    regexString = '<style([^>])*>([^<])*<\/style>'
    if re.search(regexString, html):
        for m in re.finditer(regexString, html):
            arr.append(m.group().strip())
    
    regexString = '>([^<]+)</'
    for i in range(0, len(arr)):
        if re.search(regexString, arr[i]):
            for m in re.finditer(regexString, arr[i]):
                arr[i] = m.group().strip()[1:-2]    
    return arr

def getBackground(html, url=None):
    cssFiles = getCSSFiles(html, [])
    for css in cssFiles:
        cssDict = None
        if "http://" in css or "https://" in css:
            cssDict = parseCSS.parseURL(css)
        if css[0:2] == "//":
            cssDict = parseCSS.parseURL("http:" + css)
        elif css[0:1] == '/' and css[0:2] != "//" and url != None:
            base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
            cssDict = parseCSS.parseURL(base_url + css)
        
        
        if css is not None and cssDict is not None and 'body' in cssDict.keys() and 'background-color' in cssDict['body'].keys():
            return cssDict['body']['background-color']
        
        if css is not None and cssDict is not None and 'body#' in cssDict.keys():
            for key in cssDict.keys():
                #print("body" in key)
                if "body" in key:
                    return cssDict[key]['background-color']
    
    cssInline = getInlineCSS(html, [])
    for css in cssInline:
        cssDict = parseCSS.parseEntries(parseCSS.removeComments(css))        
        if css is not None and 'body' in cssDict.keys() and 'background-color' in cssDict['body'].keys():
            return cssDict['body']['background-color']        
    return 'white'

def test():
    #url = 'https://www.websitebuilderexpert.com/how-to-choose-color-for-your-website/'
    url = 'http://www.catallianceteam.org/'
    html = getURL.getURL(url)
    
    print(getBackground(html))

def main():
    root = Tk()
    root.geometry("100x100")
    
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    textFrame = Frame(root)
    textFrame.pack(side=BOTTOM)
    
    url = 'https://www.websitebuilderexpert.com/how-to-choose-color-for-your-website/'
    #url = 'http://www.catallianceteam.org/'
    html = getURL.getURL(url)
    print(getBackground(html))
    
    displayText = Text(textFrame, yscrollcommand=scrollbar.set)
    scrollbar.config(command=displayText.yview)
    displayText = Text(root, background=getBackground(html, url))
    displayText.pack()
    
    root.mainloop()

if __name__ == '__main__':
    test()
