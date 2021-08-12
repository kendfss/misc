import site, os
from typing import Any

from moviepy.editor import VideoFileClip
from moviepy.audio.io.readers import FFMPEG_AudioReader as ar
import moviepy

site.addsitedir(r'E:\Projects\Monties\2020\operatingSystem')
import cabinet as fs
from m3ta import save, load, empty, nameSpacer, gather, show, module

def pop(arg:Any=None,silent:bool=False,file=False) -> str:
    """
    Open the folder containing a given module, or object's module
    Open's current working directory if no object is given
    Open the module's file if it is given
    Return the path which is opened
    """
    if arg:
        if isinstance(arg,module):
            path = arg.__file__
        else:
            mstr = arg.__module__
            if (top:=mstr.split('.')[0]) in globals().keys():
                m = eval(mstr)
            else:
                t = exec(f'import {top}')
                m = eval(mstr)
            path = m.__file__
        if not file:
            path = os.path.dirname(path)
    else:
        path = os.getcwd()
    if not silent:
        os.startfile(path)
    print(locals())
    return path

# pop(os)
# pop(ar,file=True)
# pop(print)
pop()
# print(ar.__module__)