import os, re, urllib

from bs4 import BeautifulSoup
import requests

from sl4ng import show

url = 'http://the-eye.eu/public'
r = requests.get(url)
u = urllib.request.urlopen(url)
soup = BeautifulSoup(r.text, 'lxml')

show(filter(lambda x: re.match('^.*/$', x['href']), soup.find_all('a')))