#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : dbUtils.py
# @Time    : 2018/6/15 15:21
# @Software: PyCharm

import pymysql
import config

class DbConnention(object):

    def __init__(self):
        self.__conn_dict = config.PY_MYSQL_CONN_DICT
        self.conn = None
        self.cursor = None

    def connect(self, cursor=pymysql.cursors.DictCursor):
        self.conn = pymysql.connect(**self.__conn_dict)
        '''self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='fanglei',
            port=3306,
            database='test',
            charset='utf8'
        )'''
        self.cursor = self.conn.cursor(cursor=cursor)

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
