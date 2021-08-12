"""
https://stackoverflow.com/questions/66250184/python-real-and-imaginary-how-to-print-2-2i

class comp:
  
    def __init__(self, real, imag):
        self.real=real
        self.imag=imag

    def add(self,other):
        print('Sum of the two Complex numbers :{}+{}i'.format(self.real+other.real,self.imag+other.imag))
    
    def sub(self, other):
        print('Subtraction of the two Complex numbers :{}+{}i'.format(self.real-other.real, self.imag-other.imag))
"""



class comp(complex):
    def add(self, other):
        print(f'Sum of the two Complex numbers: {self+other}')
    def sub(self, other):
        print(f'Subtraction of the two Complex numbers: {self-other}')


x = comp(1, 2)
y = comp(3, 4)
x.add(y)
# Sum of the two Complex numbers: (4+6j)
x.sub(y)
# Subtraction of the two Complex numbers: (-2-2j)


def sign(x):
   return '+' if x>=0 else ''

class comp:
  
    def __init__(self, real, imag):
        self.real=real
        self.imag=imag

    def add(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        print(f'Sum of the two Complex numbers: {r}{sign(i)}{i}i')
    
    def sub(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        print(f'Subtraction of the two Complex numbers: {r}{sign(i)}{i}i')


x = comp(1, 2)
y = comp(3, 4)
x.add(y)
# Sum of the two Complex numbers: 4+6i
x.sub(y)
# Subtraction of the two Complex numbers: -2-2i