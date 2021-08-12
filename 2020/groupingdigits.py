#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from itertools import cycle

def swap(it,i1,i2):
    a,b=it[i1],it[i2]
    it[i2] = a
    it[i1] = b
    return it

def minMoves(arr):
    # Write your code here
    moves1 = 0
    moves2 = 0
    if arr==sorted(arr) or sorted(arr,reverse=True):
        return moves1
    else:
        clone = arr[:]
        loop = cycle(range(len(arr)))
        i = next(loop)
        while clone!=sorted(arr):
            # for i,element in enumerate(arr):
            # for i in range(1,len(arr)):
                if clone[i]>clone[i-1]:
                    moves1 += 1
                    clone[i] = 0
                    clone[i+1] = 1
                i = next(loop)
        clone = arr[:]
        loop = cycle(range(len(arr))[::-1])
        i = next(loop)
        while clone!=sorted(arr,reverse=True):
            # for i,element in enumerate(arr):
            # for i in range(1,len(arr)):
                if clone[i]>clone[i+1]:
                    moves2 += 1
                    clone[i] = 0
                    clone[i-1] = 1
                i = next(loop)
        
    return min(moves1,moves2)

if __name__ == '__main__':