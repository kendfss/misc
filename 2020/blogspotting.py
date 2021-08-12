# encoding=utf8
from bs4 import BeautifulSoup
import requests
from m3ta import show

string = requests.get("http://devlinsangle.blogspot.com/feeds/posts/default").text
soup = BeautifulSoup(string, 'lxml')
print(soup.prettify())


pairs = []

    # if
# show({c['term'].strip() for c in soup.find_all('category')})
# show((t.text.strip() for t in soup.find_all('title')))
# show(soup.find_all())
# for i, e in enumerate(soup.find_all()):
def scrapeBlogSpot():
    # contents = soup.find_all('content')
    # for title in soup.find_all('title'):
        # if title.next in contents:
            # yield title, title.next
    for a in soup.find_all('link', title=True):
        if a['title'] and not 'comments' in a['title'].lower():
            yield a['title'].strip(), a['href']
for i, j in scrape():
    print(i)
    print(j)
    print('.'*24)