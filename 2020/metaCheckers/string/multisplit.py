from m3ta import gen, show, chords, flatten as chain
from itertools import chain, tee
from typing import Sequence

def multisplit(splitters:Sequence[str], target:str) -> gen:
    """
    Split a string by a sequence of arguments
    >>> list(multisplit(',`* ', 'wma,wmv mp3`vga*mp4 ,`*  ogg'))
    ['wma', 'wmv', 'mp3', 'vga', 'mp4', 'ogg']
    """
    splitters = iter(splitters)
    result = target.split(next(splitters))
    for splitter in splitters:
        result = [*chain.from_iterable(i.split(splitter) for i in result)]
    yield from filter(None, result)

# multisplit('a b c'.split(), 'carrot cabbage macabre'.split(','))
x, y = tee(multisplit('a b c'.split(), 'carrot cabbage macabre'))
x, y = tee(multisplit(',`* ', 'carrot cabbage macabre'))
x, y = tee(multisplit(',`* ', 'wma,wmv mp3`vga*mp4 ,`*  ogg'))
x, y = tee(multisplit('z', 'wma,wmv mp3`vga*mp4 ,`*  ogg'))
show(x)
print(list(y))