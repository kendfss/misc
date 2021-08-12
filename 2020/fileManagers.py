import os


counter = 1

def musicManager():
    global counter
    source = r'C:\Users\Kenneth\Downloads\music'
    dest = r'C:\Users\Kenneth\Music\Collection'
    folders = tuple(os.path.join(source,i) for i in os.listdir(source) if os.path.isdir(os.path.join(source,i)))
    end = len(folders)
    
    for folder in folders:
        subs = os.listdir(folder)
        for sub in subs:
            op = os.path.join(folder,sub)
            np = os.path.join(dest,sub)
            os.rename(op,np)
            print(f'\nmoved {sub} to {np}\n')
        print(f'\nfinished with folder {counter} of {end}:\n        {folder.split(os.sep)[-1]}\n\n')
        counter += 1
    print('\n\n\n****done****\n\n\n')

if __name__== '__main__':
    musicManager()