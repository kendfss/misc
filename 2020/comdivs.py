from m3ta import factors as v1, pipe, beeper, sample, freq, factors
from time import perf_counter as ctr
from statistics import fmean as mean
from itertools import combinations, chain

def eratosthenes(n):
    interval = range(2,n)
    marked = set()
    for i in interval:
        if i not in marked:
            multiples = {j for j in interval if j%i==0 and j>i}
            marked.update(multiples)
            yield i

def v1(n):
    """Returns the set of multiplicative factos of an input integer
    Dependencies: N/A
    In: Integer
    Out: Set"""
    if n == 0:
        return {1}
    elif n == 1:
        return {1}
    else:
        facts = [1,n]
        for i in range(2,int(n/2)+1):
            if n % i == 0:
                facts.append(i)
                facts.append(n/i)
        fctrs = set(sorted(list(int(i) for i in facts))) # remove diplicates
        return fctrs

def v2(n):
    val = round(n/2)
    yielded = set()
    if n > 0:
        yield n
    while val:
        # if val in yielded or n/val in yielded:
            # break
        if n%val==0:
            yield val
            # yield int(n/val)
            yielded.add(val)
            # yielded.add(int(n/val))
        val -= 1
# def v3(n):
    # val = round(n/2)
    # yielded = set()
    # if n > 0:
        # yield n 
        # yielded.add(n)
        # if n != 1:
            # yield 1 
            # yielded.add(1)
    # while val:
        ### if val in yielded or int(n/val) in yielded:
        ###     break
        # if n%val == 0:
            # if not val in yielded:
                # yield val 
                # yielded.add(val)
            # if not int(n/val) in yielded:
                # yield int(n/val) 
                # yielded.add(int(n/val))
        # val -= 1
def v3(n):
    primes = tuple(eratosthenes(n))
    facts = {n,1} if n!= 0 else {}
    for p in primes:
        if n%p==0:
            e = 1
            while n%p**e==0:
                facts.add(p**e)
                e += 1
    if facts == {n,1}:
        yield from facts
    else:
        for numbers in chain.from_iterable(combinations(facts,r) for r in range(1,len(facts))):
            if n%pipe(numbers)==0:
                facts.add(pipe(numbers))
        yield from facts        
def ishighlycomposite(n,start=0):
    # factors = v3
    selflen = len(list(factors(n)))
    # rax = [list(factors(i)) for i in range(start,n+1)]
    return all(len(list(factors(i)))<selflen for i in range(start,n))
    # return len(max(rax,key=len))==selflen

factors0 = v3
def comdivs(*args):
    if len(args) == 1 and hasattr(args[0],'__iter__'):
        args = tuple(args[0])
    if all(isinstance(i,int) or i==int(i) for i in args):
        # facsets = [k for k in (j for j in (v2(i) for i in args))]
        facs = []
        for i in args:
            for j in factors0(i):
                facs.append(j)
        for i in facs:
            if freq(i,facs)==len(args):
                yield i
        # elements = set(i for i in facs if freq(i,facs)==len(args))
        # print(facs)
        # print(elements)
        
def integerFunctionTest(trials,*functions,start=1):
    results = {f'v{i}':[] for i,f in enumerate(functions,1)}
    # while trials-start:
    for i in range(start,start+trials):
        # print(f'\t{trials-start}')
        for i,func in enumerate(functions,1):
            t = ctr()
            func(start)
            results[f'v{i}'].append(ctr()-t)
        start += 1
    for k in results:
        results[k] = mean(results[k])
    return results
    
def bigtest(r):
    res = {
        f'v{i}':[]\
        for i,f in enumerate(range(3),1) 
    }
    
    for j in range(r):
        # print(r-j)
        for k,v in integerFunctionTest(r,v1,v2,v3,start=r).items():
            res[k].append(v)
    print()
    print()
    print()
    for k,v in res.items():
        print(f'{k}:\t{mean(v)}')
if __name__ == '__main__':
    # comdivs(2336,2497)
    # print(list(factors(10)))
    for i in range(5045):
        # print(f'{i}:\n\t{sorted(v1(i))}\n\t{sorted(list(v2(i)))}\n\t{sorted(list(v3(i)))}')
        # print(f'{i}:\n\t{list(v3(i))}\n\t{len(list(v3(i)))}')#\n\t{ishighlycomposite(i)}')
        # if ishighlycomposite(i,i-1) and 0<i%6 and 0<i%4:
            # print(f'{i}:\n\t{list(factors(i))}\n\t{len(list(factors(i)))}\n\t{ishighlycomposite(i)}')
        if ishighlycomposite(i):
            print(f'{i}:\n\t{list(factors(i))}\n\t{len(list(factors(i)))}\n\t{ishighlycomposite(i)}')
    r = 5000
    l = sample(range(2,30,2),4)
    print(l)
    # print(set(comdivs(*l)))
    print(set(comdivs(4)))
    # for i in range(3):
        # bigtest(r)
    
    # beeper(8)
    # beeper(8)
    # beeper(8)