#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : diary_app.py
# @Time    : 2018/6/14 15:22
# @Software: PyCharm

from tornado import web, httpserver, ioloop
from model import DiaryModel
import datetime


class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")


class CreateDiaryHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("create.html")

    def post(self, *args, **kwargs):
        # 获取create页面的数据
        weather = self.get_argument('weather')
        mood = self.get_argument('mood')
        content = self.get_argument('content')

        print(weather, mood, content)

        # 入数据库
        model = DiaryModel()
        diary_id = model.create_diary(weather=weather, mood=mood,
                                      content=content)
        if diary_id:
            self.redirect(r"/list")
        else:
            self.write("failed, please try again")


class ListDiaryHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        model = DiaryModel()
        diary_list = model.get_diary_list()
        self.render("list.html", diary_list=diary_list)


application = web.Application(
    [(r"/", IndexHandler), (r"/create", CreateDiaryHandler),
        (r"/list", ListDiaryHandler), ], )

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
