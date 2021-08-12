import site

import pafy, pytube, youtube_dl as yt

site.addsitedir(r'E:\Projects\Monties\2020\operatingSystem')
import filesystem2inheritance as fs
from m3ta import save, load, show

videos = fs.user['videos']['ytdls']

def url(video):
    id = video.title.split('-')[-1]
    if len(id)==11:
        return ''.join(('https://www.youtube.com/watch?v=',id.split('.')[0]))
    
def description(url):
    # return pafy.new(url).description
    # return pytube.YouTube(url).description
    return yt.YoutubeDL().description
    
def scrape(folder):
    for i,video in enumerate(folder.leaves,1):
        try:
            print(f'{i} of {len(folder.leaves)}')
            
            print(f'\t{video}\n\t{url(video)}')
            if (link:=url(video)):
                text = description(link)
                print(f'\t\t{text}\n\n\n')
            yield text
        except:
            continue
    
if __name__ == '__main__':
    # descriptions = {i for i in scrape(videos)}
    y = yt.YoutubeDL()
    inf = y.extract_info('https://www.youtube.com/watch?v=A1cmPdxf2KY',download=False)
    # print(inf)
    show(inf.keys())
    # help(inf)
    
    
    
    
    
    
    
    
    
    pass