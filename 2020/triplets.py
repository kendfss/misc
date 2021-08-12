#!/bin/python3

import math
import os
import random
import re
import sys


from itertools import permutations as combinations
from functools import lru_cache

# Complete the triplets function below.
@lru_cache(maxsize = 500)
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
        
def chords(iterable,length:int):
    from itertools import tee, islice
    t = tee(iterable,length)
    yield from zip(*(it if n==0 else islice(it,n,None) for n,it in enumerate(t)))

for i in chords(range(4),3):
    print(i)

def triplets(t, d):
    print(len(d))
    print(factorial(len(d))/(factorial(3)*factorial(len(d)-3)))
    orderly = lambda tup: all(tup[i]>tup[i-1] for i in range(1,len(tup)))
    indices = lambda tup: [d.index(i) for i in tup]
    enclosed = lambda tup,t: sum(tup)<=t
    countable = lambda tup: enclosed(tup) and orderly(tup)
    ctr = 0
    return sum(1 for i in filter(countable,combinations(d,3)) if all(j<t for j in i))
    # return sum((0,1)[countable(tup)] for tup in combinations(d,3))
            

if __name__ == '__main__':
    import os
    print(triplets(8,(1,4,2,6,3)))
    print()
    
    print(triplets(146,(72,30,9,78,49,23,58,7,73,44)))
    print()
    
    print(triplets(7,(3,1,2,4)))
    print()
    
    print(triplets(13041,(99,9505,3865,6357,1153,5228,8013,6716,7157,672,4438,9149,404,2188,7923,94,2196,4091,8981,979,6853,6501,8821,337,1272,13937408,3658,4303,5668,878,6579,8228,105,7544,6517,2612,7987,7826,9336,9530,3169,933,3512,278,8930,4536,4115,5335,9560,8549,903,4298,5485,2503,5001,298,8165,977,7722,1123,9267,9063,1967,9425,4492,8124,6752,3099,1566,6708,1745,7633,9451,6807,5249,3144,4440,7944,9814,8024,3042,9097,4666,1816,8635,4933,5629,1729,7709,3810,1669,2327,73,194,7801,4195,8840,1490,6882)))
    print()
        # 13041

    
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # d_count = int(input().strip())

    # d = []

    # for _ in range(d_count):
        # d_item = int(input().strip())
        # d.append(d_item)

    # res = triplets(t, d)

    # fptr.write(str(res) + '\n')

    # fptr.close()
