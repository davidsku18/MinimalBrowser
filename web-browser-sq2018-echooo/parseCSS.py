import re, time
import getURL

def removeWhitespace(css):
    return css.strip(" ").strip().replace("\n","").replace("\t","").replace("\r","").replace("   ", "")

def makeContentDict(group):
    subDict = {}
    mGroup = group.split(";")
    if mGroup[-1] != '': mGroup = mGroup[:-1]
    if len(mGroup) == 0: mGroup = [group]
    for i in range(len(mGroup)):
        s = mGroup[i].split(":")
        if len(s) == 2:
            #if not "{" in s[0].strip() or not "}" in s[1].strip():
            subDict[s[0].strip()] = s[1].strip()
    return subDict

def getEntries(css, arr=[]):
    regexString = '[^{}]*{([^}])*}'
    if re.search(regexString, css):
        for m in re.finditer(regexString, css):
            arr.append(removeWhitespace(m.group().strip()))
    
    arrRemove = []
    for i in range(len(arr)):
        if arr[i].count("{") == 2:
            if i+1 < len(arr):
                arr[i] = arr[i] + arr[i+1] + "}"
                arrRemove.append(arr[i+1])
    
    for rem in arrRemove:
        if rem in arr: arr.remove(rem)
    return arr

def parseEntries(css, entriesDict={}):
    entriesArr = getEntries(css)
    entries = [entriesArr[i][:-1].split("{") for i in range(0, len(entriesArr))]
    for entry in entries:
        entriesDict[entry[0].strip()] = makeContentDict(entry[1].strip())
        entriesDict[entry[0].strip()]["__level"] = 0
    return entriesDict

def printDic(cssDict):
    print(cssDict)
    
    if 'body' in cssDict.keys() and 'background-color' in cssDict['body'].keys():
        print("Background Color:", cssDict['body']['background-color'])

def getComments(css):
    arr = []
    regexString = '\/\*(.|\n)*?\*\/'
    if re.search(regexString, css):
        for m in re.finditer(regexString, css):
            arr.append(m.group())
    return arr

def removeComments(css):
    comments = getComments(css)
    for comment in comments:
        css = css.replace(comment, "")
    return css

def parseFile(fname):
    css = removeComments(open(fname,"r").read())
    return parseEntries(css)

def parseURL(url):
    css = getURL.getURL(url).replace("\t", "").replace("\n", "")
    css = removeComments(css)
    #return makeDict(css)
    return parseEntries(css)

def testMain():
    cssDict = parseFile("test5.css")
    print(cssDict.keys())
    for i in cssDict.keys(): print(i+":", cssDict[i])

def main():
    testMain()
    css = removeComments(open("test5.css").read())
    for i in getEntries(css):
        print(i)
        print()

if __name__ == '__main__':
    main()
