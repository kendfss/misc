from pysndfx import AudioEffectsChain
from librosa import load
from m3ta import ffplay, nameSpacer
from itertools import chain, permutations

fx = (
    AudioEffectsChain()
    .highshelf()
    .reverb()
    .phaser()
    .delay()
    .lowshelf()
)
fxstr = """
.highshelf()
.reverb()
.phaser()
.delay()
.lowshelf()"""
def perms(fxstr):
    fxs = [i.strip().replace('.','') for i in fxstr.splitlines()]
    for i in chain(*(permutations(fxs,r) for r in range(1,len(fxs)))):
        rack = 'AudioEffectsChain().'+'.'.join(i)
        yield rack
        
for p  in perms(fxstr):print(p)
    



infile = 'my_audio_file.wav'
infile = r'c:\users\kenneth\pyo_rec.wav'
outfile = 'my_processed_audio_file.ogg'
# outfile = nameSpacer(infile)

# Apply phaser and reverb directly to an audio file.
fx(infile, outfile)

# Or, apply the effects directly to a ndarray.

y, sr = load(infile, sr=None)
y = fx(y)

# Apply the effects and return the results as a ndarray.
y = fx(infile)

# Apply the effects to a ndarray but store the resulting audio to disk.
fx(y, outfile)


# python -c "from pysndfx import AudioEffectsChain; AudioEffectsChain().reverb()(None, None)"

ffplay(outfile)