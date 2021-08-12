from typing import Iterable, Any
from m3ta import show, chords
from itertools import tee

def join(array:Iterable[Any]=None,sep:str='',head:str='',tail:str='') -> str:
    """
    Cast elements of an array to string and concatenate them.
    
    Examples:
        >>> show(
                map(
                    join, 
                    (range(i) for i in range(1,5))
                )
            )
        0
        01
        012
        0123
        
        # Also works as a decorator using keyword arguments
        >>> show(
            map(
                join(
                    sep = ', ', 
                    head = '[', 
                    tail = ']'
                ), 
                (range(i) for i in range(1,5))
            )
        )
        [0]
        [0, 1]
        [0, 1, 2]
        [0, 1, 2, 3]
    """
    if array:
        return head+sep.join(map(str,array))+tail
    else:
        def bind(array):
            array = map(str,array)
            return head+sep.join(array)+tail
        return bind


if __name__ == '__main__':
    n = 5
    show(map(join,(range(i) for i in range(1,n))))
    show(map(join(sep=', ',head='[',tail=']'),(range(i) for i in range(1,n))))
    show(map(join(sep=', ',head='[',tail=']'),(chords(range(n),i) for i in range(1,n))))
    
    x = tee(map(join(sep=', ',head='[',tail=']'),(chords(range(n),i) for i in range(1,n))))
    show(eval(i)[-1] for i in [*x[0]][::-1])
    show(eval(i)[-1] for i in [*x[1]])