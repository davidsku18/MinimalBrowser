import re

def removeComments(html):
    arr = []
    regexString = '<!--.*-->'
    if re.search(regexString, html):
        for m in re.finditer(regexString, html):
            arr.append(m.group())
        return arr
    return []

def getStartTags(html):
    arr = []
    regexString = '<[a-zA-Z1-9]*>'
    if re.search(regexString, html):
        for m in re.finditer(regexString, html):
            arr.append(m.group())
    regexString = '<.*>'
    if re.search(regexString, html):
        for m in re.finditer(regexString, html):
            arr.append(m.group())    
    return arr

def getEndTags(html):
    arr = []
    regexString = '<\/.*>'
    if re.search(regexString, html):
        for m in re.finditer(regexString, html):
            arr.append(m.group())
    return arr[::-1]

def getScriptTags(html):
    arr = []
    regexinfo = '<script>.*<\/script>'
    if re.search(regexinfo, html):
        for m in re.finditer(regexinfo, html):
            arr.append(m.group())
    regexinfo = '<script.*><\/script>'
    if re.search(regexinfo, html):
        for m in re.finditer(regexinfo, html):
            arr.append(m.group())
    regexinfo = '<script.*>.*<\/script>'
    if re.search(regexinfo, html):
        for m in re.finditer(regexinfo, html):
            arr.append(m.group())    
    return arr

def stripHTML(html):
    start = html.find("<body>")
    end = html.find("</body")
    html = html[start+6:end]
    
    for tag in getScriptTags(html.replace("\n","").replace("\t","").replace("\r","").replace(" ","")):
        html = html.replace(tag, "")
    
    for tag in removeComments(html):
        html = html.replace(tag, "")    
    
    for tag in getEndTags(html):
        html = html.replace(tag, "")
    
    for tag in getStartTags(html):
        html = html.replace(tag, "")    
    
    return html
