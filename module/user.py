#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/05/23 0:51
# @Author  : Hython.com
# @File    : user.py
# @IDE     : PyCharm
from common.database import Database

class User(object):
    def __init__(self, name, account, password):
        self.name = name
        self.account = account
        self.password = password

    @staticmethod
    def is_login_valid(account, password):
        user_data = Database.find_one(collection='users',query={"account":account})
        if user_data is None:
            return False
        if user_data['password'] != password:
            return False
        return True

    def save_to_db(self):
        Database.insert(collection='users',data=self.json())

    def json(self):
        return {
            "name":self.name,
            "account":self.account,
            "password":self.password
        }

    def find_user_data(account):
        user_data = Database.find_one(collection='users',query={"account":account})
        return user_data