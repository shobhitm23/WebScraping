import webbrowser
from bs4 import BeautifulSoup
import requests
import os
import urllib2

new = 2
query = raw_input("Enter Search Term: ")
url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"

# Opening the webpage
#webbrowser.open(tabUrl)

#soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url)), 'html.parser')
#print(soup)

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
try:
    r = requests.get(url, headers=headers, timeout=1)
except requests.exceptions.Timeout:
    print("Timeout occurred")
    
#print(r.content)
#print("==========================================")
soup = BeautifulSoup(r.content, 'html.parser').encode('utf-8')
print(soup)
#print(soup.prettify())
