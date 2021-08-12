"""
https://stackoverflow.com/questions/64283087/how-would-i-make-this-stream-a-playlist-and-also-not-stop-responding-when-you-hi
"""

import vlc
import pafy
import time
from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        
        Frame.__init__(self,master)
        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title('Lofi.Chill')

        self.pack(fill=BOTH, expand=1)

        play_button = Button(self, text = 'play me some lofi', command=self.happy_song)
        play_button.place(x=0,y=0)

        quit_button = Button(self, text = 'quit', command=self.client_exit)
        quit_button.place(x=200,y=0)


    def client_exit(self):
        exit()
    
    def happy_song(self):
        Stream('https://www.youtube.com/watch?v=XN41UJ7EZ4E&ab_channel=Andrela-Chxn')

class Stream:
    def __init__(self, url):
        self.url = url

        video = pafy.new(url)
        best = video.getbestaudio()
        playurl = best.url

        instance = vlc.Instance()
        player = instance.media_player_new()
        media = instance.media_new(playurl)

        media.get_mrl()

        player.set_media(media)
        player.play()
        
        while True:
            time.sleep(1)



root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop() 