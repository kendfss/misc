from m3ta import show, xrange
from math import pi, e

def bant(x, stop=1, step=1, f=lambda x:x**x/x**.5):
    
    while stop>0:
        x = f(x)
        stop -= step
    return x
    
b = lambda x, stop=1, start=0, step=1, f=lambda x:x**x/x**.5, **kwargs: show((bant(x,stop-start-i*step,step,f) for i,v in enumerate(xrange(stop, start, step))), **kwargs)


if __name__=='__main__':
    b(pi, 10, 0, 1, enum=True)