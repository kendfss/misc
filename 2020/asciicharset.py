def ascii(omissions:str='',include:bool=False) -> str:
    """
    Return the ascii character base excluding the given omissions:
        "p" ->  ' ' + punctuation
        "u" ->  uppercase
        "l" ->  lowercase
        "d" ->  digits
    Feel free to omit combinations:
        ascii('lup')
            0123456789
    """
    import string
    d = {
        "p":" "+string.punctuation,
        "u":string.ascii_uppercase,
        "l":string.ascii_lowercase,
        "d":string.digits,
    }
    return "".join(d[k] for k in d if k in omissions) if include else "".join(d[k] for k in d if not k in omissions)
    # return ''.join(chain(d[k] for k in d if not k in omissions)) == "".join(d[k] for k in d if not k in omissions)
    
    
if __name__ == '__main__':
    # for i in ascii():
        # print(i)
    from itertools import combinations,chain
    options = 'puld'
    for comb in chain(*(combinations(options,r) for r in range(len(options)))):
        comb = ''.join(comb)
        print(f'{comb}\n\t{ascii(comb)}')
        
    # print(ascii())
    
    from m3ta import kbd 
    print(help(kbd) == help(ascii))