from functools import lru_cache as lch
from time import perf_counter as pc

@lch(maxsize=2000)
def fact1(n):
    """
    Uses ordinary recursion
    """
    if n==0:
        return 1
    elif n>0:
        return n*fact1(n)
    else:
        return -factorial(abs(n))
        
@lch(maxsize=2000)
def fact2(n):
    """
    Uses tail recursion ala Graham Hutton @ Computerphile
    """
    go = lambda target,accumulator=1 :accumulator if target==0 else go(target-1,accumulator*target)
    return go(n)


def factorial(n:int) -> int:
    """
    Return n! for any integer
    Dependencies: lru_cache(from functools)
    In: (int)
    Out: int
    """
    if n>=0:
        k = 1
        while n:
            k *= n
            n -= 1
        return k
    else:
        return -factorial(abs(n))
    

if __name__ == '__main__':
    
    for i in range(10):print(f'{i}\t{fact(i)}')
    for i in range(10):print(f'{i}\t{factorial(i)}')
    n = 1
    while n:
        print(len(str(n)))
        n=factorial(n+1)
        
    t = pc()
    for i in range(n):fact(i)
    print(t-pc())
    
    
    
    pass