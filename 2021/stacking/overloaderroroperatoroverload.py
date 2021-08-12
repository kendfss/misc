"""
https://stackoverflow.com/questions/66261319/memory-error-when-using-overloaded-addition-operator-in-python
"""
import numpy as np

class P1:
    def __init__(self):
        self.data = np.zeros((512,512),dtype='float64')
    def __setitem__(self, key, value):
        self.data[key] = value
    def __getitem__(self, item):
        return self.data[item]
    
    def __add__(self, other):
        return self.data + other.data
    
    def __radd__(self, other):
        # return other.data + self.data
        return other + self.data


p1 = P1()
p2 = P1()
print(p1 + p2)