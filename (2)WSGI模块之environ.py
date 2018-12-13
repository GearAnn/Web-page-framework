#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: WSGI模块之environ.py
@time: 2018/11/7 0007 下午 11:02
"""

"""
上节内容：
WSGI模块中说到，WSGI模块简化了4个过程：
1.socket准备过程（创建socket,bind,listen），封装socket对象
2.http解析过程
3.start_response简化了响应头的设置
4.请求信息全封装到了environ

问题：
如何利用environ来设置不同路径下的网页？

本节内容：
利用environ['PATH_INFO']拿到URL，然后利用if/else判断，赋予不同的URL路径不同的网页内容

"""

from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']   # 拿到的是个URL
    if path == '/book1':  # 如果拿到的是/BOOK这个URL地址则返回一个页面
        return [b'<h1>hello book1</h1>']  # 返回hello book,加上b是因为socket本质上byte传输

    if path == '/book2':
        return [b'<h1>nihao book2</h1>']  # 返回nihao book2,加上b是因为socket本质上byte传输

    else:
        return [b'<h1>404</h1>']

    # 即，通过environ拿到不同的URL地址，return返回不同的html内容，从而形成不同页面的内容

    return [b'<h1>hello</h1>']


httpd = make_server('', 8080, application)

print('Serving http on port 8000...')

httpd.serve_forever()

"""
作用：若想增加网页URL，只需要用 if 来添加不同的 path路径（/book1,/book2） 即可。
"""