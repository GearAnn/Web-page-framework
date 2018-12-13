#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: (4)WSGI模块之导入HTML.py
@time: 2018/11/8 0008 上午 1:45
"""
"""
上节内容：
1.简化if包含的网页代码，用简单的函数来进行代码映射；
2.利用自定义的rounter函数，简化if/else判断的多次利用，自动匹配不同的路径，显示不同路径的网页内容

问题：
如何导入html文件，并且让Python中的程序的执行结果，在网页中显示出来呢

本节内容：
导入一个html文件，让当前的时间打印在网页中显示出来。
"""

from wsgiref.simple_server import make_server
import time


def current_time(request):
    cur_time = time.ctime(time.time())
    f = open("current_time.html", 'rb')
    data = f.read()                      # 注意：是byte类型
    data = str(data, 'utf8').replace('{cur_time}', str(cur_time))
    # 因为html本质就是一大推字符串，所以可以利用字符串拼接，但byte类型要先转码，然后字符串的拼接
    # 这里用 {} 把html文档中要替换的内容包了起来，所以直接replace函数替换{}就可以了
    return [data.encode('utf8')]


def routers():
    urlpatterns = (('/current_time', current_time),)
    return urlpatterns


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']

    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break

    if func:
        return func(environ)

    else:
        return [b'<h1>404</h1>']


httpd = make_server('', 8080, application)

print('Serving http on port 8000...')

httpd.serve_forever()


"""
结语：
1.这就是我们自己写的一个简单的Web框架，我们免去了建立socket,bind,listen等过程；
2.也不用在打印请求信息，然后再在其中寻找我们需要的信息，我们只需要调用‘environ’即可；
3.设置不同的路径和函数，用for in循环利用router,urlpattern做出匹配，就可以访问我们需要的网页；
4.网页的信息也只需要做一个字符串的拼接。
5.我们写函数也只需要在 很清晰的代码 前面写def就可以了，然后给函数命名，用return做映射。
"""



















