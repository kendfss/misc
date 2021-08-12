from PDFNetPython3 import PDFDoc, TextExtractor()
from m3ta import show, pop, Directory, File


path = r"C:\Users\Kenneth\downloads\byextension\pdf\Dr_Faustroll.pdf"
# def extract(path)
extractor = TextExtractor()
doc = PDFDoc(path)

help(doc)
    

# show(doc.GetPages())
for i in doc.GetPages():
    print(i)