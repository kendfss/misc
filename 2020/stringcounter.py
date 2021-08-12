from random import choice, randint
import csv, os, string

def freq(element,iterable) -> int:
    return sum(1 for i in iterable if i==element)

def sample(sequence,length):
    '''
    Just for "generating" test strings
    breaks if the sequence does not have a __len__ attribute
    '''
    for i in range(length):
        yield choice(sequence)

def ascii(omissions:str='',include:bool=False) -> str:
    """
    A convenient ascii character set
        Return an ascii character set excluding the given omissions:
            "p" ->  ' ' + punctuation
            "u" ->  uppercase
            "l" ->  lowercase
            "d" ->  digits
    Feel free to omit combinations:
        >>> ascii('lup')
        ...     0123456789
    or include them
        >>> ascii('d',True)
        ...     0123456789
    """
    d = {
        "p":" "+string.punctuation,
        "u":string.ascii_uppercase,
        "l":string.ascii_lowercase,
        "d":string.digits,
    }
    return "".join(d[k] for k in d if k in omissions) if include else "".join(d[k] for k in d if not k in omissions)

def weights(string,omissions='',include=False):
    # return {i:freq(i,string) for i in set(string)} ## if you only want to measure elements of the string
    return {i:freq(i,string) for i in ascii(omissions,include)}

heaviest = lambda string: max(string,key=weights(string).get)

if __name__ == '__main__':
    s = 'abcda'
    print(s,heaviest(s),sep='\n\t') # 'a'

    strings = [''.join(sample(ascii('l',True)[:4],randint(3,5))) for i in range(4)]
        
        

    for s in strings:
        path = s+'.csv'
        with open(path, "w", newline="") as ECA:
            writer = csv.writer(ECA)
            writer.writerows(weights(s,'l',True).items())
        os.startfile(path)