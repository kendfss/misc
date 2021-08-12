import os,random
import pyttsx3, pyperclip
from PyPDF2 import PdfFileReader as reader

# help(slate)
# print(slate.__file__)
# pyperclip.copy(slate.__file__)


def play(page):
    eng = pyttsx3.init()
    eng.say(page)
    eng.runAndWait()

if __name__ == '__main__':
    fp = r"C:\Users\Kenneth\Documents\bookes\bostrom-superintelligentwill.pdf"
    loc = r'C:\Users\Kenneth\Documents\bookes'
    files = tuple(os.path.join(loc,i) for i in os.listdir(loc) if i.lower().endswith('.pdf'))
    fp = random.choice(files)
    print(files)
    print(fp)
    with open(fp,'rb') as f:
        # doc = slate.PDF(f)
        doc = reader(f)
        # doc.close()
        
        print(doc.numPages)
        pages = tuple(doc.getPage(i).extractText() for i in range(doc.numPages))
        print(pages)
    
    
    
    
    pass