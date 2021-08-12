'''
Short mathematical concept sketches
Policies:
    Numbers will not be regarded as sets, only as elements of sets
    The 0th order mass of a set is the sum of its elements, 
        the 1st is the sum of the mass of each of its elements, 
        and so on accordingly. The total is the sum of all masses
    The ordinary volume is the same
    If it is to exist at all, the empty set is the only self containing set whose mass and volume are finite.
        - Asking if "the set of all sets which don't contain themselves contains itself" is akin to asking if the "number of numbers is a number". 
            It's farce. No, it doesn't/isn't because it isn't even what it's alleged to be.
        - True because even if all sets contain an empty set, the effect of removing that set has no cardinal implication. 
            In this sense, the empty set is also the only set which contains it's self... Moreso it is not a set but a lack thereof.
    Because the empty set is not a set, the cardinality, C, of all sets discussed here shall be of size 1<=C<C(N).

    The force on a set is the density by the fourth power of the cube-root of the volume over the square of the change in cardinality with

'''

# import c
from itertools import combinations, chain, permutations

powerset = lambda self: chain.from_iterable(combinations(self,r) for r in range(1,1+len(self)))
triangular = lambda n: n*(n+1)/2
cardinum = lambda n: Mset(i for i in range(1,1+n))
cardinum = lambda length,shift=1: Mset(range(shift,shift+length))
frequency = lambda x,X: len(tuple(i for i in X if i==x))

class Mset:
    def __init__(self,*args):
        self.last = -1
        if len(args)==1:
            if hasattr((arg:= args[0]),'__iter__'):
                self.elements = [i for i in arg]
            else:
                self.elements = [i for i in arg]
        else:
            self.elements = list(args)
    def __add__(self,other):
        if any(isinstance(other,t) for t in (int,float,complex)) and self.isNumeric():
            for i,n in enumerate(self):
                self[i] = n + other
        elif hasattr(other,'__iter__'):
            for o in other:
                self.append(o)
        else:
            raise ValueError(f'"{type(other)}" does not support this operation')
    def __sub__(self,other):
        if any(isinstance(other,t) for t in (int,float,complex)) and self.isnumeric():
            for i,n in enumerate(self):
                self[i] = n - other
        elif hasattr(other,'__iter__'):
            for o in other:
                if o in self:
                    self.append(o)
        else:
            raise ValueError(f'"{type(other)}" does not support this operation')
    def __pow__(self,order):
        assert isinstance(order,int), "Please use an integer"
        return Mset(permutations(self,order))
    def __eq__(self,other):
        return sorted(self)==sorted(other)
    def __repr__(self):
        return str(self.elements)
    def __str__(self):
        return str(self.elements)
    def __iter__(self):
        return self
    def __next__(self):
        if self.last < len(self.elements)-1:
            self.last += 1
            return self.elements[self.last]
        else:
            self.last = -1
            raise StopIteration
    def __len__(self):
        return len(self.elements)
    def __getitem__(self,value):
        return self.elements[value]
    isNumeric = lambda self: all(any(isinstance(elem,t) for t in (int,float,complex)) for elem in self)
    # isMono = lambda self: True if isNumeric(self) or 
    # def isTypical(self):
    def isFlat(self):
        if self.isNumeric():
            return True
        elif all(hasattr(elem,'__iter__') for elem in self):
            l0 = len(self[0])
            t0 = type(self[0])
            return all(all((len(elem)==l0,type(elem)==t0)) for elem in self)
        elif not any(hasattr(elem,'__iter__') for elem in self):
            t0 = type(self[0])
            return all(type(elem)==t0 for elem in self)
    def append(self,elem):
        self.elements.append(elem)
    def update(self,elems):
        for i in elems:
            self.append(i)
    def expectation(self):
        return sum(j*frequency(j,self.elements)/len(self) for j in self.elements)
    mean = lambda self: self.mass()/len(self)
    index = lambda self,elem: None if elem not in self.elements else self.elements.index(elem)
    def remove(self,elem):
        if elem not in self.elements:
            raise ValueError(f'{elem} is not a member of {self.elements}')
        else:
            del self.elements[self.elements.index(elem)]
    def delete(self,elem):
        if elem not in self.elements:
            raise ValueError(f'{elem} is not a member of {self.elements}')
        else:
            while elem in self.elements:
                self.remove(elem)
    def indices(self,elem):
        if elem not in self.elements: return None
        clone = self.elements[:]
        indices = []
        while elem in clone:
            position = clone.index(elem)
            indices.append(position)
            clone.remove(elem)
        return indices
        
    def sort(self):
        self.elements = sorted(self.elements)
        return self
    def powerset(self):
        return chain.from_iterable(combinations(self,r) for r in range(1,1+len(self.elements)))
    def deltize(self):
        arg = (self.elements[i]-self.elements[i-1] for i in range(1,len(self.elements)))
        return Mset(arg)
    def quotize(self):
        arg = ((self.elements[i]/i)-(self.elements[i-1]/(i-1)) for i in range(1,len(self.elements)))
        return Mset(arg)
    def sigmize(self,constant=0):
        arg = [(constant,self.elements[1]-self.elements[0]),]
        for i in range(1,len(self.elements)):
            constant += i
            arg.append((constant,self.elements[i]-self.elements[i-1]))
        arg = (i[0]*i[1] for i in arg)
        return Mset(arg)
    def pitize(self,constant=1):
        arg = [(constant,self.elements[1]-self.elements[0]),]
        for i in range(1,len(self.elements)):
            constant *= i
            arg.append((constant,self.elements[i]-self.elements[i-1]))
        arg = (i[0]+i[1] for i in arg)
        return Mset(arg)
    def mass(self):
        # assert order<self.depth(), "Please choose an order lower than the set's current depth ({self.depth()})"
        return sum(self.elements)
    def volume(self):
        if any(isinstance(elem,str) for elem in self) and not all:
            return None
        return sum(len(i) for i in self.elements if hasattr(i,'__iter__') and not isinstance(i,str))
    def density(self):
        if self.volume()!=0:
            return self.mass()/self.volume()
        else:
            None
