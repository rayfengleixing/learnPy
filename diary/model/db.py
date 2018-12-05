#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : db.py
# @Time    : 2018/6/15 15:01
# @Software: PyCharm

import pymysql
from config import PY_MYSQL_CONN_DICT

conn = pymysql.connect(
    host='localhost',
    user='root',
    password=PY_MYSQL_CONN_DICT['password'],
    port=3306,
    database='test',
    charset='utf8'
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = 'select * from diary'

cursor.execute(sql)
rows = cursor.fetchall()

cursor.close()
conn.close()

print(rows)
