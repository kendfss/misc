from itertools import cycle

def swap(itr,i1,i2):
    it = itr[:]
    a,b=it[i1],it[i2]
    it[i2] = a
    it[i1] = b
    return it

def steps(iterable):
    return [i for i,j in enumerate(iterable[1:],1) if j!=iterable[i-1]]
    
def moves(iterable):
    stps = steps(iterable)
    mvs = []
    for i in stps:
        mvs.append((i,i-1))
        mvs.append((i,i+1)) if i<len(iterable)-1 else None
    mvs = [swap(iterable,*mv) for mv in mvs]
    return mvs
    

def works(iterable,i1,i2):
    return steps(iterable[:]) > steps(swap(iterable[:],i1,i2))

def best(mvs):
    # moves = [swap(arr,step,step-1) for step in steps(arr)]
    # mvs = moves(arr)
    return mvs.index(min(mvs,key=lambda x: len(steps(x))))

def minMoves(arr):
    # Write your code here
    moves1 = 0
    moves2 = 0
    moves = 0
    if arr==sorted(arr) or arr==sorted(arr,reverse=True) or steps(arr)==0:
        return moves
    else:
        # for step in steps(arr):
            # if works(arr,step,step-1):
                # arr = swap(arr,step,step-1)
                # moves += 1
            # elif works(arr,step,step+1):
                # arr = swap(arr,step,step+1)
                # moves += 1
        while arr!=sorted(arr):
            mvs = moves(arr)
            step = steps(arr)[best(arr)]
            arr = swap(arr,step,step-1)
            moves += 1
    return moves
                


arr = [0,1,0,1]
arr = [0]
arr = [1, 1, 1, 1, 0, 0, 0, 0]
arr = [1, 1, 1, 1, 0, 1, 0, 1]

print(steps(arr))
# for step in steps(arr):
    # print(swap(arr,step,step-1))
    # print(steps(swap(arr,step,step-1)))
    # print()
print(minMoves(arr))
# print(best(arr))