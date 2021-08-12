from itertools import starmap, islice
from typing import Iterable, Any

from m3ta import main, show, slices, walks, generator

class Null:
    def __bool__(self):
        return False

# def slices(iterable, length, fill=None):
    # pot = []
    # ipot = []
    # last = Null()
    # for i, e in enumerate(iterable):
        # if len(pot)<length:
            # pot.append(e)
            # ipot.append(i)
        # elif len(pot)==length:
            # yield tuple(pot)
            # pot = []
            # ipot = []
        # else:
            # raise ValueError('muddafukfukr')
        # last = i
    # if not last in ipot:

# def slices(iterable, length, fill=None):
    # for i, e in enumerate(walks(iterable, length)):
        # if not i%length:
            # yield e
def slices(iterable:Iterable, length:int, fill:Any=None) -> generator:
    """
    Yield the adjacent slices of a given length for the given iterable. Trailing values will be padded by copies of 'fill'
        use filter(all, slices(iterable, length)) to discard remainders
    :fill:
        the default value of any 
    eg:
        >>> [*slices('abc', 2, None)]
        [('a', 'b'), ('c', None)]
        >>> [*filter(all, slices('abc', 2, None))]
        [('a', 'b')]
    """
    itr = iter(iterable)
    while (main:=[*islice(itr, 0, length)]):
        main += [fill for i in range(length-len(main))]
        yield tuple(main)

if eval(main):
    n, m = 7, 10
    ts = 'abcde'
    tests = [
        # (range(n), m),
        # ((i for i in range(n)), m),
        (range(n), i) for i in range(1, m+1)
    ]
    show(tests)
    # show((list(i[0]), i[1]) for i in tests)
    show(map(list, starmap(slices, tests)))
    print()
    print([*filter(all, slices(ts, 2))])
    print([*filter(all, slices(ts, 2, float('nan')))])
    print([*slices(ts, 2, float('nan'))])
    # show(map(list, filter(all, starmap(slices, tests))))
    # for i in tests:
        # print([*filter(all, slices(*i))])