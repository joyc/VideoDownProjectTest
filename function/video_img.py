import re

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=pitbull")
content = request.content
soup = BeautifulSoup(content, "html.parser")
# get all img
for element in soup.find_all('a', {"rel": "spf-prefetch"}):
    # get first group value
    img_value = element.get('href').split("=")[1]
    all_img = soup.find_all('img', {"alt":True,"onload":True,"height":True,"width":True,"data-ytimg":True})
    img = str(re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_value), str(all_img))).strip("[\"\']")
    # revise the url of img
    video_img = img.replace("&amp;", "&")
    print(video_img)
