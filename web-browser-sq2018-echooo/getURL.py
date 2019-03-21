import requests

def getURL(url):
    headers = {'user-agent': 'Mozilla/5.0 (Python3; rv:17.0) Gecko/20100101 Firefox/17'}
    return requests.get(url, headers=headers).text


getURL("https://docs.python.org/3/library/urllib.request.html")
#print(getURL("https://docs.python.org/3/library/urllib.request.html"))
#print(getURL("http://google.com"))
