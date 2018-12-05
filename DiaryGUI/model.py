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
            sql = "insert into diary(title, mood, weather, category, content, c_time) values(%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (
                kwargs['title'], kwargs['mood'], kwargs['weather'],
                kwargs['category'], kwargs['content'],
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
            self.close()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)

    def get_info_by_id(self, diary_id):
        try:
            self.connect()
            sql = "select * from diary where id = %s"
            self.cursor.execute(sql, (diary_id,))
            self.close()
            return self.cursor.fetchone()
        except Exception as e:
            print(e)

    def get_info_by_date(self):
        try:
            self.connect()
            sql = "select * from diary order by c_time desc"
            # sql = 'select * from diary where date(c_time)>=%s and date(' \
            #       'c_time)<=%s'
            # self.cursor.execute(sql, '2018-11-01', '2018-11-02')
            self.cursor.execute(sql)
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def get_info_by_category(self):
        try:
            self.connect()
            sql = "select * from diary order by category"
            self.cursor.execute(sql)
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def get_max_time(self):
        try:
            self.connect()
            sql = "select max(c_time) from diary"
            self.cursor.execute(sql)
            self.close()
            return self.cursor.fetchone()
        except Exception as e:
            print(e)

    def get_min_time(self):
        try:
            self.connect()
            sql = "select min(c_time) from diary"
            self.cursor.execute(sql)
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
            results = self.cursor.execute(sql, (diary_id,))
            self.close()
            return results
        except Exception as e:
            print(e)


if __name__ == '__main__':
    mod = DiaryModel()
    result = mod.get_diary_list()
    # print(result)
    for i in result:
        print(i)