class Map:
    def __init__(self,domain,function):
        self.domain = Mset(domain)
        self.function = function# if not is instance(function,str) else eval(f'fu')
        self.codomain = Mset(function(elem) for elem in domain)
        # self.entirety = 
    def fidelity(self):
        c,t,d,e = (0 for i in range(4))
        continuous = len([i for i in self.domain if i in self.codomain])
        discontinuous = len([i for i in self.domain if not i in self.codomain])
        emergent = len([i for i in self.codomain if i in self.domain])
        total = sum(continuous,emergent,discontinuous)
        table = {
            'c':continouous,
            'd':discontinuous,
            'e':emergent,
            't':total,
            'continuity':continouous/total,
            'discontinuity':discontinuous/total,
            'emergence':emergent/total,
            
        }
        return table
                
    # def continuity(self):
        # pass

'All elements of a set make equipotent contributions to the mass of the powerset'
def prominenceDistribution(cardinality):
    self = cardinum(cardinality)
    ps = powerset(self)
    return {elem: sum((frequency(elem,s) for s in ps) for elem in self)}
    
# print(prominenceDistribution(5))
# n = 0
# while True:
#   if (meanPD:=sum(prominenceDistribution(

if __name__ == '__main__':
    import math as m
    import numpy as np
    # t = Mset(1,2,3,4,5,6,7,8)
    sin = lambda x: [m.sin(i) for i in x]
    t = Mset(sin(np.linspace(0,2*np.pi,200)))
    zero = list((1,2,3,4,5))
    a = Mset(1,2,3,4,1,1,4)
    # a = Mset(zero)
    b = Mset([i for i in a])
    # a = Mset(zero)
    # b = 
    print(f"{a = }")
    print(f"{b = }")
    print(f"{a.sort() = }")
    print(f"{sorted(b) = }")
    print(f"{a==b = }")
    print(f"{a.expectation() = }")
    print(f"{b.expectation() = }")
    print(f'{a.mean() = }')
    print(f'{b.mean() = }')
    print(f"{b[1] = }")
    print(f'{cardinum(5,6) = }')
    # t = Mset(1,2,3,4)
    # print(t,t.last)
    # for i in t: print(i)
    # print([(i,i in t) for i in t.elements], 'bool')
    # print('bool2',[any(x is e or x == e for e in t) for x in t.elements])
    # print(f"{t.index(5)=}")
    # print(t.deltize(),t.quotize())
    # print(t.sigmize(),t.pitize())
    # print(f"{t.mass()=}\n{t.deltize().mass()=}")
    # print(f"{t.volume()=}")
    # print(t.density())
    print([] in [1,2,3])