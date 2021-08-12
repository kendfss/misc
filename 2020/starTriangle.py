"""

"""
from typing import Iterable
from math import ceil
from itertools import cycle, permutations
from m3ta import shuffle, abc, sample, freq#, indices
from random import choice
from time import sleep
from PIL import Image, ImageDraw, ImageFont

def pull(iterable:Iterable,stop:int,start:int=0) -> tuple:
    '''
    Return 'stop' elements from an effective cycle of the iterable, using only those whose modulus is greater than 'start'
    Dependencies: typing.Iterable
    In: Iterable,int,int
    Out: tuple
    
    Example:
        pull('boris',5)
            ('b', 'o', 'r', 'i', 's')
        pull('boris',6)
            ('b', 'o', 'r', 'i', 's', 'b')
        pull('boris',6,1)
            ('o', 'r', 'i', 's', 'b', 'o')
    '''
    stop = stop if stop else len(iterable)
    return tuple(iterable[i%len(iterable)] for i in range(stop+start) if i>=start)

# iterable = 'boris'
# stop = 5
# start = 1
# s = 'eli sandro jesslem zerba zerbaman miage 5910 boob zek zekone naks sleepyk'
# p = ''.join(shuffle('.,~`:'))
# for i,j in zip(sierpinstr(n,s,p),st(n,s,p)): print(j,i)
# print(f'{iterable = }\n{start = }\n{stop = }')
# print(s)
# print(pull(iterable))
# print(pull(iterable,stop))
# print(pull(iterable,stop+1))
# print(pull(iterable,stop+1,start))
# help(pull)
def center(string:str,length:int,padder:str=' '):
    pass
def st(n:int,string:str='*',padder:str=' ',randomize:bool=False,static:bool=False) -> type(i for i in range(0)):
    """
    Generate a sequence of strings that print as a pyramid of a given word
        each row is centralized by characters from a the given padder
        in given or randomized order.
        The static handle enables the user to choose just one random character from the pad-string
    Dependencies:
    In:
    Out:
    
    Inspired by question 70:
        https://towardsdatascience.com/80-python-interview-practice-questions-f1640eea66ac
        While this implementation does not behave well when terms are printed adjacently, 
        it does solve the problem of incomplete padding when using non-space-like pad-strings
    """
    from random import choice
    from itertools import cycle
    padder = cycle((padder,(choice(padder),shuffle(padder))[not static])[randomize])
    row = lambda i: ((2*i+1)*string)
    for i in range(n):
        yield(row(i).center(len(row(n-1)),next(padder)))
        
def sierpinstr(n,string:str='*',padder:str=' '):
    parentheticals = {
        '(':')',
        ')':'(',
        '[':']',
        ']':'[',
        '{':'}',
        '}':'{',
        '/':'\\',
        '\\':'/',
        '<':'>',
        '>':'<',
        # '^':'v',
        # 'v':'^',
        # ',':'`',
        # '`':',',
    }
    for x in range(n):
        # pad = padder*(n-x-1)
        buff = padder*(n-x-1)
        shut = ''.join((i,parentheticals.get(i))[i in parentheticals] for i in padder[::-1])*(n-x-1)
        # yield(pad+string*(2*x+1)+pad[::-1]) 
        yield(buff+string*(2*x+1)+shut) 

def casemap(word):
    transforms = {i:[i.upper(),i.lower()][i.isupper()] for i in abc('pd')}
    return {k:v for k,v in transforms.items() if k in set(word)}
    

def lettermap(word):
    options = {
        'a':'@ 4 /-\\ /~\\'.split(),
        'b':'13 & 8'.split(),
        'c':'< ( [ {'.split(),
        'd':'|> |) |] |}'.split(),
        'e':'3'.split(),
        'f':'4'.split(),
        'g':'%'.split(),
        'h':'# |-| |~| |=| /=/ /-/ /~/ \\~\\ \\-\\ \\=\\'.split(),
        'i':'1 !'.split(),
        'j':'?'.split(),
        'k':'|{'.split(),
        'l':'1 |_ \\_ /_'.split(),
        'm':'^^ nn /\\/\\'.split(),
        'n':'|\\| |/| ^ |\\ /|'.split(),
        'o':'0'.split(),
        'p':'/> '.split(),
        'q':'<\\'.split(),
        'r':'4'.split(),
        's':'$ 5'.split(),
        't':'+'.split(),
        'u':'V |__| \\__\\ /__/'.split(),
        'v':'U \\/ |/ \\|'.split(),
        'w':'vv uu \\/\\/ |_|_|'.split(),
        'x':'*'.split(),
        'y':''.split(),
        'z':''.split(),
    }
    
    for k in options: 
        options[k].insert(0,k)
        options[k].insert(1,k.upper())
    
    # how to calculate the number of variations for a given word
    freqs = {letter: freq(letter,word)*len(options[letter.lower()]) for letter in word if letter.isalpha()}
    
