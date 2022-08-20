from pytube import YouTube 
from sys import argv

#link = argv[1]
link = "https://youtu.be/tPEE9ZwTmy0"
yt = YouTube(link)

for a in dir(yt):
    if not a.startswith("_") :
        print(a)
print('\n'*3)

title, views = yt.title, yt.views 
other =  yt.thumbnail_url
print(title)
print(views)
print(other)

#print(dir(yt.streams))
yd = yt.streams.get_lowest_resolution()
yd.download("")
