import os
from subprocess import run

destination = os.path.join(os.path.expanduser('~'),'videos','ytdls')
path = lambda name: os.path.join(destination,name)
def download(links,dst=destination):
    if isinstance(links,str):
        links = links.split(',')
    os.chdir(dst)
    for i,link in enumerate(links,1):
        print(f'{i} of {len(links)}')
        run(f'youtube-dl "{link}"')
        run('date')
        print("\n\n\n\n")

music = path('music')
graff = path('graff')
maths = path('maths')
physics = path('physics')
politics = path('politics')
other = path('other')
os.makedirs(destination,exist_ok=True)
os.makedirs(politics,exist_ok=True)
os.makedirs(physics,exist_ok=True)
os.makedirs(maths,exist_ok=True)
os.makedirs(graff,exist_ok=True)
os.makedirs(music,exist_ok=True)
os.makedirs(other,exist_ok=True)

# os.chdir(destination)
if __name__ == '__main__':
    # links = "https://www.youtube.com/watch?v=oXx2TczveMI,https://www.youtube.com/watch?v=-uW5NuD8O6Q".split(',')
    # links = 'https://www.youtube.com/watch?v=v7MXwFwn2yA,https://www.youtube.com/watch?v=TgpycJWK1JY,https://www.youtube.com/watch?v=ORDIJJh_Tu4,https://www.youtube.com/watch?v=zyzzhuUdcXw,https://www.youtube.com/watch?v=o1EhgcPLgiw'.split(',')
    gra = 'https://www.youtube.com/watch?v=xwp9hevKo-Q,https://www.youtube.com/watch?v=BtahvUxFBkA,https://www.youtube.com/watch?v=BtahvUxFBkA,https://www.youtube.com/watch?v=BtahvUxFBkA.https://www.youtube.com/watch?v=5Q-2lbATI0U&t=12s,'.split(',')
    pol = 'https://www.youtube.com/watch?v=vdZU4HKSxHs,'.split(',')
    mu = 'https://www.youtube.com/watch?v=Eaqxo1R7raA,https://www.youtube.com/watch?v=xPwp6YsraZw,https://www.youtube.com/watch?v=AeDvoHJ__hg,https://www.youtube.com/watch?v=XUo-XKsYF6E,https://www.youtube.com/watch?v=AF4kNV2Ka4c&list=PLCX_SlmERpRO-FuZbHX4hBy4oElCsHvy-,https://www.youtube.com/watch?v=TQtEFdyhgdE,https://www.youtube.com/watch?v=Y9HgjQvDH3A,https://www.youtube.com/watch?v=ii63fKLTSuU,https://www.youtube.com/watch?v=ZwQwXlQyha8,https://www.youtube.com/watch?v=FUkiNAyjYcA'.split(',')
    # ctr = "$i = 0;foreach ($s in $l) {$i += 1;[string]::Format('{0} of {1}',$i,$l.length);youtube-dl $s;date;'';'';'';''}"
    # download(links,graff)
    download(links,music)


    
    



