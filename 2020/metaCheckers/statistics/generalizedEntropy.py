from math import log
from m3ta import alphabet as abc, sigma, freq, mean, shannonEntropy as shan

letters = ''.join(i for i in abc if i.isalpha() or i==' ')
digits = ''.join(i for i in abc if i.isnumeric() or i=='.' or i=='-')

print(abc,"".join(letters),"".join(digits),sep='\n',end='\n\n')
lorem = r"E:\IDEs\Microsoft Visual Studio 2019\DesignTools\SampleData\pt-BR\Data\LoremIpsum.txt"

prob = lambda x,y: freq(x,y)/len(y)

def ent(inpt):
    weights = {i: prob(i,inpt) for i in set(inpt)}
    return -sigma(weights[i]*log(weights[i],2) for i in weights.keys())


def entropy(inpt,base=2,mode='kbdUS',alphabet=None):
    """
    Computes a modal entropy for a given iterable. Ints and floats will be converted to strings. Comma format ints will raise errors.
    Dependencies: m3ta.(sigma, freq, alphabet)
    Arguments: inpt -> iterable, base->int(2 - default), mode->str(kbdUS(),abc,num,shan), alphabet=iterable(None = default)
    Output: float
    """
    prob = lambda x,y: freq(x,y)/len(y)
    iterable = not any([type(inpt)==type(0),type(inpt)==type(1.2)])
    
    if mode=="kbdUS":
        inpt = str(inpt) if not iterable else tuple(str(i) for i in inpt)
        chars = abc if alphabet==None else abc
        weights = {i:prob(i,chars) for i in set(inpt)}
        return -sigma(val*log(val,base) for val in weights.values())
        
    elif mode=='abc':
        inpt = str(inpt) if not iterable else tuple(str(i) for i in inpt)
        chars = letters if alphabet==None else abc
        weights = {i:prob(i,chars) for i in set(inpt)}
        return -sigma(val*log(val,base) for val in weights.values())
    
    elif mode=='num':
        inpt = str(inpt) if not iterable else tuple(str(i) for i in inpt)
        chars = digits if alphabet==None else abc
        weights = {i:prob(i,chars) for i in set(inpt)}
        return -sigma(val*log(val,base) for val in weights.values())
        
    elif mode=='shan':
        inpt = str(inpt) if not iterable else inpt
        chars = tuple(i for i in inpt)
        weights = {i:prob(i,chars) for i in set(inpt)}
        return -sigma(val*log(val,base) for val in weights.values())
    
    elif mode == "ascii":
        pass
        
    elif mode == 'utf-8':
        pass
    
with open(lorem,'r') as f:
    txt = f.readlines()[0]
    txt2 = list(i for i in txt)
    # print(txt, len(txt.split()), len(set(txt)), shan(txt), ent(txt), entropy(txt), entropy(set(txt)), sep='\n', end='\n\n')
    q = 123
    # print(entropy(q),entropy(q,mode='shan')-shan(str(q)))
    # print(len(txt)==len(txt2))
    print(txt,txt2)
    for q in range(len(txt)):
        print(
            entropy(txt[:q],mode='shan')==shan(str(txt[:q])),
            entropy(txt2[:q],mode='shan')==shan(txt2[:q])
        )
        # print(q,entropy(q,mode='shan')-shan(str(q)))