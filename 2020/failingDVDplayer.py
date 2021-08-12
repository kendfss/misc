import re, os, subprocess

folder = r"G:\VIDEO_TS"
os.chdir(folder)
files = os.listdir(folder)
for file in files: print(file)

pattern = '\.VOB$'
p = re.compile(pattern)
# for file in files: print(file,p.search(file))

vobs = filter(p.search,files)
sizebool = lambda file: os.stat(file).st_size > 10**6
# for file in vobs: print(file,f"{os.stat(file).st_size:,}")

significant = filter(sizebool,vobs)
for file in sorted(significant): 
    print(file,f"{os.stat(file).st_size:,}")
    cmd = f'ffplay -autoexit -v error "{file}"'
    # try:
    # subprocess.run(cmd)
    # pass