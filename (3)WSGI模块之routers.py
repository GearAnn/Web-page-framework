#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: WSGI模块之route.py
@time: 2018/11/7 0007 下午 11:34
"""


"""
上节内容：
WSGI模块之environ中说到，
利用environ['PATH_INFO']拿到URL，然后多次利用if/else判断，赋予不同的URL路径不同的网页内容

问题：
如果要显示大量的不同页面内容，是不是需要大量重复的if/else来判断呢？

本节内容：
1.简化if包含的网页代码，用简单的函数来进行代码映射；
2.利用自定义的rounter函数，简化if/else判断的多次利用，自动匹配不同的路径，显示不同路径的网页内容

"""


from wsgiref.simple_server import make_server


def f1(request):                        # 简化if包含的网页代码,用f1来映射
    return [b'<h1>hello book1</h1>']


def f2(request):
    return [b'<h1>nihao book2</h1>']


def routers():
    urlpatterns = (('/book1', f1), ('/book2', f2))
    # 由元组构成，元组的第一个参数是路径，第二个参数是路径对应的函数，也可以换成字典
    return urlpatterns


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']  # path='book1/book2'

    urlpatterns = routers()
    func = None  # 提前设置了func为空
    for item in urlpatterns:  # 从urlpatterns中拿到元组，第一次拿到book1,第二次拿到book2
        if item[0] == path:   # 从拿到的元组中选择第一个元素去匹配path，匹配不成功就不往下走了
            func = item[1]    # 走到这步就是已经匹配成功了，此时item[1]这个函数，也就是f1,用func去接收
            break

    if func:    # 若func接收到了f1/f2，即func不为空，则返回func所接收的函数执行
        return func(environ)

    else:
        return [b'<h1>404</h1>']

    # 利用了一个for in循环来简化了 if判断的多次使用！！替代的就是下列代码！1
    # if path == '/book1':
    #     return f1()
    #
    # if path == '/book2':
    #     return f2()
    #
    # else:
    #     return [b'<h1>404</h1>']
    #
    # return [b'<h1>hello</h1>']


httpd = make_server('', 8080, application)

print('Serving http on port 8000...')

httpd.serve_forever()

"""
作用：
若想增加网页的URL,只需要在urlpatterns中以元组/字典的形式去增加函数名和函数即可，然后在写对应的函数内容即可。
"""