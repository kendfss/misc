import xml
from xml.parsers.expat import ParserCreate


# p = parsers.expat.ParserCreate()
p = ParserCreate()

with open(r'C:\Program Files (x86)\notepadpp.7.8.5.bin\themes\Obsidian.xml','rb') as styling:
    stylesheet = p.ParseFile(styling)
    print(stylesheet)
    help(p)