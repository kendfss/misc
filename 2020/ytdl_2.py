import os

"""
rewrite query to work between functions

"""

from pytube import YouTube
from tqdm import tqdm

from m3ta import nameSpacer,beeper

get = lambda url: YouTube(url)
    # return yt.streams

def both(got,folder=r"c:\users\kenneth\downloads"):
    
    
    streams = got.streams.filter(progressive=True)
    return streams.get_highest_resolution()
    

    
def audio(got,folder=r'f:\samples\soundflowering\pytubes'):
    """
    Collects the optimal audio stream
    """
    # yt = YouTube(url)
    streams = got.streams.filter(only_audio=True)
    return streams.get_audio_only()
    
audio = lambda got: got.streams.filter(only_audio=True).get_audio_only()
both = lambda got: got.streams.filter(progressive=True).get_highest_resolution()
video = lambda got: got.streams.filter(only_video=True).get_highest_resolution()

def download(stream,folder):
    print(f'\tname:\t{stream.default_filename}\n\tsize:\t{stream.filesize}\n\tfolder:\t{folder}')
    stream.download(folder)
    print("\tdone")
    

    
def main(links,a=True,b=True,v=False,adir=r'f:\samples\soundflowering\pytubes',bdir=r"c:\users\kenneth\downloads",vdir=r"c:\users\kenneth\videos"):
    counter = 1
    logname = nameSpacer('ytdl-output.txt')
    for link in links:
        print(f'{counter} of {len(links)}', file=open(logname, 'a'))
        try:
            yt = get(link)
            print(f'url:\t{link}\n\t', file=open(logname, 'a'))
            if a:
                au = audio(yt)
                if not os.path.exists(os.path.join(adir,au.default_filename)):
                    print(f'Downloading "{yt.title}"\n\tformat:\tAudio', file=open(logname, 'a'))
                    download(au,adir)
            if b:
                bt = both(yt)
                if not os.path.exists(os.path.join(bdir,bt.default_filename)):
                    print(f'Downloading "{yt.title}"\n\tformat:\tProgressive', file=open(logname, 'a'))
                    download(bt,bdir)
            if v:
                vd = video(yt)
                if not os.path.exists(os.path.join(vdir,vd.default_filename)):
                    print(f'Downloading "{yt.title}"\n\tformat:\tVideo', file=open(logname, 'a'))
                    download(vd,vdir)
            counter += 1
        except ValueError:
            print(f'ValueError: {link}', file=open(logname, 'a'))
            counter += 1
            # continue
        except KeyError:
            print(f'KeyError: {link}', file=open(logname, 'a'))
            counter += 1
        
def progressive(url,folder=r'c:\users\kenneth\downloads'):
    """
    A progressive stream features audio and video in a single file
    """
    yt = get(url)
    streams = yt.streams.filter(progressive=True)
    stream = streams.get_highest_resolution()
    if not os.path.exists(os.path.join(folder,stream.default_filename)):
        print(f'Downloading "{yt.title}"\n\tformat:\tProgressive')
        download(stream,folder)
def sample(url,folder=r'f:\samples\soundflowering\pytubes'):
    yt = get(url)
    streams = yt.streams.filter(only_audio=True)
    stream = streams.get_audio_only()
    if not os.path.exists(os.path.join(folder,stream.default_filename)):
        print(f'Downloading "{yt.title}"\n\tformat:\tAudio')
        download(stream,folder)
def progressive(url,folder=r'c:\users\kenneth\downloads'):
    yt = YouTube(url)
    streams = yt.streams.filter(only_video=True)
    stream = streams.get_highest_resolution()
    # if not os.path.exists(os.path.join(folder,stream.default_filename)):
    print(f'Downloading "{yt.title}"\n\tformat:\tVideo')
    print(f'\tname:\t{stream.default_filename}\n\tsize:\t{stream.filesize}\n\tfolder:\t{folder}')
    stream.download(folder)
    print("\tdone")


if __name__ == '__main__':
    # audio('https://www.youtube.com/watch?v=3vD4df_63wo')
    # audio('https://www.youtube.com/watch?v=FLP6QluMlrg')
    
    targets = [
        "https://www.youtube.com/watch?v=QRYzre4bf7I",
        "https://www.youtube.com/watch?v=zKcT9Y_f2-0",
        "https://www.youtube.com/watch?v=KjOC4MghYRA",
        "https://www.youtube.com/watch?v=bf9J35yzM3E",
        "https://www.youtube.com/watch?v=nz11b5mkNGQ",
        "https://www.youtube.com/watch?v=duojBgOv6h0",
        "https://www.youtube.com/watch?v=S_caTsMFuBM",
        "https://www.youtube.com/watch?v=zbubXrtmKRo",
        "https://www.youtube.com/watch?v=E0de43ngMvc",
        "https://www.youtube.com/watch?v=jFzJFdEJwQc"
        
    ]
    # from random import choice
    # url = choice(targets)
    # print(url)
    progressive('https://www.youtube.com/watch?v=MHlwl6GsT8s')
    # [both(i) for i in targets]
    # main(targets)
    # counter = 1
    # for i in targets:
        # print(f'{counter} of {len(targets)}')
        # progressive(i)
        # counter += 1
    # print(os.stat(r"c:\users\kenneth\downloads\Making modern GUIs with Python and ElectronJS.mp4").st_size)
    # help(sorted)  