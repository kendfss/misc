from math import atan,atan2

class comp:
    def __init__(self,real=0,imaginary=0):
        self.re = real
        self.im = imaginary
    @property
    def val(self):
        return [self.re,self.im]
    @property
    def modulus(self):
        return sum(i*i for i in self.val)
    @property
    def phase(self):
        if self.x>0 or self.y!=0:
            return atan(self.y/((self.x**2+self.y**2)**(1/2)+self.x))
        elif x<0 and y==0:
            return pi
        elif x==y==0:
            return None
        else:
            raise ValueError('Argument is undefinable wrt Wikipedia')
    @property
    def phase(self):
        return atan2(*self.val[::-1])
    @property
    def x(self):
        return self.re
    @property
    def y(self):
        return self.im
    @property
    def trig(self):
        return self.phase,self.modulus
    
    argument = phase
    arg = phase
    
    mod = modulus
    magnitude = modulus
    mag = modulus
    
    
    def __repr__(self):
        rep = ''
        for i in self:
            rep += str(i)+(', ','j')[i==self.y]
        
        # return str((self.x,str(self.y)+'j'))
        return rep
    def __int__(self):
        return int(self.re)
    def __next__(self):
        if not hasattr(self,'_ind'):
            self._ind = -1
        if self._ind < len(self.val)-1:
            self._ind += 1
            return self.val[self._ind]
        else:
            del self._ind
            raise StopIteration
    def __iter__(self):
        return self
        
    def __add__(self,other):
        if any(isinstance(other,t) or issubclass(type(other),t) for t in (int,float)):
            self.re += other
        elif isinstance(other,complex) or issubclass(type(other),complex):
            self.re += other.real
            self.im += other.imag
        else:
            self.im += other.im
            self.re += other.re
        return self
    def __pow__(self,other):
        if any(isinstance(other,t) or issubclass(type(other),t) for t in (int,float)):
            self.re **= other
        elif isinstance(other,complex) or issubclass(type(other),complex):
            self.re **= other.real
            self.im **= other.imag
        return self

    # def __new__(self,other):
        # if any(isinstance(other,t) or issubclass(type(other),t) for t in (int,float)):
            # new = comp(real=other,imaginary=0)
        # elif isinstance(other,complex) or issubclass(type(other),complex):
            # new = comp(real=other.real,imaginary=other.imag)
        # return self    


if __name__ == '__main__':
    pass