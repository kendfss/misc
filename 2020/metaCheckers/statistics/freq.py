from typing import Any, Iterable
import random
from m3ta import freq,alphabet,chords,join,eq

def freq(element:Any, iterable:Iterable, greedy:bool=False) -> int:
    """Returns the number of appearences of some term in some collection
    Will run silently if the greedy flag is incorrectly set to True
    Dependencies: N/A
    In: (term, name of collection)
    Out: number"""
    if greedy:
        if hasattr(element,'__len__'):
            if not len(element) > 1:
                return freq(element,iterable,False)
            # elif isinstance(element,str):
            elif eq(*map(type,(element,iterable)),str):
                return len(iterable.split(element)) - 1
            return freq(tuple(i for i in element),chords(iterable,len(element)))
        return freq(element,iterable,False)
    else:
        # if isinstance(element,str):
            # return len(iterable.split(element)) - 1
        return sum(1 for i in iterable if i==element)
    

# r = random.randint(1,13)
# shif = r%len(alphabet)
# lis = [random.choice(alphabet[shif:shif+r])*(i*0+1) for i in range(r)]
# s = ''.join(lis)

# print(len(s),r,shif,lis,s,sep='\n')
# for i in set(sorted(lis)):
    # print(i,freq(i,lis),freq(i,s))

t = 'tt'
print(t)
for i in range(5):
    el = i*'test'
    lis = i*['test']
    # lis = [*el]
    mat = [*(lis for i in range(i))]
    # stlis = st
    print(
        i,
        f'"{el}"',
        freq(t,el),
        freq(t,el,True),
        lis,
        freq(t,lis,True),
        mat,
        freq(lis,mat,True),
        sep='\n\t'
    )