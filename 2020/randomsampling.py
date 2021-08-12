import random as r
from itertools import permutations

def sample(iterable,n):
    """
    Obtains a random sample of any length from any iterable and returns it as a tuple
    Dependencies: random.randint(a,b)
    In: iterable, lengthOfDesiredSample
    Out: iterable of length(n)
    """
    import random as r
    iterable = tuple(iterable) if type(iterable)==type({0,1}) else iterable
    choiceIndices = tuple(r.randint(0,len(iterable)-1) for i in range(n))
    return tuple(iterable[i] for i in choiceIndices)
    
def sample2(iterable,n):
    return tuple(r.choice(iterable) for i in range(n))
    
if __name__ == '__main__':
    ctr = 0
    num = 0
    iterable = range(100)
    print(iterable)
    l = 2
    printed = []
    while 1:
        
        two = sample2(iterable,l)
        one = sample(iterable,l)
        if all([sum(one)==sum(two), one!=two, one!=two[::-1], not one in permutations(two,len(two)), not one in printed, not two in printed]):
            print(one,sum(one))
            print(two,sum(two))
            printed.append(one)
            printed.append(two)
            num += 1
        ctr += 1
        print(num/ctr)
        
    0.04717308697020733