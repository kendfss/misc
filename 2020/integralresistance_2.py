from math import e,pi
import decimal
decimal.getcontext().prec = 200
  
def res(val):
    n = 1
    # val = decimal.Decimal(val)
    # while val**n!=int(val**n):
    while not (val**n).is_integer():
        # print(f'{n}\t{x**n:.100}')
        n += 1
    return n
def rseries(root,length,base=10):
    return (res(root+(base**-i)) for i in range(length))

if __name__ == '__main__':
    if 0:
        x = 1.01
        r = res(x)
        print(r)
        print(x**r)

    if 0:
        x = 1
        for i in range(20):
            d = 10**-i
            r = res(x+d)
            print(f'{i}\n\t{d = }\n\t{r = }')
    if 0:
        for i,(j,k) in enumerate(zip(rseries(1,20),rseries(2,20))):
            print(f'{i}\n\t{j}\n\t{k}')
    
    else:
        r = pi
        l = 10
        b = 2
        # for i in r:
            # print(i)
        print(res(r))
        print(r**res(r))
        for i,j in enumerate(rseries(r,l,b)):
            d = b**-i
            v = r+d
            k = v**j
            print(f'{i}\n\t{j = }\n\t{d = }\n\t{v = }\n\t{k = }')