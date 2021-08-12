import os,shutil,subprocess

import pyperclip

folder = r'F:\Samples\Miscellaneous Samples\Pianobook\Air Piano\Air Piano - All Signals Samples'
contents = set(' '.join(j for j in i.split()[:-1]) for i in os.listdir(folder))
structure = {
    "files":set(i for i in os.listdir(folder)),
    "groups":set(' '.join(j for j in i.split()[:-1]) for i in os.listdir(folder)),
    # "nonRT":set(i for i in structure['groups'] if i.split()[-1].lower() != 'rt'),
    "groupHandles":set(' '.join(j for j in i[len('Air Upright'):].split()[:-1]) for i in os.listdir(folder)),
    "":0,
    "":0,
    "":0,
    "":0,
    "":0,
    
}

# contentGroups = set(i for i in os.listdir(folder))
# c = set(' '.join(j for j in i.split()[:-1]) for i in os.listdir(folder))

def generateIndex():
    groups = {}
    for handle in structure['groupHandles']:
        samples = set(file for file in structure['files'] if handle in file)
        groups[handle] = {'len':len(samples),'content':samples,'paths':{}}
        for file in groups[handle]['content']:        
            groups[handle]['paths'][file] = os.path.join(folder,file)
    return groups

def makeCopies():
    workspace = os.path.join(folder,'premonoliths')
    groups = generateIndex()
    counter = 0
    for handle in structure['groupHandles']:
        location = os.path.join(workspace,handle)
        os.makedirs(location,exist_ok=True)
        for file in groups[handle]['content']:
            shutil.copy(groups[handle]['paths'][file],location)
            counter += 1
            print(f'{counter} of {len(structure["files"])}')
    cmd = f'explorer "{workspace}"'
    subprocess.run(cmd)

def generateFinals():
    dst1 = r"F:\Samples\minez\beau dun garted\pianobook dwps"
    dst2 = r"F:\Samples\minez\beau dun garted\pianobook dwbs"
    counter = 1
    L = len(structure['groupHandles'])
    for handle in structure['groupHandles']:
        d1 = os.path.join(dst1,handle)
        d2 = os.path.join(dst2,handle)
        os.makedirs(d1,exist_ok=True)
        os.makedirs(d2,exist_ok=True)
        print(f'{counter} of {L}')
        counter += 1
# makeCopies()
# generateFinals()

# cmd = f'explorer "{os.path.join(folder,'premonoliths')}"'
# print(cmd)
# subprocess.run(cmd)

# for key,val in groups.items(): print(key,val,sep='\n',end='\n\n')
# print(len(structure['files']),structure['files'])
# print(len(structure['groups']),structure['groups'])
# print(len(structure['nonRT']),structure['nonRT'])
# print(len(structure['groupHandles']),structure['groupHandles'])
