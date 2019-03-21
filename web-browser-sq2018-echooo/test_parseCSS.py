import pytest
import parseCSS

def test_CSS():
    keys = parseCSS.parseFile("test.css").keys()
    assert [i for i in keys] == ["body", "h1", "p"]

def test_CSS2():
    entryDict = parseCSS.parseFile("test2.css")
    entries = [entryDict[i] for i in entryDict.keys()]
    
    assert entries == [{"background-color":"lightblue", '__level': 0}, {"color":"white","text-align":"center", '__level': 0}, {"font-family":"verdana", "font-size":"20px", '__level': 0}]

def test_CSS3():
    assert parseCSS.parseFile("test2.css") == {"body":{"background-color":"lightblue", '__level': 0}, "h1":{"color":"white","text-align":"center", '__level': 0}, "p":{"font-family":"verdana","font-size":"20px", '__level': 0}}

def test_CSS4():
    d = "@keyframes fa-spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(359deg);transform:rotate(359deg)}}"
    css = parseCSS.removeComments(open("test5.css").read().strip()).strip()
    output = parseCSS.getEntries(css, [])
    
    print(output[0] == d)
    assert output[0] == d
