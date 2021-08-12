"""
Attempt at Michael Penn's "How large can a subset be???" combinatorics video
"""

from itertools import combinations, chain

from m3ta import show


# print(1988/4)
def basic(cardinality, exclusions):
    bag = range(1, cardinality+1)
    result = [*bag]
    print(all(i in bag for i in result))
    print(all(i in result for i in bag))
    for a, b in combinations(bag, 2):
        if (b-a) in exclusions:
            result.remove(b) if b in result else None
    return(result)
    
    
x = basic(1989, (4,7))
x = basic(11, (4,7))
show(x)
print(len(x))


def solution(cardinality, exclusions):
    bag = range(1, cardinality+1)
    compatibles = {
        exclusion: [(a,b) for a,b in combinations(bag, 2) if b-a == exclusion]
        for exclusion in exclusions
    }
    incompatibles = {
        exclusion: [(a,b) for a,b in combinations(bag, 2) if b-a == exclusion]
        for exclusion in exclusions
    }
    # print(len(com))
    show(map(len, (compatibles, incompatibles)))
    # while any(b-a in exclusions for a,b in abs(com))
    
x = solution(1989, (4,7))
x = solution(7, (4,7))
# print(solution)