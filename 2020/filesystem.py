import os
from dataclasses import dataclass

from send2trash import send2trash

from m3ta import show, delevel

@dataclass
class address:
    """
    A systemic pointer to the location of the data associated with a file system object
    """
    # def init(self,path:str):
        # assert os.path.exists(self.path), f'"{path}" is not a valid address on this system'
        # self.path = path
    path:str
    
    @property
    def exists(self):
        return os.path.exists(self.path)
    @property
    def isdir(self):
        return os.path.isdir(self.path)
    @property
    def isfile(self):
        return os.path.isfile(self.path)
    @property
    def obj(self):
        if self.isdir:
            return directory(self.path)
        elif self.isfile:
            return file(self.path)
        else:
            raise ValueError(f'"{self.path}" is not a valid address on this system')



class directory:
    def __init__(self,path:str):
        assert address(path).isdir, f'"{path}" is not a directory'
        self.path = path
        cntnt = (address(os.path.join(path,i)) for i in os.listdir(path))
        for i in cntnt:
            name = os.path.split(i.path)[1]
            if i.isdir:
                setattr(self,name,i.path)
            elif i.isfile:
                setattr(self,os.path.splitext(name)[0],i.path)
    
    @property
    def children(self):
        return tuple(i for i in os.listdir(self.path) if address(os.path.join(self.path,i)).isdir)
    @property
    def files(self):
        return tuple(i for i in os.listdir(self.path) if address(os.path.join(self.path,i)).isfile)
    @property
    def content(self):
        return tuple(os.listdir(self.path))
    @property
    def name(self):
        return os.path.split(self.path)[1]
    @property
    def ancestors(self):
        level = []
        p = self.path[:]
        while p != delevel(p):
            p = delevel(p)
            level.append(p)
        return tuple(level)[::-1]
    @property
    def depth(self):
        return len(self.ancestors)
    @property
    def root(self):
        return self.ancestors[0].split(':')[0]
        
    def show(self, indentation:int=1, enum:bool=False, start:int=1, indentor:str='\t'):
        assert indentation>0, f'"{indentation}" is not a viable indentation level'
        print((indentation-1)*'\t'+self.name)
        show(self.content,indentation,enum,start,indentor)
        
    def heritage(self):
        print(f'\nheritage({self.name.title()})')
        ancs = list(self.ancestors)
        ancs.append(self.path)
        for i,anc in enumerate(ancs):
            print('\t'+('','.'*i)[i>0]+i*'  '+[i for i in anc.split(os.sep) if i][-1])
    def delete(self,recycle=True):
        send2trash(self.path) if recycle else os.remove(self.path)
    def container(self,steps=1,obj=False):
        return directory(delevel(self.path,steps)) if obj else delevel(self.path,steps)
    
    def isroot(self):
        return not self.depth
    def __bool__(self):
        return len(os.listdir(self.path))>0
    def __str__(self):
        return self.path
    def __repr__(self):
        return str(self)
    
    
    


class file:
    def __init__(self,path:str):
        assert address(path).isfile, f'"{path}" is not a file'
        self.path = path
    
    @property
    def name(self):
        return os.path.split(self.path)[1]
    @property
    def ext(self):
        return os.path.splitext(self.name)[1]
    @property
    def title(self):
        return os.path.splitext(self.name)[0]
    @property
    def ancestors(self):
        level = []
        p = self.path[:]
        while p != delevel(p):
            p = delevel(p)
            level.append(p)
        return tuple(level)[::-1]
    @property
    def depth(self):
        return len(self.ancestors)
    @property
    def root(self):
        return self.ancestors[0].split(':')[0]
    
    def delete(self,recycle=True):
        send2trash(self.path) if recycle else os.remove(self.path)
    def container(self,steps=1,obj=False):
        return directory(delevel(self.path,steps)) if obj else delevel(self.path,steps)
    def heritage(self):
        print(f'\nheritage({self.name.title()})')
        ancs = list(self.ancestors)
        ancs.append(self.path)
        for i,anc in enumerate(ancs):
            print('\t'+('','.'*i)[i>0]+i*'  '+[i for i in anc.split(os.sep) if i][-1])
    def __str__(self):
        return self.path
    def __repr__(self):
        return str(self)
      
if __name__ == '__main__':
    dp = r'c:\users\kenneth\videos'
    # print(directory(dp))
    # show(directory(dp).fils,)
    fp = r'c:\users\kenneth\pyo_rec.wav'
    # print(os.path.isfile(fp))
    # print(file(fp))
    
    d = address(dp).obj
    print(d)
    d.show(1)
    f = address(fp).obj
    print(f)
    
    system = (d,f)
    print(system)
    print([i.name for i in system])
    print([i.depth for i in system])
    print([i.ancestors for i in system])
    print([i.heritage() for i in system])
    print([i.root for i in system])
    # d.heritage()
    # os.rename('Few Nolder','randombumbashit')
    # print(os.listdir('randombumbashit'))