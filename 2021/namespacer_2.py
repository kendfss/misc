import os, re


def namespacer(path, sig="_{}"):
    start = start if not isinstance(start, type(None)) else 2
    name, ext = os.path.splitext(path)
    if start == None:
        pat = sig.replace('{}', '\d+') + "$"
        if re.search(pat, name):
    while os.path.exists(path):
        if 