def photo(n,string:str='*',padder:str=' ',fontsize:float=12): 
    """
    Draw text
        Page 87 in the PIL doc pdf file
    Font sizing:
        page 101
    """
    triangle = sierpinstr(n,string,padder)
    picheight = fontsize*len()
        
    fonts = []
    # create an image
    out = Image.new("RGB", (150, 100), (255, 255, 255))
    # get a font
    fnt = ImageFont.truetype(no, fontsize)
    # get a drawing context
    d = ImageDraw.Draw(out)
    # draw multiline text
    d.multiline_text((10,10), "Hello\nWorld", font=fnt, fill=(0, 0, 0))
    out.show()
    
if __name__ == '__main__':
    for k,v in casemap('cD').items():
        print(f'{k}\t{v}')
    
    qw = 1
    row = lambda i: ((2*i+1)*string)
    t = .14159
    if 0:
        n = 8
        s = 'boris'
        # s = 'eli sandro jesslem zerba zerbaman miage 5910 boob zek zekone naks sleepyk'
        p = ''.join(shuffle('.,~`:'))
        # for i,j in zip(sierpinstr(n,s,p),st(n,s,p)): print(j,i)
        # print(s)
        # print(''.join(pull(s,5)))
        # print(''.join(pull(s,5,1)))
    elif 0:
        length = 8
        words = 'eli sandro jesslem zerba zerbaman miage 5910 boob zek zekone naks sleepyk'.split()
        # word = choice(words)
        word = 'bisto'
        pads = lambda word: (''.join(i) for i in permutations(abc('uld'),len(word)))
        # print(len(list(pads)))
        for j,pad in enumerate(pads(word)):
            print(str(j).center(len((2*length)*word)-len(word)))
            for level in sierpinstr(length,word,pad):print(level)
            # for i,level in enumerate(tuple(sierpinstr(length,word,pad))[:-1:]):print(level)
            # for i,level in enumerate(tuple(sierpinstr(length,word,pad))[::-1]):print(level)
            print()
            sleep(t)
    while 0:
        n = 8
        # words = 'cunt fuck bitch ass tits eli sandro alix perez calibre rosa hype contrast dillinja'.split()
        # s = choice(tuple(set(word[:min(len(word) for word in words)] for word in words)))
        words = 'eli sandro jesslem zerba zerbaman miage 5910 boob zek zekone naks sleepyk'.split()
        s = choice(words)
        # p = ''.join(shuffle('.,~`:'[:4]))
        p = ''.join(sample(abc('ul'),len(s)))
        # s = ''.join(sample(abc('p'),len(p)))
        # s = ''.join(sample(' OI ',len(p)))
        # s = choice([' OI ',''.join(sample('FUCK',len(p)))])
        # s = word
        # for j,i in enumerate(tuple(sierpinstr(n,s,p))[:-1:]): print(f'{j}\t{i}')
        # for j,i in enumerate(tuple(sierpinstr(n,s,p))[::-1]): print(f'{j}\t{i}')
        print(str(qw).center(len((2*n)*s)-len(s)))
        print(str(qw).center(2*(len((2*n)*s)//2+len(str(qw)))))
        print(str(qw).center(2*n*len(s)-ceil(len(s)/2)))
        print(str(qw).center(2*(len(s)*n-ceil(len(s)/2))))
        qw += 1
        for j,i in enumerate(tuple(sierpinstr(n,s,p))[:-1:]): print(f'{i}')
        # for j,i in enumerate(tuple(sierpinstr(n,s,p))[::-1]): print(f'{i}')
        print()
        sleep(t)
        
    # for i in st(n,s,p): print(i)
    