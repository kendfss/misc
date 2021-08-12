from itertools import tee, product, zip_longest
from m3ta import regurge, main, join, show, clock



def products(*args, repeat=2):
    print(f"{eval('args') = }")
    # print(eval('args[0]'))
    # print(eval('args[1]'))
    
    if (la:=len(args)) == 1:
        iterable = args[0]
        elements = [f'e{i}' for i in range(repeat)]
        iterables = [f'for {element} in regurge(iterable)' for element in elements]
        # iterables = [f'for {element} in regurge(iterable)' for element in elements]
    elif la > 1:
        # print(eval('args'))
        # print(eval('args[0]'))
        # print(eval('args[1]'))
        # iterables = [f'for e{i} in args[{i}]' for i, arg in enumerate(args)]
        # print(iterables)
        # print([exec(s.split()[-1]) for s in iterables])
        print(*zip(*sorted(args, key=len)))
        return products(zip(*args), repeat=repeat)
    else:
        raise ValueError("Argument has no elements")
    parts = join(elements, sep=', ', head='eval("(', tail=')")'), join(iterables, sep=' ')
    cmd = join(parts, ' ', head='(', tail=')')
    # print(eval('args'))
    # print(eval('args[0]'))
    # print(eval('args[1]'))
    print(f"{cmd = }")
    return eval(cmd)
    
    


if eval(main):
    iterable = 'ab'
    # show(product(iterable, repeat=3))
    # show(products(iterable, repeat=3))
    show(product(iterable,'c', repeat=3))
    show(products(iterable,'c', repeat=3))
    # for i in range(10):
        # wrap
        # clock(products