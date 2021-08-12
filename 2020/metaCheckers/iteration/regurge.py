from itertools import tee, islice
from typing import Iterable, Any, Sequence, List
from copy import deepcopy

# from m3ta import show, pop, Address, unzip

# from m3ta.cabinet import debug
# pop(debug)

# print(Address(__file__).obj)
# show(sorted(Address('.').obj, key=lambda x:x.size), 0, 1)
generator = type(i for i in '')

def regurge(iterable:Iterable[Any]):
    """
    Secure your generators by passing them through this function in order to produce a copy.
    Your generator will be replaced with a tee object.
    If your iterable is not a generator the function shall return a copy.deepcopy of it
    """
    if issubclass(type(iterable), (map, filter, generator)):
        iterable, consumable = tee(iterable)
    else:
        consumable = deepcopy(iterable)
    return consumable

def show(x):
    for i in x:
        print(i)
    print('\n\n')

if __name__ == '__main__':
    x = zip('abc', '123')
    y = regurge(x)
    show(y)
    show(x)
    show(y)
    show(x)
    