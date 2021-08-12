from pafy import *
url = str(input("Videonun Youtube linkini girin"))
video = pafy.new(url)
streams = video.streams
for s in streams:
    print(s.resolution, s.extension, s.get_filesize(), s.url)

format = input("indirilecek turu seçin")
res = input("lutfen sectiginiz ture uygun cozunurluk yazın")

best = video.getbest(preftype=format)
best.resolution, best.extension(res, format)

konum = str(input("indirilecek yeri seçin"))
best.download(quiet=False,filepath=konum)