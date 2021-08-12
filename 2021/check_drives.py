"""
https://stackoverflow.com/questions/4188326/in-python-how-do-i-check-if-a-drive-exists-w-o-throwing-an-error-for-removable
"""

import ctypes
import itertools
import os
import string
import platform

from sl4ng import show

letters = 'abcdefghijklmnopqrstuvwxyz'

def compress(data, selectors):
    for d, s in zip(data, selectors):
        if s:
            yield d

def get_available_drives():
    if 'Windows' not in platform.system():
        return []
    drive_bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    return list(itertools.compress(string.ascii_uppercase,
               map(lambda x:ord(x) - ord('0'), bin(drive_bitmask)[:1:-1])))

# get_available_drives()

import platform,os
def hasdrive(letter):
    return "Windows" in platform.system() and os.system("vol %s: 2>nul>nul" % (letter)) == 0


def does_drive_exist(letter):
    import win32file
    return (win32file.GetLogicalDrives() >> (ord(letter.upper()) - 65) & 1) != 0

def getinfo(drive):
    import win32api
    return win32api.GetVolumeInformation("C:\\")