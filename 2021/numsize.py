from sys import getsizeof
from sl4ng import show, freq


def size(x):
    return getsizeof(x)
def sizes(m):
    for i in range(m):
        yield getsizeof(10**i)

def spm(m):
    return freq(getsizeof(10**m), sizes(m))
# for i in range(100): print(f'{i}:\t{getsizeof(2*10**i)}')
for i in range(100): print(spm(i))
