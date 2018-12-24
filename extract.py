import pandas as pd
import numpy as np
import urllib
from bs4 import BeautifulSoup

url = 'https://www.bloomberg.com/asia'
html_bb = urllib.urlopen(url)
# print(html_bb)

soup_obj = BeautifulSoup(html_bb, 'lxml')
print(type(soup_obj))
