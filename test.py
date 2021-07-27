from pytube import YouTube, Playlist
import os

yt = YouTube('https://www.youtube.com/watch?v=Z6Kd6bZKBH4&list=PLfeV8c6fNqzlwiU83uOJMj9UstVQpOOC4&index=4')
[print(y) for y in yt.streams]
print()
print(yt.streams.filter(progressive=True, file_extension='mp4', type='video').order_by('resolution').desc().first())
print(yt.streams.filter(progressive=False, file_extension='mp4', type='video').order_by('resolution').desc().first())
print(yt.streams.filter(progressive=False, file_extension='mp4', type='audio').order_by('abr').desc().first())
# pl = Playlist('https://www.youtube.com/playlist?list=PLfeV8c6fNqzlwiU83uOJMj9UstVQpOOC4')
# [print(v) for v in pl.videos]