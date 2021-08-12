"""
https://stackoverflow.com/questions/66245075/get-all-values-from-dictionary-including-the-values-from-a-dictionary-inside-a

For example, if there is a dictionary like the one below, I want a function `get_dict_values()` such that

```
dic = {1:"1", 2:"2", 3:{"a":"a", "b":"b"}, 4:"4"}

print(get_dict_values(dic))

>>> ["1","2","a","b","4"]
```
"""
from itertools import _tee
from typing import Iterable
from sl4ng import generator


# def flat(iterable, dict_keys=False):
    # if isinstance(iterable, dict):
        # itr = iterable.keys() if dict_keys else iterable.values()
        # for val in itr:
            # yield from flat(val, dict_keys)
    # elif isinstance(iterable, (list, tuple)):
       # for val in iterable:
          # yield from flat(val)
    # else:
         # yield iterable
 
def flat(iterable:Iterable, dict_keys:bool=False, strings:bool=False) -> generator:
    """
    Create a completely flat version of an iterable.
    params:
        strings
            yield each character from each string if set to true
        dict_keys
            yield the keys instead of the values if set to true
    """
    if isinstance(iterable, str):
        yield from iterable if strings else [iterable]
    elif isinstance(iterable, dict):
        itr = iterable.keys() if dict_keys else iterable.values()
        for val in itr:
            yield from flat(val, dict_keys, strings)
    elif isinstance(iterable, (list, tuple)):
       for val in iterable:
          yield from flat(val, dict_keys, strings)
    elif hasattr(iterable, '__iter__'):
        yield from iterable
    else:
         yield iterable


if __name__ == '__main__':
    TEST_CASE = {
        1: "1",
        2: "2",
        3: {
            "a": "a",
            "b": "b",
            "c": dict(enumerate('eieio')),
        },
        4: {
            0: 1,
            1: {
                0: 'this',
                1: {
                    0: 'one',
                    1: {
                        0: 'goes',
                        1: {
                            0: 'deeper',
                            1: 'than deep'.split(),
                            }
                    }
                }
            },
        }
    }
    
    print(list(flat(TEST_CASE)))
    print(list(flat(TEST_CASE, 0, 1)))
    print(list(flat(TEST_CASE, 1, 0)))
    print(list(flat(TEST_CASE, 1, 1)))