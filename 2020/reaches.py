from itertools import combinations,permutations

from m3ta import factorial,sgm,sigma

sort = lambda iterable,k=None: sorted(list(iterable),key=k)
tract = lambda a,b: a-b

ladders = lambda n,k=2: combinations(range(n),k)
reaches = lambda n,k=2: {sum(i) for i in ladders(n,k)}

# difference between successive peak reaches 
peakdiff = lambda n,k=2: max(reaches(n,k))-max(reaches(n-1,k))
# the difference between the last elements of peaks varies with the length of the ladder
linearity = lambda r=100,k=2: len({peakdiff(i,k) for i in range(k+1,r)})==1 
# differential==1 everywhere
continuity = lambda iterable: all(i in iterable for i in range(min(iterable),max(iterable))) and all(i in range(min(iterable),max(iterable)+1) for i in iterable)

