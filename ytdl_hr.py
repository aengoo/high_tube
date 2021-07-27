from urllib.error import *
import ffmpeg
from pytube import YouTube, Playlist
import os
import re

# YouTube('https://youtu.be/LdgrwynDBY8').streams.get_highest_resolution().download()


def download_merge(vid, save_path):
    try:
        yt = None
        if isinstance(vid, str):
            yt = YouTube(vid)
        elif isinstance(vid, YouTube):
            yt = vid
        else:
            print('invalid parameter type for [vid] in download()')
            exit()
        save_dir = os.path.join(save_path, str(yt.publish_date.year))
        regex = r'[?|*|\\|:|/|.|<|>|"|\|]'
        nm = re.sub(regex, '', yt.title)

        if not os.path.exists(os.path.join(save_dir, nm + '.mp4')):
            print('Downloading [' + nm + '] ...', end='')
            # yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first().download(save_dir, nm)
            # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(save_dir, nm)
            tmp_dir = 'tmp'
            yt.streams.filter(progressive=False, file_extension='mp4', type='video').order_by(
                'resolution').desc().first().download(tmp_dir, 'v')
            yt.streams.filter(progressive=False, file_extension='mp4', type='audio').order_by(
                'abr').desc().first().download(tmp_dir, 'a')
            print('Complete!!')
            print('Merging [' + nm + '] ...', end='')
            v = ffmpeg.input(os.path.join(tmp_dir, 'v.mp4'))
            a = ffmpeg.input(os.path.join(tmp_dir, 'a.mp4'))
            os.makedirs(save_dir, exist_ok=True)
            o = ffmpeg.output(v, a, os.path.join(save_dir, nm + '.mp4'), vcodec='copy', acodec='copy', strict='experimental')
            o.run()
            print('Complete!!')
        else:
            print('[' + nm + '] already exists...pass')
        return False
    except (HTTPError, URLError):
        print('fail...retry')
        return True


path = 'test'
os.makedirs(path, exist_ok=True)

pls = ('https://www.youtube.com/playlist?list=PLfeV8c6fNqzlwiU83uOJMj9UstVQpOOC4',
       'https://www.youtube.com/playlist?list=PLfeV8c6fNqzkpyg9cwgMez358o3Ed-fWl',
       'https://www.youtube.com/playlist?list=PLJ8elSeS2xGwO81ZMj2bo6VWDF05BWUun'
       )

# pls = ('https://www.youtube.com/playlist?list=PLJ8elSeS2xGwO81ZMj2bo6VWDF05BWUun',)

for pl_url in pls:
    pl = Playlist(pl_url)
    for video in pl.videos:
        retry = True
        while retry:
            retry = download_merge(video, path)


