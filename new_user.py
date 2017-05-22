#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/05/23 0:46
# @Author  : Hython.com
# @File    : new_user.py
# @IDE     : PyCharm
from common.database import Database

Database.initialize()
Database.insert('user', {"email": "kevin@test.com", "password": "123456"})
user = Database.find_one('user', {"email": "kevin@test.com"})
print(user)
