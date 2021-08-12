"""\
Scrape (and listen to) the html and/or text of an adblocked (and any other non-bot-weary) webpage\
"""
# ```
import os, re, urllib
from itertools import tee

import requests, pyttsx3
from bs4 import BeautifulSoup

from sl4ng import show, join


HEADERS = {
    'user-agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/45.0.2454.101 Safari/537.36'
    ),
    'referer': 'http://stats.nba.com/scores/'
}
# https://stackoverflow.com/questions/36853651/python-requests-get-iterating-url-in-a-loop


def clean(url):
    out = url[:]
    while url.startswith('/'):
        out = out[1:]
    while url.endswith('/'):
        out = out[:-1]
    return out


def setname(url:str,ext:str='.txt') -> str:
    # title = url.split('/')[-1].replace('#','')
    # while re.search('^.+-\d+',title):
        # title = '-'.join(title.split('-')[:-1])
    # return title+ext
    parse = urllib.parse.urlparse(url)
    title = parse.path.strip('/').split('/')[-1].replace('-', ' ').replace('+', ' ')
    source = parse.netloc.split('.')[-2]
    return join(source, title, sep='-')+ext
    

def scrapePage(url:str,save:bool=True,name:str=None) -> str:
    name = setname(url,'.html')
    r = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(r.text,'lxml')
    content = tee(p for p in soup.find_all('p'))
    if save:
        with open(name,'w') as fobj:
            fobj.write(content[0])
    return content[1]


def scrapeText(url:str,save:bool=False,name:str=None) -> str:
    name = name if name else setname(url)
    r = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(r.text,'lxml')
    content = (p.text.strip() for p in soup.find_all('p'))
    text = '\n\t'.join(content)
    if save:
        print(f'Saving:\t{name}')
        with open(name,'w') as fobj:
            fobj.write(text)
    return text


def load(url:str,save=False,ext:str='.txt') -> str:
    try:
        with open(setname(url,ext),'r') as fobj:
            text = ''.join(fobj.readlines())
    except FileNotFoundError:
        try:
            with open(url,'r') as fobj:
                text = ''.join(fobj.readlines())
        except FileNotFoundError:
            scrapeText(url,save)
            load(url)
    return text
    

def narrate(url:str,ext='.txt') -> None:
    text = load(url,ext)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def getlinks(url,bind=False) -> list:
    r = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(r.text,'lxml')
    if bind:
        refs = ['/'.join((url,a['href'])) for a in soup.find_all('a',href=True) if not 'mailto:' in a['href']]
    else:
        refs = [a['href'] for a in soup.find_all('a',href=True) if not 'mailto:' in a['href']]
    # refs = [a for a in soup.find_all('a',href=True)]
    return refs
    
    
def bandcamp(url,mode='music') -> list:
    url = clean(url)
    r = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(r.text,'lxml')
    refs = ['/'.join((url,clean(href))) for a in soup.find_all('a',href=True) if 'action=download' in (href:=a['href'])]
    return refs
    


 

if __name__ == '__main__':
    url = 'https://markets.businessinsider.com/news/stocks/robinhood-stock-market-controversial-week-traders-cyberattack-accounts-trading-margin-2020-10-1029690410#'
    url = 'https://blindhypnosis.com/the-idiot-pdf-fyodor-dostoyevsky'
    url = 'https://leonvynehall.bandcamp.com/album/rojus-designed-to-dance'
    url = 'https://www.cprogramming.com/tutorial/c++-tutorial.html?inl=pf'
    url = 'https://www.forbes.com/sites/gilpress/2018/02/07/the-brute-force-of-deep-blue-and-deep-learning/?sh=5ce2101a49e3'
    url = 'http://ubiquity.acm.org/article.cfm?id=2667647'
    url = 'https://www.forbes.com/sites/bernardmarr/2018/02/19/the-5-big-problems-with-blockchain-everyone-should-be-aware-of/?sh=56a8eac61670'
    # url = 'https://www.wired.com/story/ai-beat-humans-at-reading-maybe-not/'
    # url = 'https://www.cloudflare.com/5xx-error-landing'
    # print(setname(url))
    # links = getlinks(url)
    # links = bandcamp(url)
    # print(links)
    # show(links,enum=True)
    # text = load(url)
    directory = r'C:\Users\Kenneth\Downloads\blockchain'
    os.chdir(directory)
    text = scrapeText(url,True)
    print(text)
    # narrate(url)
# ```