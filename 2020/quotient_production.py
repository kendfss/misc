"""
How many ways are there to form a quotient in a set of N consecutive integers?
"""
from itertools import permutations, chain
from collections import defaultdict

from m3ta import join, show, function

def classes(n, key:function=lambda x: x, zerodivs:bool=False):
    """
    Sort the viable quotients of range(n) into congruence classes
    """
    cache = defaultdict(list)
    for a, b in permutations(range(n), 2):
        if key(b) != 0:
            div = key(a) / key(b)
            cache[div].append((a, b))
        elif zerodivs:
            cache['undefined'].append((a, b))
    return cache
    
def classify(array, key:function=lambda x: x, zerodivs:bool=False):
    """
    Sort the viable quotients of any array of divisible elements into congruence classes
    """
    cache = defaultdict(list)
    for a, b in permutations(array, 2):
        if key(b) != 0:
            div = key(a) / key(b)
            cache[div].append((a, b))
        elif zerodivs:
            cache['undefined'].append((a, b))
    return cache
    
    
def diffs(array, key:function=lambda x: x):
    """
    Compute the difference between consecutive elements of an array.
    """
    last = None
    for i in array:
        if last != None:
            yield key(i) - key(last)
        last = i

# print([*diffs(range(3))])
for n in range(10)[::-1]:
    cls = classes(n)
    clss = [*chain.from_iterable(classes(j).keys() for j in range(n))]
    clss = sorted(set([*filter(lambda x: not isinstance(x, str), clss)]))
    report = filter(None, f"""
    {n = }
    {len([*cls.keys()]) = }
    {len([*chain.from_iterable(cls.values())]) = }
    {clss = }
    """.splitlines())
    report = join(report, sep='\n')
    print(report)
    show((join([key, val], sep='\n\t\t') for key,val in cls.items()),1)
    