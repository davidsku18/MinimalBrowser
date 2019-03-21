import pytest
import basicUI

def test_open():
    basicUI.open("https://up.edu")
    assert len(basicUI.history) == 2


def test_back():
    basicUI.open("https://up.edu")
    basicUI.goBack()
    assert basicUI.currentIndex == 0

def test_forward():
    basicUI.open("https://up.edu")
    basicUI.goBack()
    basicUI.goForward()
    assert basicUI.currentIndex == 1
