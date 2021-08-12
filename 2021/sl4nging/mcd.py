from typing import Iterable
import os

from sl4ng import pop, getsource, show, main, namespacer, flat



def mcd(*args:Iterable[str], overwrite:bool=False, go_back:bool=False, recursive:bool=True) -> str:
    """
    Start a project by creating all the directories you think you'll need ahead of time
    
    go_back:
        if set to True, the process will return to the starting directory
    recursive:
        if set to false, all directories will be created in the starting directory
    overwrite:
        if set to True, a 
    eg
        each of the following calls create the following tree:
            dir-1
                dir0: starting directory
                    dir1
                        dir2
                        dir3
                    dir4
            dir5
        
        >>> mcd('dir1 dir2 .. dir3 .. .. dir4 .. .. dir5'.split())
        >>> mcd('dir1/dir2 ../dir3 ../../dir4 ../../dir5'.split())
    """
    home = os.getcwd()
    for arg in flat(args):
        arg = namespacer(arg) if arg!='..' and not overwrite else arg
        os.makedirs(arg, exist_ok=True)
        os.chdir(arg) if recursive else None
    last_stop = home if go_back else os.getcwd()
    os.chdir(last_stop)
    return last_stop


if eval(main):
    pass
    # pop(mcd('fuck/fuckitty ../fuck fuck ../fuck'.split(), go_back=1))
    # pop(mcd('dir1 dir2 .. dir3 .. .. dir4'.split(), go_back=1))
    # pop(mcd('dir1 dir2 .. dir3 .. .. dir4 .. .. dir5'.split()))
    # pop(mcd('dir1/dir2 ../dir3 ../../dir4 ../../dir5'.split(), go_back=True))