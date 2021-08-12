"""
How to find missing number in a string of numbers with no separator in python?
    https://stackoverflow.com/questions/64289404/how-to-find-missing-num..
        Parse a string of digits into integers, check if it has any incomplete sequences of consecutive integers, fill in the blanks
        
Cannot work if the first integer is longer than a third of the sequence length
"""

from m3ta import factors,powerset,chords
from itertools import combinations,chain,product,combinations_with_replacement as cwr

examples = {
    89101113:12,
    9899101102:100,
    596597598600601602:599,
    909192939495969798100101:99,
    11111211311411511:-1,
    11111311511:[112,114],
    1234567812345680:12345679
}
t = str(list(examples.keys())[0])
# def split(string,sizes):
    # if not len(string)%sizes:
        # return [string]
def split(sequence, x):
    return sequence[:x], sequence[x:]

def parse(digits,most=None):
    """
    Try to parse "digits" into numbers, and find the missing one.

    The numbers will have no more than six digits.
    Return -1 if "digits" isn't parseable or isn't missing one.

    >>> parse("89101113")  # 8, 9, 10, (12), 13
    12
    >>> parse("9899101102")  # 98, 99, (100), 101, 102
    100
    >>> parse("596597598600601602")  # 596, 597, 598, (599), 600, 601, 602
    599
    >>> parse("909192939495969798100101")  # 90, ...
    99
    >>> parse("11111211311411511")  # Looks like "111, ..." but isn't
    -1
    """
    for n in range(1, most if most else len(digits)+1):
        expected, remainder = split(digits, n)
        # print(expected)
        failures = []
        while len(failures) <= 1 and remainder:
            expected = str(int(expected) + 1)
            actual, remainder = split(remainder, len(expected))
            if actual != expected:
                failures.append(expected)
                remainder = actual + remainder  # Re-parse
        if len(failures) == 1:
            return int(failures[0])
    return 0

# for k,v in examples.items():
    # print(k,v,parse(str(k)),sep='\n\t')
    
first = lambda long, n: int(str(long)[:n])
def parse(long,max=None):
    strong = str(long)
    for i in range(1,maximum if maximum else len(strong)+1):
        start = first(strong,i)
        rest = strong[i:]
        while rest.startswith(str(start+1)):
            start = start + 1

def freshers(alpha:int,n:int,extend:bool=False) -> int:
    r = range(alpha,alpha+n) if extend else range(alpha,n)
    return sum((r[0]+i)*10**(len(q)-sum(len(str(k)) for k in r[i::-1])) for i,j in enumerate(r))
    
def mine(alpha:int,n:int,extend:bool=False) -> int:
    r = range(alpha,alpha+n) if extend else range(alpha,n)
    return sum((r[0]+i)*10**(sum(len(str(k)) for k in r[:i])) for i,j in enumerate(r))

bind = lambda array,sep='':sep.join(str(i) for i in array)
if __name__ == '__main__':
    pen = lambda a,n: 1 if n==0 else a**a**pen(a,n-1)
    fail = lambda a,n: 1 if n==0 else a**a**a**pen(a,n-1)
    long = fail(2,2)
    strong = str(long)
    digits = set(int(i) for i in set(strong))
    # for i in range(6,len(strong)+1):
        # if (val:=parse(strong,i)):
            # print(i,val,sep='\n\t')
        # else: print(i)
    # for i in range(10):
        # print(first(long,i))
    
    a,n = (6,120)
    
    r:range = range(1,5)
    r = range(a,n)
    q = ''.join(str(o) for o in r[::-1])
    # print(r)
    # a,n = (6,6)
    print(q)
    # print(sum((r[0]+i)*10**(sum(len(str(k)) for k in r[:i])) for i,j in enumerate(r))==int(q))
    print(mine(a,n)==int(q))
    print(mine(a,n))
    print(mine(a,n,True)==int(q))
    print(mine(a,n,True))
    print()
    q = ''.join(str(i) for i in r)
    print(q)
    # print(sum((r[0]+i)*10**(len(q)-sum(len(str(k)) for k in r[i::-1])) for i,j in enumerate(r))==int(q))
    print(freshers(a,n)==int(q))
    print(freshers(a,n))
    print(freshers(a,n,True)==int(q))
    print(freshers(a,n,True))
    x = 10**243
    # print(x)
    print(f'{freshers(a,n,True):.100000000000}')
    pass
    
