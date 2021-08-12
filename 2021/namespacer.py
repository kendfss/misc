from dataclasses import dataclass
import os, pathlib
from sl4ng import show, pop


def namespacer0(path:str, sep:str='_', start:int=2) -> str:
    """
    Returns a unique version of a given string by appending an integer
    
    example:
        tree:
            /folder
                /file.ext
                /file_2.ext
        
        >>> namespacer('file', sep='-', start=2)
        file-2.ext
        >>> namespacer('file', sep='_', start=2)
        file_3.ext
        >>> namespacer('file', sep='_', start=0)
        file_0.ext
    """
    id = start
    oldPath = path[:]
    while os.path.exists(path):
        newPath = list(os.path.splitext(path))
        if sep in newPath[0]:
            if newPath[0].split(sep)[-1].isnumeric():
                # print('case1a')
                id = newPath[0].split(sep)[-1]
                newPath[0] = newPath[0].replace(f'{sep}{id}', f'{sep}{str(int(id)+1)}')
                path = ''.join(newPath)
            else:
                # print('case1b')
                newPath[0] += f'{sep}{id}'
                path = ''.join(newPath)
                id += 1
        else:
            # print('case2')
            newPath[0] += f'{sep}{id}'
            path = ''.join(newPath)
            id += 1
    return path



def namespacer1(path:str, index:int=2, format:str="{name}_{index}{ext}") -> str:
    weirdos = ".tar".split()

    folder, namext = os.path.split(path)
    name, ext = os.path.splitext(path)
    while any(name.endswith(weirdo:=w) for w in weirdos):
        if name != (name:=name.removesuffix(weirdo)):
            ext = weirdo + ext 
    new = os.path.join(folder, format.format(name=name, index=index, ext=ext))
    if os.path.exists(new):
        index = index + 1 if isinstance(index, int) else 2
        return namespacer1(path, index, format)
    return new


class NameSpacer:
    """
    Create an incrementation of a path if it already exists on the local system
    
    params
        format
            a formattable string amenable to both "name" and "index" key words
    
    examples
        >>> my_path = "c:/users"
        >>> NameSpacer()(my_path)
        c:/users_2
        >>> NameSpacer("{name} ({index})")(my_path)
        c:/users (2)
    """
    def __init__(self, format:str="{name}_{index}"):
        self.format = format
    def __call__(self, path:str, index:int=2) -> str:
        if os.path.exists(new:=self.new(path, index)):
            return self(path, index + 1)
        return new
    def new(self, path:str, index:int) -> str:
        weirdos = ".tar".split()
        name, ext = os.path.splitext(path)
        while any(name.endswith(weirdo:=w) for w in weirdos):
            if name != (name:=name.removesuffix(weirdo)): 
                ext = weirdo + ext
        return self.format.format(name=name, index=index)
namespacer = NameSpacer()






if __name__ == '__main__':
    examples = ('~'+'\n'+__file__+"\n"+os.path.dirname(__file__)+"\n"+r"""C:\Users\Kenneth\Downloads\imgui\SDL2-devel-2.0.14-mingw.tar.gz
C:\Users\Kenneth\Downloads\maths\cs\compilers\bison-3.7.6.tar.xz
e:/""").splitlines()
    show(map(os.path.splitext, examples))
    show(map(namespacer0, examples))
    show(map(namespacer1, examples))
    show(map(namespacer, examples))
    show(map(NameSpacer(), examples))
    show(map(NameSpacer("{name} ({index})"), examples))
    # print(namespacer(__file__))