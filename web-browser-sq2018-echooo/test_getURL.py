import pytest
import getURL

def test_getURL():
    assert getURL.getURL("https://rtsfred3.github.io/echoo/").strip() == """<!DOCTYPE html>
<html>
    <head>
        <title>rtsfred3.github.io</title>
    </head>
    <body>
        <font class="all">
            HelloWorld<br />
            Scripts:
            <script src="https://status.github.com/api/status.json?callback=Status"></script>
            <script src="https://status.github.com/api/messages.json?callback=Messages"></script>
        </font>
    </body>
</html>"""
    
def test_getURL2():
    assert getURL.getURL("https://rtsfred3.github.io/echoo/index2.html").strip() == """<!DOCTYPE html>
<html>
    <head>
        <title>rtsfred3.github.io/index2.html</title>
    </head>
    <body>
        <div><p>This is index2.html</p></div>
    </body>
</html>"""
