#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/05/15 22:33
# @Author  : Hython.com
# @File    : dl_mp4.py
# @IDE     : PyCharm
import youtube_dl

ydl_opts = {'outtmpl':'/video/%(title)s.%(ext)s'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=zjQGYSEHtto'])