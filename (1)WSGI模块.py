#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: WSGI模块.py
@time: 2018/11/7 0007 下午 10:03
"""

# wsgiref是Python内置的服务器模块
from wsgiref.simple_server import make_server


def application(environ, start_response):  # 请求的内容都在environ里面，其是个请求对象，就可以用environ对象去拿内容
    start_response('200 OK', [('Content-Type', 'text/html')])  # 响应体的文件类型是个HTML，是以元组的格式
    # 上面一行就是响应头，其设置就仅仅变成了一个元组，以后还可以用元组格式加上JS内容

    return [b'<h1>hello</h1>']   # 响应体


httpd = make_server('', 8080, application)  # application函数作为参数传入一个实例化对象

print('Serving http on port 8000...')  # 开始监听


httpd.serve_forever()  # 对象利用serve_forever方法启动application


"""
WSGI模块简化了4个过程：
1.socket准备过程（创建socket,bind,listen），封装socket对象
2.http解析过程
3.start_response简化了响应头的设置
4.请求信息全封装到了environ

注意：environ封装请求中的所有内容（字典形式），start_response(())中的元组包含了响应体的文本类型
     需要查看请求内容的时候直接去environ中去拿

"""









