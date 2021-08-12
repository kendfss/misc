import os, re, sys
from sl4ng import show, trim, multisplit, namespacer

forbiddens = r'\/:?*<>|"'

def likefile(path:str) -> bool:
    """
    Check if a path string looks like a file or not
    """
    path = normalize(path)
    return bool(re.search('readme$|.+\.(\S)+$', path.split(os.sep)[-1], re.I))

def hasdirs(path:str) -> bool:
    """
    check if a path string contains directories or not
    """
    return bool(re.search(re.escape(os.sep), normalize(path)))

def hasdrive(path:str) -> bool:
    """
    Check if the path has an explicit drive
    """

def normalize(path:str, force:bool=False) -> str:
    """
    Standardize a path for a current operating system.
    Given an equivalently structured file/project system, this should make code reusable across platforms 
    params
        force
            If true, all forbidden characters will be replaced with an empty string
    relative
    """
    other = ''.join(i for i in '\/' if not i==os.sep)
    if force:
        if sys.platform == 'win32':
            forbiddens
        new = ''.join(i for i in path if not i in forbiddens)
    else:
        new = path[:]
    if other in path:
        terms = []
        for term in path.split(os.sep):
            if other in term:
                for part in term.split(other):
                    terms.append(part)
            else:
                terms.append(term)
        new = os.path.join(*terms)
    return new


if __name__ == '__main__':
    __all__ = "trim normalize hasdirs likefile multisplit namespacer".split()
    # __all__ = [eval(i) for i in __all__]
    # show
    # from sl4ng import trim
    # show(__all__)
    # show(map(exec, __all__[2:]))
    mock = 'drive: users user place subplace file.extension.secondextension'.split()
    # mock = 'drive: users user place subplace readme'.split()
    testPaths = [
        ''.join(mock),
        os.path.join(*mock),
        os.path.join(*mock[:4])+'/'+'/'.join(mock[4:]),
        os.path.join(*mock[3:4])+'/'+'/'.join(mock[4:]),
        os.path.join(*mock[:-1]),
        '/'.join(mock),
        '/'.join(mock),
        '/'.join(mock[:4])+'/'+'/'.join(mock[4:]),
        '/'.join(mock[3:4])+'/'+'/'.join(mock[4:]),
        '/'.join(mock[:-1]),
        '/'.join(mock[:-1]),
        mock[-1],
        './'+mock[-1]
    ]
    # tests = [eval(f'{f}(r"{p}")') for f in __all__ for p in testPaths]
    # tests = [eval(f'{f}(r"{p}")\n\t{f}\n\t{p}') for f in __all__ for p in testPaths]
    # tests = [((f'{f}(r"{p}")'), f, p) for f in __all__ for p in testPaths]
    # tests = [(f(f'(r"{p}")'), f, p) for f in __all__ for p in testPaths]
    # show(tests)
    # show(normalize(p, 0) for p in testPaths)
    # show(normalize(p, 1) for p in testPaths)
    show(map(os.path.realpath, testPaths))
    show(map(os.path.normpath, testPaths))
    # show(zip(testPaths, map(normalize, testPaths)))
    # show(zip(testPaths, map(likefile, map(normalize, testPaths))))
    # for 