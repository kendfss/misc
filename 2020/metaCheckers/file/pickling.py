from m3ta import alphabet

def save(obj,filename):
    """
    Pickles the given object to a file with the given path/name
    """
    import pickle
    with open(filename,'wb') as fob:
        pickle.dump(obj,fob,protocol=pickle.HIGHEST_PROTOCOL)

def load(filename):
    """"""
    import pickle
    with open(filename,'rb') as fob:
        var = pickle.load(fob)
    return var

if __name__ == '__main__':
    f = r'c:\users\kenneth\downloads\tst.pkl'
    save(tuple(i for i in alphabet),f)
    y = load(f)
    print(y)
    for i in y:
        print(i)