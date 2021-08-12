"""
def div(arg1,arg2):
    return true if all b in arg2 divide all a in arg1 else false
    
div({a1,...,aN}:=A,b) -> div(sum(A),b) for all nonzero aN,b:
    there exists A2:={a21/b,...,a2N/b} if div(A,b) such that A = {b*i for i in A2}
    let c = sum(A)
    there exists some a2N for which not div(sum{b*i for i in A2},b): # if not div(c,b)
        so b would not divide itself since: # valid iff b==0
            there would exist some aN which does not divide by b 
                so there would be some An which would not equal itself
    
    also a direct consequence of distributivity of addition
    
    
    
"""
from m3ta import gcd

div = lambda a,b: a%b==0

def check(n):
    r = range(1,n)
    s = sum(r)
    d = gcd(*r)
    if not div(s,d):
        print()
        