import webbrowser
from bs4 import BeautifulSoup
import requests
import os
import urllib2


query = raw_input("Enter Search Term: ")
url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
# Opening the webpage
#webbrowser.open(tabUrl)
#soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url)), 'html.parser')
#print(soup)
REQUEST_HEADER = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

def get_soup(url,headers):
    try:
        r = requests.get(url, headers=REQUEST_HEADER, timeout=1)
    except requests.exceptions.Timeout:
        print("Timeout occurred")
    return BeautifulSoup(r.content, 'html.parser')


#print(r.content)
#print("==========================================")
#print(soup)
#print(soup.prettify())

def getRawImg(url):
    req = Request(url, headers=REQUEST_HEADER)
    res = urlopen(req)
    return res.read()

soup = get_soup(url, REQUEST_HEADER)
print(soup)
print(getRawImg(url))
