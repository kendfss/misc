from typing import Iterable, Sequence, Any, List
from m3ta import generator, show, walks, main, regurge
from itertools import tee, chain


def cast(x,y,base=None):
    # Transform any flat array into an YxX matrix (y lists of length x)
    base = base if base else tuple(range(x*y))
    assert x*y==len(list(tee(base)[0])), f"base={base} does not cast to {(x,y)}"
    return [base[slice(i*x,x+i*x)] for i in range(y)]

def unzip(iterable:Iterable[Sequence[Any]]) -> List[list]:
    """
    Obtain the inverse of a zip of a collection of arrays
    This is about the same as a clockwise rotation of a matrix by 90 degrees
    This will omit empty arrays
    examples
        >>> m3ta.show(unzip(range(3) for i in range(3)))
        [0, 0, 0]
        [1, 1, 1]
        [2, 2, 2]
        
        
        >>> m3ta.show(unzip(range(j) for j in range(10)))
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        [1, 1, 1, 1, 1, 1, 1, 1]
        [2, 2, 2, 2, 2, 2, 2]
        [3, 3, 3, 3, 3, 3]
        [4, 4, 4, 4, 4]
        [5, 5, 5, 5]
        [6, 6, 6]
        [7, 7]
        [8]
        
        
    """
    consumable = regurge(iterable)
    str_escape = lambda string: string.replace("'", "\'")
    length = 0
    racks = []
    for i in consumable:
        for j, k in enumerate(i):
            if j > length-1:
                exec(f"x{j} = []")
                racks.append(eval(f'x{j}'))
                length += 1
            app_elem = f"x{j}.append('{str_escape(k)}')" if isinstance(k, str) else f"x{j}.append({k})"
            eval(app_elem)
    return racks




if eval(main):
    for i in range(10):
        print(f"Trial #{i}")
        s, x = tee(zip([*range(j)] for j in range(1,10)))
        s, x = tee([*range(j)] for j in range(i))
        print("X")
        show(s,tail=None)
        y = unzip(x)
        print("Y")
        show(y,tail=None) if y else None
        print(len(y)) if y else None
        print('\n\n\n\n'+'.'*50)
    s, x = tee(zip(range(3), map(chr, range(3,6)), range(3,6), map(chr, range(6,9))))
    # s, x = tee(zip(range(3), map(chr, range(1,14))))
    # s, x = tee(map(chr, range(3)))
    # s, x = tee(range(3) for i in range(3))
    show(s)
    y = unzip(x)
    show(y)