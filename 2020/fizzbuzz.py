#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for n in range(1,n+1):
        moduli = mod3,mod5 = (n%3,n%5)
        gte3,gte5 = (n>=3,n>=5)
        greater = gte3
        if greater and not any(moduli):
            print('FizzBuzz')
        elif gte5 and not mod5:
            print('Buzz')
        elif gte3 and not mod3:
            print('Fizz')
        else:
            print(n)
    
    # for n in range(1,n+1):
    #     if n<3:
    #         print(n)
    #     elif not n%3:
    #         if not n%5:
    #             print('FizzBuzz')
    #         else:
    #             print('Fizz')
    #     elif not n%5:
    #         print('Buzz')
    #     else:
    #         print(n)
            

        
if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)
    # for i in range(1,16):print(i);fizzBuzz(i)
    # for i in range(1,16):
    #     fizzBuzz(i)
