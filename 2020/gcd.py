from m3ta import gcd0 as gcd,shuffle
from random import randint


def gcd2(*args):
    """
    Compute the gcd for more than two integers at a time. Returns input if only one argument is given and it is greater than zero
    Dependencies: itertools.combinations
    In: subscriptable
    Out: int
    """
    from itertools import combinations
    if len(args)>1:
        gcds = {d for pair in combinations(args,2) if all(i%(d:=gcd(*pair))==0 for i in args)}
        return max(gcds)
    elif sum(args)>0:
        return args[0]
    

if __name__=='__main__':
    # print(gcd2(10,15,90))
    # print(gcd2(randint(2,1000)))
    l = 20
    ints = tuple(randint(2,100) for i in range(l))
    # ints = range(2,l,2)
    # test = lambda r: [print(rack),[print(gcd2(*rack[:i]))]]
    print(gcd2(*ints[:1]))
    print(gcd2(*ints[:2]))
    print(gcd2(*ints[:3]))
    print(gcd2(*ints[:4]))
    print(gcd2(*ints[:5]))
    print(gcd2(*ints[:6]))
    print(gcd2(*ints[:7]))
    print(gcd2(*ints[:8]))
    print(gcd2(*ints[:9]))
    # print(gcd2(*(randint(2,100) for i in range(2))))
    # print(gcd2(*(randint(2,100) for i in range(3))))
    # print(gcd2(*(randint(2,100) for i in range(4))))
    # print(gcd2(*(randint(2,100) for i in range(5))))