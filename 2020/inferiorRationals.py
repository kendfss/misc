"""
7:29

Proof that it is/isn't possible to express all rationals qi inferior to some natural n as ratios qi=a,b where b <= n
"""

from itertools import chain, count, product, permutations

from continuumHypothesis_2 import toString, digits

# help(count)

# for i in count(5): print(i)
# def count(start,end,step=1):
    # while start<end:
        # yield start
        # start += step
# for i in count(0,5): print(i)

        
# digits = {0,1,2,3,4,5,6,7,8,9}

    
def naturalNumbers(end,start=0):
    bag = (int(toString(nat)) for nat in chain.from_iterable(product(digits,repeat=i) for i in count(start=1)) if toString(nat)==toString(int(toString(nat))))
    for i in bag:
        if i<end:
            if i>=start:
                yield i
        else: return
        
# for i in range(1,10):
    # print(f'for {i}:')
    # for j in naturalNumbers(i):
        # print(j)
    # print('\n\n')

# def inferiors(end,start=0):
    # bag = (int(toString(nat)) for nat in chain.from_iterable(product(digits,repeat=i) for i in count(start=1)) if toString(nat)==toString(int(toString(nat))))
    # q0 = float(end).as_integer_ratio()
    # div = lambda n,m: n/m
    # pairs = permutations(bag,2)
    # q = (div(pair[0],pair[1]) for pair in pairs)
    # return q

print(inferiors(3))
