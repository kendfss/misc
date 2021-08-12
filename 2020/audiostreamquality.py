import site, os
from moviepy.editor import VideoFileClip
from moviepy.audio.io.readers import FFMPEG_AudioReader as ar

site.addsitedir(r'E:\Projects\Monties\2020\operatingSystem')
import cabinet as fs
from m3ta import save, load, empty, nameSpacer, gather, show, module

def pop(arg=None)
    if arg:
        if isinstance(arg,module):
            os.startfile(os.path.dirname(module.__file__))
        else:
            mstr = arg.__module__
            if (top:=mstr.split('.')[0]) in locals().keys():
                m = eval(top)
            else:
                eval('import {top}')
            os.startfile(os.path.dirname(m.__file__))
    else:
        os.startfile(os.getcwd())

videos = fs.user['videos']['ytdls']

def audiostream(path):
    return VideoFileClip(path).audio
    



if __name__ == '__main__':
    help(ar)
    # for vid in videos['music']['singles'].leaves:
        # help(audiostream(vid.path))
        # help(VideoFileClip(vid.path))
        
        # print
        # Attributes
         # |  ------------
         # |
         # |  nbytes
         # |    Number of bits per frame of the original audio file.
         # |
         # |  fps
         # |    Number of frames per second in the audio file
         # |
         # |  buffersize
         # |    See Parameters.
         # |
         # |  ...
         # |  ...
         # |
         # |  to_soundarray(self, tt=None, fps=None, quantize=False, nbytes=2, buffersize=50000)
        # video = VideoFileClip(vid.path)
        # print(video.audio_bitrate)
        # audio = audiostream(video.path)
         
        # print('\n\t'.join(str(i) for i in (audio.nbytes,audio.fps,audio.buffersize)))