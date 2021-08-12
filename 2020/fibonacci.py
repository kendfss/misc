def fib(n:int) -> int:
    fibs = [0,1]
    if n in fibs:
        return fibs.index(n)
    else:
        while n:
            fibs.append(fibs[-1]+fibs[-2])
            n -= 1
    return fibs[-1]
        
def str2ba(string:str) -> str:
    return bytearray(ord(i) for i in string)
if __name__ == '__main__':
    # print(fib(0))
    # print(fib(1))
    for i in range(100):
        print(f'{i}\n\t{fib(i)}')
        print(f"\t{' '.join(j for j in str(fib(i)))}")
        print(f"\t{str2ba(chr(i).join(j for j in str(fib(i))))}")
    print(f"{str2ba(' '.join(str(fib(i)) for i in range(10)))}")