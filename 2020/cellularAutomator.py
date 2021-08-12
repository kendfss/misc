class Origin:
    def __init__(self, form):
        self.start = form
        self.history = {'branches':{},'transformations':{}}

class Rule:
    def __init__(self, rule):
        self.rule = rule
    
    def __repr__(self):
        rep = "{\n"
        for key,val in self.rule.items():
            rep += f'    {key}: {val},\n'
        rep += '}'
        return rep
    
    def branches(self, origin):
        org = Origin(origin)
        cacheLen = len(org.history['branches'].items())
        org.history['branches'][cacheLen+1] = tuple(origin[:].replace(key,val) for key,val in self.rule.items())
        # return tuple(origin[:].replace(key,val) for key,val in self.rule.items())
        return org.history['branches'][cacheLen+1]
    
    def transform(self, origin):
        # if all([key not in self.rule.values() for key in self.rule.keys()]) and 
        # if all([len(key)==1 for key in self.rule.keys()]):
        observations = self.rule.keys()
        outcomes = self.rule.values()
        terminus = ""
        for term in origin:
            terminus += term if term not in self.rule.keys() else self.rule[term]
        # else:
            # terminus = 'Null'
        return terminus
    
    def generate(self, origin, end, start=0):
        cache = [(origin,)]
        pind = 0
        for i in range(end):
            # print(i)
            parent = cache[-1]
            children = []
            print(f'p{pind}:', parent)
            ind = 0
            for branch in parent:
                print(f'b{ind}p{pind}:', branch)
                children.append(self.apply(branch))
                ind += 1
            print('c:',children)
            cache.append(children[0])
            pind += 1
        return cache[start:]

def strands(iterable, length=1):
    # if length == 0: return None
    # else:
        # for i in range(length,len(iterable)+1):
            # yield iterable[i-length:i]
    return ''.join(iterable[i-length:i] for i in range(length, len(iterable)+1))
    
def merge(iterable, out=''):
    iter2 = [iterable[0]]
    for j in iterable[1:]:
        i = iterable.index(j)
        if j[0] == iterable[i-1][-1]:
            iter2.append(j[1:])
        else: 
            iter2.append(j)
    return ''.join(iter2)


def chopper(iter1, iter2, iter3, out=''):
    """
    Given a string s1 and two others s2 and s3, return a new string s4 wherein all occurences of s2 in s1 have been replaced with s3
    """
    # for i in range(1,len(iterable)):
        # chop = iterable
        # print(i,iterable[::i])
    if iter2 in iter1:
        subs = list(strands(iter1,len(iter2)))
        print(subs, iter2)
        for sub in subs:
            if sub==iter2: subs[subs.index(sub)] = iter3
        # return link(subs)
        return ''.join(merge(subs))
    else: return None
    
    
if __name__ == '__main__':
    from time import perf_counter_ns as time
    from random import randint
    from itertools import permutations, chain
    from sl4ng import sample, freq
    
    bases = 'atcg'
    basePairs = {
        'a':'t',
        't':'a',
        'c':'g',
        'g':'c'
    }
    
    strandom = lambda x: sample(bases,randint(1,x))
    # z = Rule({'a':'A','b':'a'})
    # print(z,z.generate('0',10),sep='\n',end='\n\n')
    # t = 'abcde'
    t = "".join(strandom(10))
    z = Rule(basePairs)
    
    print(
        t,
        z.branches(t),
        z.transform(t[:]),
        strands(t,2),
        merge(strands(t,2)),
        # transform(z,t[:]),
        # z.transform(t) in z.branches(t),
        sep='\n',end='\n\n'
    )
    
    def test(detail):
        # T = lambda x: ("".join(i) for i in chain.from_iterable(permutations(bases,j) for j in range(2,1+x)))
        T = lambda x: ("".join(i) for i in permutations(bases,x))
        for i in range(1,detail):
            x = time()
            check = (z.transform(t) in z.branches(t) for t in T(10**i))
            y = time()-x
            yield any(check),y
    # for j in test(10): print(j)