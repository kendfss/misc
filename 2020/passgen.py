from collections import defaultdict
from m3ta import shuffle, load, save



gallery = load('generated.pkl') if os.path.exists('generated.pkl') else {}

def passgen(site=None,length:int=32,copy:bool=True) -> str:
    """
    Generate a GUID for different resources
    Dependencies: random,string,m3ta.shuffle
    In: format{length of the intervals of the guid you want}
    Out: str
    """
    import random,string,os
    import pyperclip
    used = load(gallery)
    punctors = ''.join(i for i in string.punctuation if not i in '{}[]\/|()')
    chars = ''.join(i for i in shuffle(string.ascii_uppercase + string.digits + string.ascii_lowercase + punctors))
    ranstr = ''.join([random.choice(chars) for i in range(length)])
    # [ranstr.insert(i+sum(format[:i+1]),sep) for i,j in enumerate(format[:-1])]
    pyperclip.copy(''.join(ranstr)) if copy else None
    return ''.join(ranstr)


t = passgen('facebook', copy=False)

print(t, len(t))