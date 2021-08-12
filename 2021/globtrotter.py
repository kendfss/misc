import glob, os

folder = r'C:'
folder = r'f:/ytdls'

# files = r'**\git-remote-https.exe'.split()
files = r'**/*slowthai*'.split()
os.chdir(folder)
for file in files:
    # file = '**\\' + file
    print(file)
    itr = glob.iglob(file, recursive=True)
    # itr = glob.iglob(file)
    for i in itr:
        print(i)
    # [*map(print, itr)]
    # print(glob.glob(file[:2], recursive=True))
    # print(glob.glob(file))