#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 基础框架的解耦之.py
@time: 2018/11/8 0008 上午 3:41
"""

"""
解耦：在一个基础框架之中，根据不同部分功能的不同，把整个代码分解成不同的文件。


第二部分：controller

controller部分涉及的主要函数是：def , return ，mysql数据库

controller的作用：
1.不同url来这里找其对应的函数来执行；

2.从数据库中取出信息到自定义的函数中去操作

比如：客户的数据是放在服务器数据库中，客户访问后网站后，需要从数据库中取出客户数据然后放在Web中显示。
     跟数据库对接的模块就是Djongo中的model函数,后面会详细讲解。
"""


def f1(request):
    # cur_time = time.ctime(time.time())
    # f = open("current_time.html", 'rb')
    # data = f.read()
    # data = str(data, 'utf8').replace('{cur_time}', str(cur_time))
    return


def f2(request):

    return


def f3(request):

    return



