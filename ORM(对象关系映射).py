#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: ORM(对象关系映射).py
@time: 2018/11/14 0014 下午 1:01
"""

"""
ORM（对象关系映射）：
用于实现面向对象编程语言里不同类型系统的数据之间的转化，也就是用面向对象的方法去操作数据库;
从效果上说，它其实是创建了一个可在编程语言里使用的--“虚拟对象数据库”。

优点：
1.ORM使得更好的与数据库进行交互，不用使用SQL语句便可以操作；
2.避免SQL语句带来的性能问题；
3.通过QuerySet的query属性查询对应操作的SQL语句：
   author_obj=models.Author.objects.filter(id=2)
   print(author_obj)

缺点：
1.性能有所牺牲；
2.对于个别复杂查询，ORM无法实现，但是ORM也支持写 raw sql;

功能：
1.创建表单；   # 即，在 models.py 中创建一个类

2.创建关联表(foreignKey);
   一对一
   一对多
   多对多

3.如何在数据库中生成表单？在终端中输入：
    python manage.py makemigrations
    python manage.py migrate
"""























































