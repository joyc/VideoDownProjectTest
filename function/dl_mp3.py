#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/05/15 22:57
# @Author  : Hython.com
# @File    : dl_mp3.py
# @IDE     : PyCharm
import youtube_dl

ydl_opts = {'format': 'bestaudio/best', 'outtmpl':'/video/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=zjQGYSEHtto'])