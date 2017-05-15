#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/05/15 0:26
# @Author  : Hython.com
# @File    : video_time.py
# @IDE     : PyCharm
import requests
from bs4 import BeautifulSoup

request = requests.get('https://www.youtube.com/results?search_query=pitbull')
content = request.content
soup = BeautifulSoup(content, 'html.parser')
for time in soup.find_all('span', {"class":"video-time"}):
    print(time.text)