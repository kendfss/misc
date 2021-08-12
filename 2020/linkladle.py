# from multiprocessing import Pool
# import os



# def f(x):
    # return x*x
    


# if __name__ == '__main__':
    # print(os.cpu_count())
    # with Pool(5) as p:
        # print(p.map(f, [1, 2, 3]))
        
# import stdio
# import sys

# n = int(input(sys.argv[0]+'\nPick a number, any number\n'))

# arr= [-i for i in range(1,n+1)]

# print(arr)



import csv, re, urllib.request, os
import requests
from bs4 import BeautifulSoup
# from IPython.display import HTML

def exists(link) -> bool:
    """
    Check if request response is 200
    """
    try:
        return 200 == requests.get(link).status_code
    except requests.exceptions.MissingSchema:
        return False
    except requests.exceptions.InvalidSchema:
        return False
        
def scrapeLinks(url):
    yielded = set()
    page = requests.get(url).text
    soup = BeautifulSoup(page,"html.parser")
    for a in soup.find_all('a',href=True):
        link = a['href']
        if not link in yielded and exists(link):
            yield link
            yielded.add(link)
            
# Program that scraps the website for 
url = 'https://www.census.gov/programs-surveys/popest.html'
url = 'http://bumba.org/'
# r = urllib.request.urlopen(url).read()
r = requests.get(url).text
soup = BeautifulSoup(r,"html.parser")
# for link in soup.find_all('a'): print(link.get('href'))

# links = [
        # a['href'] for a in soup.find_all('a',href=True)\
        # if exists(a['href'])
    # ]

file_name = "Giles_C996.csv"
with open(file_name,"w") as csv_file:
    # writer = csv.writer(csv_file),delimiter="/n")
    writer = csv.writer(csv_file)
    # writer.writerow(set(links)) # conversion to remove duplicates
    writer.writerow(scrapeLinks(url)) 
    # writer.writerows(enumerate(scrapeLinks(url),1))  ## if you want a 2d-indexed collection
    
os.startfile(file_name)

# Close()
