import os
from pyperclip import copy
from m3ta import show, freq


file = r'c:\users\kenneth\pipfreeze.txt'
module = lambda i: i.split('==' if '==' in i else '@')[0].strip()
version = lambda i: (i.split('==')[1] if '==' in i else '').strip()

def lines(file):
    with open(file,'r') as fob:
        return [i.strip() for i in fob.readlines()]
def modules(linez):
    return [module(i) for i in linez]
    
def roots(lines):
    mods = modules(lines)
    worthy = lambda i: freq('.',i)==0 and freq(i,mods)==1 and not any(j in i for j in [k for k in mods if i!=k])
    return [i for i in mods if worthy(i)], [i for i in mods if not worthy(i)]
    # worthy = lambda i: module(i) == 'tensorflow' or not 'tensorflow' in module(i)
    
def parseVersions(file):
    lns = lines(file)
    mods = modules(lns)
    viables, unviables = roots(lns)
    parsed = {
        module(i): version(i)
        for i in lns
            if module(i) in viables
    }
    return parsed
    
def reformat(file):
    modules = parseVersions(file)
    string = ''
    for k,v in modules.items():
        string += '=='.join((k,v)) if bool(v) else k
        string += '\n'
    return string
    
def dump(file,newname='pipsweets.txt'):
    source = os.path.dirname(file)
    new = os.path.join(source,newname)
    with open(new,'w') as fob:
        fob.write(reformat(file))
    return new


if __name__ == '__main__':
    # print(modules(file))
    # show(lines(file))
    # print(parseVersions(file))
    # os.startfile(file)

    # for k,v in parseVersions(file).items():
        # print(f'{k}:\t{v}')
    # print(reformat(file))
    # show(roots(file)[0])
    # show(roots(file)[1])
    # print(len(roots(file)[0]))
    # print(len(roots(file)[1]))

    # print(reformat(file))
    lns = lines(file)
    show(roots(lns)[0])
    show(roots(lns)[1])
    new = dump(file)
    # os.startfile(new)
    print(new)
    # copy(' '.join(roots(lns)[0]))
    