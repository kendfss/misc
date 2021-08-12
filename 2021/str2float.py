"""
https://github.com/Dangerxfh/codeArmy_issue
"""
from functools import reduce

from sl4ng import show

def _str_2_float(s):
    return  reduce(lambda x,y: x+y/(10**len(str(y))),map(int,s.split(".")))
print(_str_2_float("123.999")+0.001)



def san(num):

    level=[1]
    indexLevel = [];
    for i in range(0,num):
        for j in range(1,len(level)):
            indexLevel[j]=level[j]+level[j-1]
        indexLevel.append(1)
        print(indexLevel)
        level=indexLevel.copy()
san(8)

def san2(num):
    level = [1]
    for i in range(num):
        yield level
        level = [i + j for i, j in zip([0, *level], [*level, 0])]

show(san2(8))