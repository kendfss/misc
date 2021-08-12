import os
from m3ta import straw, main

def straw(path:str, text:bool=True, lines:bool=False) -> [str, list]:
    """
    Extract the text, or bytes if the keyword is set to false, from a file
    ::text::
        text or bytes?
    ::lines::
        split text by line or return raw?
    """
    if os.path.isfile(path):
        mode = "rb r".split()[text]
        with open(path, mode) as f:
            return f.readlines() if lines else f.read()


if eval(main):
    print(straw(__file__, True, True))
    print('\n'*7)
    print(straw(__file__, True, False))
    print('\n'*7)
    print(straw(__file__, False, False))
    print('\n'*7)
    print(straw(__file__, False, True))
    print('\n'*7)
    
    help(straw)