"""
Inspection of the behaviour of the int function's base conversion feature for naturals in bases upto 10

int(str(integer),base) will read the given string as an integer in the given base and report its value in base 10
    int(str(1),2) -> 1
    int(str(12),3) -> 5
    int(str(123),4) -> 27
    int(str(1234),5) -> 194 - 4*5**0 + 3*5**1 + 2*5**2 + 1*5**3
    int(str(12345),6) -> 5+24+(3*36)
    
"""
# def ib(value,base):
    # """
    # Generalized version of the int function's base converter
    # Dependencies
    # Arguments
    # int(str(integer),base) will read the given string as an integer in the given base and report its value in base 10
        # int(str(1),2) -> 1
        # int(str(12),3) -> 5
        # int(str(123),4) -> 27
        # int(str(1234),5) -> 194 - 4*5**0 + 3*5**1 + 2*5**2 + 1*5**3
        # int(str(12345),6) -> 5+24+(3*36)
        
    # Unfortunately, python's interpreter will only return the index of the first occurence of an element in an iterable so the following one liner is obsolete
        # return sigma(int(i)*base**(str(value)[::-1].index(i)) for i in str(value)[::-1])
    # """
    # val = str(value)
    # r = 0
    # i = 0
    # for v in val:
        # r += int(v)*base**(len(val)-1-i)
        # i += 1
    # return r
def ib(value,base):
    """
    interpet an integer as a number of a given base and return its corresponding value in base 10
    Dependencies: m3ta.sigma
    In: value:int,base:int
    Out: int
    """
    if all(int(i)<base for i in str(value)):
        return sigma(int(i)*base**(j) for j,i in enumerate(str(value)[::-1]))
    else:
        raise ValueError(f"invalid literal for int() with base {base}: {value}")

ib2 = lambda value, base: int(str(value),base)

trials = lambda x: tuple(None if ib(i,x+1)==ib2(i,x+1) else (i,ib(i,x+1),ib2(i,x+1)) for i in range(x))
fails = lambda x: tuple(i for i in trials(x) if i != None)

flops = lambda x: len(fails(x))/len(trials(x))

def test(top):
    from itertools import product, chain
    from m3ta import alphabet
    
    x = 0
    y = 0
    for i in range(2,36):
        for j in range(i):
            uno = f1(j,i)
            dos = f2(j,i)
            booly = uno==dos
            
            y += 1 if not booly else 0
            print(f"{round(100*y/x)}%","int({},{}): {} ... {}".format(j,i,uno,dos), sep='\n',end='\n\n') if not booly else None
            print()
            x += 1
    

import random, math
from itertools import chain

import matplotlib.pyplot as plt, pyperclip as pc

from m3ta import freq

def bq(value,depth):
    result = 1
    peak = max(set(int(i) for i in str(value))) + 1
    for i in range(peak,peak+depth): 
        if i > 36: break
        else:
            result /= int(f"{value}",base=i)
    return 1/result


minBase = lambda x: 1 + max(set(int(i) for i in str(x)))
maxDepth = lambda x: 37 - minBase(x)

    
def bq2(value,depth):
    base = minBase(value)
    peak = base + depth - 1
    assert peak < 37, (f"Current peak is {peak} but maxium base is 36. Please reduce depth by some integer greater than {depth-maxDepth(value)} but smaller than {peak - 1}.")
    result = 1
    while depth > 0:
        result /= int(f"{value}",base=base)
        base += 1
        depth -= 1
    return 1/result
# print(bq2(357,37))


def exp(inpt):
    """
    Computes iterations of BQ2 to the maximum viable depth of the given integer. Also returns the natural log of each value
    """
    q = str(inpt)
    val = int(q,base=minBase(int(q))) 
       
    x = tuple(i for i in range(maxDepth(val)))
    y = tuple((bq2(val,i)) for i in x)
    z = tuple(math.log(i) for i in y)
    return (x,y,z)


"""
Next:
Sort integers into depth clases and compare plot evolution
"""
class Depth:
    def __init__(self,depth):
        self.depth = depth
    def finite(self,end,start=0):
        for i in range(end):
            if maxDepth(i) == self.depth:
                yield i
    def infinite(self):
        x = 0
        while True:
            if maxDepth(x) == self.depth: yield x
            else: x += 1
            
print("depth checking...")
for j in range(1,100): print(j, minBase(j), maxDepth(j), min(maxDepth(i) for i in range(j)))
print(min(maxDepth(i) for i in range(1000)))
print("depth checked\n\n")
# for i in Depth(24).infinite(): print(i)

                
def depthClass(n,mode='f'):
    """
    Produces the sequence of naturals whose depth class is equivalent to n
    If mode is set to 
    """

"""
val = 357
print(val, maxDepth(val))
fig, axs = plt.subplots(2,1)
matrix = exp(val)
axs[0].plot(matrix[0],matrix[1]); axs[0].set_title(f"BQ({val},{maxDepth(val)})")
axs[1].plot(matrix[0],matrix[2]); axs[1].set_title(f"Corresponding logarithms")
fig.show()

plt.plot(exp(val)[0],exp(val)[2])
plt.plot(exp(val)[0],exp(val)[1])
plt.title("BQ Function")
plt.show()
"""



def seed(inpt):
    last = 0
    while last != inpt:
        yield inpt
        n = inpt
        inpt = int(str(inpt),base=minBase(inpt))
        last = n



print(f"seed(457)")
for i in seed(457): print(i)
# for i in range(11,100):
    # print(i,len(list(seed(i))),end='\n\n')



id = lambda x: x
def retrieveMaximii(itr,f=seed):
    m = max(len(set(f(i))) for i in itr)
    cache = []
    for i in set(itr):
        if len(set(f(i))) >= m:
            cache.append((i, len(set(f(i)))))
    return tuple(cache)

s = [i for i in range(10,100)]
# rm = retrieveMaximii(s,seed)
# print(rm)
# for i in rm: print(len(list(seed(i))))
# s = lambda x: tuple(i for i in range(1+(10**x), ))
# print("\nalskdjd"*20)
print(s)
s = lambda x: tuple(i for i in range(10**(x),10**(x+1)))
print(s(1))
# for i in range(3): print(s(i))

ss = lambda x: [tuple(i for i in range(10**(j-1),10**j)) for j in range(2,x+2)]
maximalPodLocations = lambda x,y: (i for i in ss(y))
# for i in ss(4): print(retrieveMaximii(i),len(i),'\n\n')
print(len(ss(4)))
# rms = ((i,len(list(seed(i)))) for i in (retrieveMaximii(tup,seed) for tup in ss(4)))
# rms = lambda x: [(i,len(list(seed(i)))) for i in retrieveMaximii(j) for j in s (for s in ss(x))]

# ss = (max(j) for j in rms)
# for i in rms(2): print(i)