from pysndfx import AudioEffectsChain
from librosa import load
from m3ta import ffplay, nameSpacer, freq
from itertools import chain, permutations

# fx = (
    # AudioEffectsChain()
    # .highshelf()
    # .reverb()
    # .phaser()
    # .delay()
    # .lowshelf()
# )

def perms(fxstr):
    fxs = [i.strip().replace('.','') for i in fxstr.splitlines()]
    for i in chain(*(permutations(fxs,r) for r in range(1,len(fxs)))):
        rack = '.'.join(i)
        # yield(len(i)-1==freq('.',rack))
        yield rack
        

# print(all(perms(fxstr)))
    
def process(rack,infile,loops=2):
    fx = eval(f'AudioEffectsChain().{rack}')
    # Apply phaser and reverb directly to an audio file.
    outfile = 'my_processed_audio_file.ogg'
    fx(infile, outfile)
    
    ffplay(outfile,loop=loops)
    keep = input('keep?\n\t')
    out,ext = os.path.splitext(infile)
    out += '-'+'_'.join(i.replace('(','').replace(')','') for i in rack.split('.'))+ext
    [fx(infile, nameSpacer(out)),print('\n\tsaved\n\n\n')] if keep else None
def process2(rack,infile,loops=2):
    # Or, apply the effects directly to a ndarray.
    fx = eval(f'AudioEffectsChain().{rack}')
    y, sr = load(infile, sr=None)
    y = fx(y)

    # Apply the effects and return the results as a ndarray.
    y = fx(infile)

    # Apply the effects to a ndarray but store the resulting audio to disk.
    fx(y, outfile)


    ffplay(outfile,loop=loops)
    
    keep = input('keep?\n\t')
    [fx(y, nameSpacer(infile)),print('saved')] if keep else None



infile = r'c:\users\kenneth\pyo_rec.wav'
fxstr = """\
.highshelf()
.reverb()
.phaser()
.delay()
.lowshelf()"""
ffplay(infile,loop=False)
for rack in perms(fxstr):
    print(rack)
    process(rack,infile,2)

