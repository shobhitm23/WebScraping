import pandas as pd
import numpy as np
import urllib
from bs4 import BeautifulSoup
import time

url = 'https://www.bloomberg.com/asia'
html_bb = urllib.urlopen(url)
# print(html_bb)

soup_obj = BeautifulSoup(html_bb, 'html.parser')
# print(type(soup_obj))
print(soup_obj.prettify())
#print("Name: ")
#print(soup_obj.name)

text = soup_obj.get_text()
#print("-------")
#print(text)

title = soup_obj.title
print("Title: "+ str(title))

print("---------------------------------------")

# Find All
dict_a = soup_obj.find_all('a')
print(dict_a)

# Getting all the links from <a> tags
#for link in dict_a:
#    print(link.get("href"))
