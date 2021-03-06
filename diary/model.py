#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : model.py
# @Time    : 2018/6/15 15:31
# @Software: PyCharm

from dbUtils import DbConnention
import time

class DiaryModel(DbConnention):
    def create_diary(self, **kwargs):
        try:
            self.connect()
            sql = "insert into diary(weather, mood, content, c_time) values(%s, %s, %s, %s)"
            self.cursor.execute(sql, (kwargs['weather'], kwargs['mood'], kwargs['content'], time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
            self.close()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)

    def get_info_by_id(self, diary_id):
        try:
            self.connect()
            sql = "select * from diary where id = %s"
            self.cursor.execute(sql, (diary_id, ))
            self.close()
            return self.cursor.fetchone()
        except Exception as e:
            print(e)

    def get_diary_list(self):
        self.connect()
        sql = "select * from diary"
        try:
            self.cursor.execute(sql)
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def delete_by_id(self, diary_id):
        try:
            self.connect()
            sql = "delete from diary where id = %s"
            result = self.cursor.execute(sql, (diary_id, ))
            self.close()
            return  result
        except Exception as e:
            print(e)


# if __name__ == '__main__':
#mod = DiaryModel()
#result = mod.delete_by_id(2)
#print(result)