import os, re, site
from random import choice

import filetype as ft

from sl4ng import pop, show, getsource, shuffle, flatten, freq
from filey import Place, Library, forbiddens, ffplay, shortcuts as commons, convert, files
from pyperclip import copy, paste
# pop(Place)
# print(forbiddens)

# site.addsitedir(r'E:\Projects\Monties\2020\operatingSystem')
# import filesystem2inheritance as fs

os.chdir("f:/ytdls")
pwd = Place(os.getcwd())

ff = lambda: ffplay(paste(), loop=0)
rm = lambda: os.remove(paste())
smp = lambda: os.rename(paste(), os.path.join("samples", paste()))

root = Place(commons['home'])
# musearch = [
musearch = Library(
    root['music'],
    # root['videos']['ytdls']['music'],
    root['downloads']['music'],
    # Place(r'f:/ytdls')
)

def clear() -> None:
    Popen('clear')
    sleep(.2)
def cls() -> None:
    clear()
    show(map(repr, cd), head=False, tail=False)
def cd(path:str=None) -> None:
    global pwd
    if isinstance(path, type(None)):
        path = os.getcwd()
    os.chdir(path)
    pwd.path = path


pat = re.compile('^\.|^ntuser.dat|^_', re.I)



def videos(path):
    os.chdir(path)
    files = os.listdir(path)
    for file in files: 
        if os.path.isfile(file):
            if not pat.match(file):
                if ft.video_match(file):
                    yield(file)    
def audios(path):
    os.chdir(path)
    files = os.listdir(path)
    for file in files: 
        if os.path.isfile(file):
            if not pat.match(file):
                if ft.audio_match(file):
                    yield(file)
def findartists(artists):
    if artists=='*':
        for d in musearch:
            d = Place(d) 
            if re.match('videos', d.name, re.I):
                for f in d['music']['singles'].leaves:
                    if re.match('audio|video', f.kind, re.I):
                        yield f.path
            else:
                for p in d:
                    for f in p.leaves:
                        if not re.match('some assembly required|123 mix', f.path, re.I):
                            if re.match('audio|video', f.kind, re.I):
                                yield f.path
    else:
        rei = 0 if any(map(str.isupper, artists)) else re.I
        sep = max(forbiddens.replace('/', '')+',', key=lambda c: freq(c, artists))
        pat = '|'.join(re.escape(i.strip().replace('/', os.sep)) for i in artists.split(sep))
        print(pat+'\n\n')
        for d in musearch:
            d = Place(d) 
            for f in d.leaves:
                if re.search(pat, f.path, rei):
                    yield f.path
    
def playlist(artists:str, shuf:int=1, rep:int=float('inf')):
    """
    Create a playlist from the results of a search
    """
    results = filter(ft.audio_match, findartists(artists))
    playlist = sorted(results)
    tracks = (playlist, shuffle(playlist))[shuf]
    
    play(tracks, shuf=shuf, rep=rep)
    
def playfrom(path:str, shuf:int=1, rep:int=float('inf')):
    """
    Create a playlist from a directory
    """
    results = filter(ft.audio_match, files(path))
    playlist = sorted(results)
    tracks = (playlist, shuffle(playlist))[shuf]
    
    play(tracks, shuf=shuf, rep=rep)
    
def play(tracks:list[str], shuf:int=1, rep:int=float('inf')):
    print(f"{shuf=}\n{rep=}")
    if len(tracks):
        show(tracks, enum=True)
        while rep:
            ffplay(tracks, randomize=False, loop=False)
            rep -= 1
    else:
        raise Exception("Nothing was found")




if __name__ == '__main__':
    mysh = {
        r'C:\Users\Kenneth\Documents\bounces\bleeding_heart-master.mp3',
        r'C:\Users\Kenneth\Documents\bounces\bisto_75^1_10_2_38-crashed1_15 - Copy.mp3',
        r'C:\Users\Kenneth\Documents\bounces\broken wagon_49.mp3',
        r'C:\Users\Kenneth\Documents\bounces\fakie blips_22-crshrcvr_2-short.mp3',
        r'C:\Users\Kenneth\Documents\bounces\harryGriffifths-distillll-edit_31.mp3',
        r"C:\Users\Kenneth\Music\bounces\andar_22.wav",
    }
    mysh = shuffle(mysh)
    
    artists = r'floating points: pangaea: luso'
    artists = 'alice coltrane, aging, yussef kamaal, floating points, taylor mcferrin, filoxiny'.replace(',',':')
    artists = "doorbells/ambitions: automine:elephantitis:charles"
    artists = 'music for the uninvited'
    artists = 'crooklyn: melanie'
    artists = 'thaw cycle.mp3: passed tomorrows: wait for you'
    # artists = ""
    # artists = 'saturn' #need a new rip
    # artists = 'getaway: qadir'
    
    # artists = "ascension:noyce/over"
    # artists = "ascension:noyce/over"
    # artists = "albums"
    # artists = "crywank"
    # artists = "charles"
    # artists = "ryan patrick maguire"
    # artists = 'spaceape: milo: slowthai'
    # artists = 'empty 9-volts'
    # artists = 'gold panda,noyce/over,elan tamara,airhead/wait,empty 9-volts,believe - ep, mernau/traces, rahhh/ones,plastic dreams,clark,noyce/devil,noyce/moment,floating points'.replace(',',':')
    
    # artists = 'airhead'.replace(',',':')
    # artists = 'spaceape:  space ape'
    # artists = 'animal collective'
    # artists = 'router:sorcerer'
    # artists = 'aging'
    # artists = 'kode9, las, gantz, loom, objekt, the nativist, unitz, tnght, the chain, tessela'.replace(',',':')
    # artists = 'chaos in the cbd, henry wu, french fries, floating points, pangaea, pearson sound, anz, tyler straub, the chain, spectrasoul, spherique'.replace(',',':')
    artists = r'evenings,gold panda,dominic pierce, alix perez,mernau,youandewan,rahhh,noyce,jafu,kenny segal,taylor mcferrin,floating points,pangaea'.replace(',',':')
    artists = r'dbridge: alix perez: tyler straub'
    artists = 'ascension'
    # artists = 'weirddough:tropes'
    # artists = 'dreamgirl: king krule'
    artists = 'krule'
    artists = 'man_alive'
    # artists = 'ooz'
    # artists = 'dum surfer'
    # playlist(artists)
    
    # results = [*files(r"C:\Users\Kenneth\Downloads\music\drivies\Dsve-20210618T062958Z-001\Dsve\Porcelain")]
    # results = [r"C:\Users\Kenneth\Downloads\music\drivies\Dsve-20210618T062958Z-001\Dsve\Porcelain\03 Porcelain.mp3"]
    # play(results)

    
