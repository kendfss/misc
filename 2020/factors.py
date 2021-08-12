from m3ta import factors as v1, pipe, beeper, sample, freq
from time import perf_counter as ctr
from statistics import fmean as mean
from itertools import combinations,chain

def eratosthenes(n):
    interval = range(2,n)
    marked = set()
    for i in interval:
        if i not in marked:
            multiples = {j for j in interval if j%i==0 and j>i}
            marked.update(multiples)
            yield i

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
def ishighlycomposite(n):
    return all(len(list(factors(i)))<len(list(factors(n))) for i in range(n))

factors = v2
def comdivs(*args):
    if len(args) == 1 and hasattr(args[0],'__iter__'):
        args = tuple(args[0])
    if all(isinstance(i,int) or i==int(i) for i in args):
        # facsets = [k for k in (j for j in (v2(i) for i in args))]
        facs = []
        for i in args:
            for j in factors(i):
                facs.append(j)
        elements = set(i for i in facs if freq(i,facs)==len(args))
        print(facs)
        print(elements)
        
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
    # for i in range(50):
        # print(f'{i}:\n\t{sorted(v1(i))}\n\t{sorted(list(v2(i)))}\n\t{sorted(list(v3(i)))}')
        # print(f'{i}:\n\t{list(v3(i))}\n\t{len(list(v3(i)))}')#\n\t{ishighlycomposite(i)}')
        # if ishighlycomposite(i) and 0<i%6 and 0<i%4:
            # print(f'{i}:\n\t{list(factors(i))}\n\t{len(list(factors(i)))}\n\t{ishighlycomposite(i)}')
    r = 5000
    l = sample(range(10),3)
    print(comdivs(*l))
    # for i in range(3):
        # bigtest(r)
    
    # beeper(8)
    # beeper(8)
    # beeper(8)