import re, os, subprocess, itertools


def compare(pair,mode=None,):
    mode = 'r' if mode == None \
        else 'rb' if mode == 'bytes' \
        else 'l' if mode == 'lines' \
        else 'r' if mode == 'read' \
        else None
    if mode is None: raise ValueError(f'{mode=} is not valid. Use "bytes", "lines", "read"')
    lines = mode=='l'
    form = {
        'r':'part',
        'rb':'byte',
        'l':'line',
    }[mode]
    mode = 'r' if lines is True else mode
    report = []
    name1 = os.path.split(pair[0])[1]
    name2 = os.path.split(pair[1])[1]
    with open(pair[0],mode) as one:
        with open(pair[1],mode) as two:
            booly = tuple(part in two for part in one) if lines is False else tuple(line in two.readlines() for line in one.readlines())
            filty = tuple(filter(bool,booly))
            q = len(filty)/len(booly)
            report.append((True,f'"{name2}" contains every {form} from "{name1}"')) if q==1 \
                else report.append((False, f'"{name2}" contains no {form}s from "{name1}"')) if q == 0 \
                else report.append((False, f'"{name2}" contains most {form}s from "{name1}"')) if q>=1/2 \
                else report.append((False, f'"{name2}" contains some {form}s from "{name1}"'))
    # print(report)
    return report[0]
    
def check(files,mode=None):
    modes = 'read,bytes,lines'.split(',')
    pairs = tuple(itertools.permutations(files,2))
    reports = {}
    if mode is None:
        for file in files:
            name = os.path.split(file)[1]
            relevantPairs = (pair for pair in pairs if pair[0]==file)
            reports[name] = [compare(pair,mode) for pair in relevantPairs for mode in modes]
            booly = tuple(val[0] for val in reports[name])
            announcement = True if all(booly) else name+'\n\t'+"\n\t".join([i[1] for i in reports[name]])
            reports[name] = announcement
    else:
        for file in files:
            name = os.path.split(file)[1]
            relevantPairs = (pair for pair in pairs if pair[0]==file)
            reports[name] = [compare(pair,mode) for pair in relevantPairs]
            booly = tuple(val[0] for val in reports[name])
            announcement = True if all(booly) else name+'\n\t'+"\n\t".join([i[1] for i in reports[name]])
            reports[name] = announcement
    report = "\n".join(reports[key] for key in reports)
    return report

def deltas(pair,mode=None):
    _mode = mode
    mode = 'r' if mode == None \
        else 'rb' if mode == 'bytes' \
        else 'l' if mode == 'lines' \
        else 'r' if mode == 'read' \
        else None
    if mode is None: raise ValueError(f'{mode=} is not valid. Use "bytes", "lines", "read"')
    lines = mode=='l'
    form = {
        'r':'part',
        'rb':'byte',
        'l':'line',
    }[mode]
    mode = 'r' if lines is True else mode
    report = []
    name1 = os.path.split(pair[0])[1]
    name2 = os.path.split(pair[1])[1]
    with open(pair[0],mode) as one:
        with open(pair[1],mode) as two:
            fails = tuple(tuple(one).index(part) for part in one if part not in two) if lines is False \
                else tuple(one.readlines().index(line) for line in one.readlines() if line not in two.readlines())
            print(fails)
            return (None,compare(pair,_mode)[1]) if len(fails)>0 else (False,'\t'+"\t".join(fails))

def check2(files,mode=None):
    modes = 'read,bytes,lines'.split(',')
    if mode not in [None]+modes: raise ValueError(f'{mode=} is not valid. Use "bytes", "lines", "read", or none')
    pairs = tuple(itertools.permutations(files,2))
    reports = {}
    if mode is None:
        for file in files:
            name = os.path.split(file)[1]
            relevantPairs = (pair for pair in pairs if pair[0]==file)
            reports[name] = [deltas(pair,mode) for pair in relevantPairs for mode in modes]
            print(reports[name])
            booly = tuple(True for val in reports[name] if val[0] is None)
            announcement = None if len(booly)==len(reports[name]) else name+'\n\t'+"\n\t".join([i[1] for i in reports[name]])
            reports[name] = announcement
    else:
        for file in files:
            name = os.path.split(file)[1]
            relevantPairs = (pair for pair in pairs if pair[0]==file)
            reports[name] = [deltas(pair,mode) for pair in relevantPairs]
            booly = tuple(True for val in reports[name] if val[0] is None)
            announcement = None if len(booly)==len(reports[name]) else name+'\n\t'+"\n\t".join([i[1] for i in reports[name]])
            reports[name] = announcement
    report = "\n".join(reports[key] for key in reports)
    return report
            
if __name__ == '__main__':
    files = [
        r"e:\ffmpegFormatGuide.txt",
        r"e:\ffplayFormatGuide.txt"
    ]
    # print(check(files))
    print(check2(files))
    pass
    