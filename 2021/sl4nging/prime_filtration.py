from statistics import fmean as mean, median, mode, stdev
from itertools import filterfalse
from sl4ng import show, factors, regenerator, clock, eratosthenes, pop, imap, unzip, eq

#@clock
def old(n):
    return n in eratosthenes(n+1)
    
#@clock
def isprime(n:int) -> bool:
    """
    Confirm that an integer has no factors other than 1 and itself
    """
    if n < 2:
        return False
    tried = []
    for i in range(2, int(n/2)+1):
        if any(not i%j for j in tried):
            continue
        else:
            tried.append(i) if i > 1 else None
            if not n%i:
                return False
    return True
    
def comparables(trials, every=False):
    func = map if every else filter
    dom = range(trials)
    # return zip(filter(old, dom), filter(isprime, dom))
    return zip(func(old, dom), func(isprime, dom))
    
def agreetest(trials):
    return all(map(eq, comparables(trials, True)))
    # return all(map(eq, comparables(trials, False)))
    

def timetest(trials:'int>2'):
    dom = range(trials)
    comps = zip(map(old, dom), map(isprime, dom))
    # show(comps)
    diffs = regenerator(y-x for x,y in comps)
    # mean = sum(diffs)/sum(1 for i in diffs)
    # median = sum(diffs)/sum(1 for i in diffs)
    # mode
    return imap(diffs, mean, mode, median, stdev)
    # return "mean:\t{}\nmode:\t{}\nmedian:\t{}\nstdev:\t{}".format(*results)

def batchtest(trials):
    results = regenerator(map(mean, unzip(map(timetest, range(2, trials+1)))))
    print("mean:\t%s\nmode:\t%s\nmedian:\t%s\nstdev:\t%s" % tuple(results))
    return results

# def analyze(results):
    # report
if __name__ == '__main__':
    print('testing')
    n = 3000
    # batchtest(n)
    # show(comparables(n, 1),0,1)
    show(filterfalse(eq, comparables(n)),0,1)
    print(agreetest(n))
    
    # results = map(mean, unzip(map(timetest, range(2, n+1))))
    # print("mean:\t%s\nmode:\t%s\nmedian:\t%s\nstdev:\t%s" % tuple(results))
    # r = regenerator(filter(old, range(n)))
    # r = regenerator(filter(isprime, range(n)))
    # r = regenerator(range(n))
    # show(r)
    # print(all(map(old, r)))
    # show(map(old, r))
    # show('%s:\t%s\n\t%s' % (i, isprime(i), [*factors(i)]) for i in r)
    # show('%s:\t%s\n\t%s' % (i, isprime(i), i%2) for i in r)
    # show('%s:\t%s' % (i, isprime(i)) for i in r)