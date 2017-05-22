#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/05/21 21:08
# @Author  : Hython.com
# @File    : database.py
# @IDE     : PyCharm
import pymongo


# client = pymongo.MongoClient(['localhost:27017'])
# DATABASE = client['test1']
# DATABASE['student'].insert({"name":"leo","age":"20"})
# DATABASE['student'].remove({"name":"leo"})

class Database(object):
    URI = ['localhost:27017']
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['project']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
