#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/05/15 23:36
# @Author  : Hython.com
# @File    : run.py
# @IDE     : PyCharm
from flask import Flask, render_template, request
from module import item

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("base.html")


@app.route("/results")
def result_page():
    page = request.args.get('sp')
    if page == None:
        search = request.args.get('search')
        soup = item.find_search_content(search)
        all_item = item.every_video(soup)
        all_page = item.page_bar(soup)
        return render_template("result.html", search=search, all_item=all_item, all_page=all_page)
    elif page != None:
        search = request.args.get('q')
        page = request.args.get('sp')
        current_page = request.args.get('current_page')
        value = "q={}".format(search) + '&' + 'sp={}'.format(page)
        soup = item.find_page_content(value)
        all_item = item.every_video(soup)
        all_page = item.page_bar(soup)
        return render_template("result_page.html", search=search, all_item=all_item, all_page=all_page,
                               current_page=current_page, int=int)


@app.route("/download")
def download():
    value = request.args.get('value')
    download_type, url = value.split('&')
    if download_type == 'mp3':
        item.download_mp3(url)
        return render_template('download.html')
    elif download_type == 'mp4':
        item.download_mp4(url)
        return render_template('download.html')


if __name__ == "__main__":
    app.run(debug=True)
