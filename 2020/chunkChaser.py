import os
import requests, tqdm, pyperclip

downloads = os.path.join(os.path.expanduser('~'),'Downloads')

def chase(url,destination=downloads,copy=False):
    name = url.split('/')[-1]
    path = os.path.join(destination,name)
    
    r = requests.get(url,stream=True)
    size = int(r.headers['content-length'])
    chunkSize = 1024
    chunks = r.iter_content(chunk_size=chunkSize)
    chunkNum = len(chunks)-1
    unit = 'KB'
    
    with open(path,'wb') as file:
        print(f'Downloading {name}')
        for data in tqdm.tqdm(iterable=chunks,total=size/chunkSize, unit=unit):
            file.write(data)
            print(f'acquired chunk {len(chunks)-chunkNum} of {len(chunks)}')
            chunkNum -= 1            
    print("\n\nDownload complete!\n\n")
    print("       ",path)
    
    return path if not copy else pyperclip.copy(path)
if __name__ == '__main__':
    url = 'https://data.keithito.com/data/speech/tacotron-20180906.tar.gz'
    chase(url)