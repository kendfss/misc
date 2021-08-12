"""
Goal here is to implement those trays/pyramids from LIS days
Perhaps define a "cycle" object that behaves like a generator but restores itself upon the end of its iterative life


"""
from math import e,pi

import numpy as np

def diff(iterable):
    return tuple(iterable[i]-iterable[i-1] for i in range(1,len(iterable)))
def genate(iterable,start=0):
    return tuple(start+sum(iterable[:i]) for i in range(1+len(iterable)))
    # return tuple(start+(0,sum(iterable[i-1:i]))[i>0] for i in range(len(iterable)))
    
    
def level(iterable,depth=2):
    d = depth**1
    while depth:
        iterable = diff(iterable)
        depth -= 1
        if len(iterable)<1:
            raise ValueError(f'Desired depth exceeds that of the incident sequence. Try depth={d-1}')
    return iterable

def pyramid(iterable):
    if hasattr(iterable,'__len__'):
        l = len(iterable)**1
        # print(f'pyramid{l}')
        while len(iterable)>0 and not all(i==0 for i in iterable):
            yield iterable
            iterable = diff(iterable)
def height(iterable):
    return len(list(pyramid(iterable)))
def area(iterable):
    # return height(iterable)*len(iterable)/2
    return height(iterable)*(max(iterable)-min(iterable))/2
    
def kinks(iterable):
    deltum = diff(iterable)
    kinked = (i for i,j in enumerate(deltum,1) if deltum[i-1]!=deltum[i-2])
    return tuple(kinked)
    
def flat(iterable):
    d = diff(iterable)
    return all(i==d[0] for i in d[1:])
    


r = 70
t = tuple(range(r))
# t = [i**100 for i in range(1,r)]
# t = [e/(pi*i) for i in range(1,r)]
# t = np.sin(np.linspace(0,1,50))
print(f"""\
{t = }
{diff(t) = }
{genate(t) = }
{kinks(t) = }
{flat(kinks(diff(t))) = }
{height(t) = }
{area(t) = }
{level(t,4)[:0] = }
{diff(genate(t))==genate(diff(t)) = }
    """
)
print()
print()
print()
print()
print()
[print(i) for i in pyramid(t)]