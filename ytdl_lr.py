from urllib.error import *

from pytube import YouTube, Playlist
import os

#YouTube('https://youtu.be/LdgrwynDBY8').streams.get_highest_resolution().download()


def download(vid, save_path):
    try:
        if isinstance(vid, str):
            yt = YouTube(vid)
        elif isinstance(vid, YouTube):
            yt = vid
        else:
            print('invalid parameter type for [vid] in download()')
            exit()
        save_dir = os.path.join(save_path, str(yt.publish_date.year))
        nm = yt.title
        print('downloading [' + nm + '] ...', end='')
        # yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first().download(save_dir, nm)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(save_dir, nm)
        print('complete')
        return False
    except HTTPError:
        print('fail...retry')
        return True

path = './test'
os.makedirs(path, exist_ok=True)

pls = ('https://www.youtube.com/playlist?list=PLfeV8c6fNqzlwiU83uOJMj9UstVQpOOC4',
       'https://www.youtube.com/playlist?list=PLfeV8c6fNqzkpyg9cwgMez358o3Ed-fWl',
       'https://www.youtube.com/playlist?list=PLJ8elSeS2xGwO81ZMj2bo6VWDF05BWUun'
       )

for pl_url in pls:
    pl = Playlist(pl_url)
    for vid in pl.videos:
        retry = True
        while retry:
            retry = download(vid, path)


