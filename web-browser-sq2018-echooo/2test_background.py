import pytest
import getURL
import tkinterBackground

def test_background():
    html = getURL.getURL("https://www.websitebuilderexpert.com/how-to-choose-color-for-your-website/")
    assert tkinterBackground.getBackground(html) == "#ebedf3"

def test_test_background2():
    html = getURL.getURL("https://www.awwwards.com/websites/colorful/")
    assert tkinterBackground.getBackground(html) == "white"

'''def test_background3():
    assert True

def test_background4():
    assert True'''
