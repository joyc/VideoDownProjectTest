#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/05/15 23:36
# @Author  : Hython.com
# @File    : run.py
# @IDE     : PyCharm
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! By Hython"

if __name__ == "__main__":
    app.run()