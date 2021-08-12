from itertools import combinations, chain, filterfalse
from functools import reduce
from sl4ng import show


user_input=['a','b','c']

ddict = {
    'd1': ['a','c','d'],
    'd2': ['a','b','e','f'],
    'd3': ['a','c','b','f'],
    'd4': ['b'],
    'd5': ['g','e','a'],
    'd6': ['g']
}
# dlist = [d1,d2,d3,d4,d5,d6]

def freq(element, iterable):
    return sum(i == element for i in iterable)

def counter(user_input):
    def wrap(d_n):
        return sum(i in d_n for i in user_input)

def matchbot(user_input):
    cache = set()
    # perfect = lambda i: all(j in i for j in user_input)
    perfect = lambda i: all(j in ddict[i] for j in user_input)
    # best, rest = filter(perfect, dlist), filterfalse(perfect, dlist)
    best, rest = filter(perfect, ddict), filterfalse(perfect, ddict)
    # for i in sorted(best, key=len):
    for i in sorted(best, key=lambda x: len([]):
        # yield i
        yield ddict[i]
        yielded.append(ddict[i])
    
    candidates = filter(lambda x: any(i in x for i in user_input), rest)
    powerset = chain.from_iterable(combinations(candidates, r) for r in range(1, len(user_input)+1))
    for bundle in powerset:
        details = map(ddict.get, bundle)
        union = reduce(lambda x, y: x+y, details, [])
        bool0 = not any(union.count(i) > 1 for i in user_input)
        bool1 = all(i in union for i in user_input) 
        if :
            
        # if reduce(lambda x, y: x ^ y )
        # union = reduce(lambda x, y: x+y, bundle, [])
        
        if :
            yield bundle
        



show(matchbot(user_input))