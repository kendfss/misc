from typing import Hashable
from itertools import cycle

from sl4ng import mainame, show, pop, save, load, unique, tipo, flat, choose, kbd

def dictate(dictionary:dict, *omissions:Hashable, include:bool=False):
    """
    Create a selective clone of a dictionary
    params:
        omissions
            the hashable values corresponding to keys you would like to remove
        include
            If true, only keys specified in "omissions" will persist in the final dictionary
            
    >>> dictate(dict(zip('abc', range(3))), 'a')
    {'b': 1, 'c': 2}
    >>> dictate(dict(zip('abc', range(3))), 'a', include=True)
    {'a': 0}
    >>> dictate(dict(zip('abc', range(3))), 'b c'.split(), include=True)
    {'b': 1, 'c': 2}
    
    """
    if include:
        return {key: dictionary.get(key) for key in dictionary if key in flat(omissions)}
    return {key: dictionary.get(key) for key in dictionary if not key in flat(omissions)}


def test(n, string=kbd()):
    d = dict(zip(cycle(string), range(n)))
    for i in range(n):
        yield dictate(d, choose(cycle(string), range(i)))
        yield dictate(d, choose(cycle(string), i))
        # print()


if eval(mainame):
    for i in range(10):
        print(i)
        show(test(i, 'bollocks'))
    d = {'max_len': 1, 'kind': None, 'tight': True, 'path': 'log.pkl', 'content': [1], '_Logger__index': -1, '_Logger__itr': 1}
    omittables = '_Logger__index _Logger__itr path content'.split()
    print(dictate(d, omittables))
    print({'tight': True, 'kind': None, 'max_len': 1})
    