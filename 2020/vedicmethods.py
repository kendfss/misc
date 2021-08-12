# from typing import Iterable
from functools import reduce


def commonmagnitude(*args:float) -> int:
    magnitude = len(str(max(args,key=lambda n: len(str(n).split('.')[0]))).split('.')[0])
    base = int('1'+('0'*(magnitude)))
    # diffs = tuple(base-i for i in args)
    return base
    
def baselaw(a,b):
    base = commonmagnitude(a,b)
    diffs = tuple(i-base for i in (a,b))
    adb = base+diffs[1]
    bda = base+diffs[0]
    fa = adb*reduce(lambda x,y:x*y,diffs)
    fb = bda*reduce(lambda x,y:x*y,diffs)
    print(base,diffs,fa,fb,sep='\n')
    
    
n = 9
m = 9
print(baselaw(n,m),n*m)


from m3ta import convert
help(convert)
convert(r'F:\Samples\Miscellaneous Samples\1HrThunderstorm.ogg.ogv','mp3')