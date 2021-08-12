import random

def benchmark(func, name=False):
    """
    A decorator for benchmarking functions
    
    taken from
    Mari Wahl, mari.wahl9@gmail.com
    University of New York at Stony Brook
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        delta = time.perf_counter()-t
        if name:
            print("\t%s" % func.__name__, delta)
        else:
            print(f"d={delta}")
        return res
    return wrapper

# @benchmark
def random_tree(n):
    temp = [n for n in range(n)]
    for i in range(n+1):
        temp[random.choice(temp)] = random.choice(temp)
    return temp

if __name__ == "__main__":
    for i in range(10):
        # random_tree(10000, i%2)
        print(i)
        benchmark(random_tree, i%2)(10000)
        print()