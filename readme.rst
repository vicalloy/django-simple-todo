=======================
simple-todo (Django 版)
=======================

缘起
====
simple-todo最早是web.py一个中文教程的例子。后来Uliweb的作者limodou
认为这个教程很不错，于是有了Uliweb版的simple-todo。接着又有了Bottle版
和Flask版。这俨然成了一个FrameworksShow项目。既然是FrameworksShow，
那Django的总不应当缺了吧。

simple-todo: 一个简易的 todo 程序
http://simple-is-better.com/news/309

Simple Todo (Uliweb 版本) 教程 by @limodou
http://simple-is-better.com/news/312

Simple-TODO Bottle 实现版 by @zoomquiet
http://simple-is-better.com/news/509

Simple-TODO Flask实现版 by @wyattwang
http://simple-is-better.com/news/524

运行需求
========
Django>=1.3

安装及运行
==========

初始化数据库：
python manage.py syncdb

启动：
python manage.py runserver

使用：
在浏览器中打开 http://127.0.0.1:8000/

Django Admin:
在浏览器中打开 http://127.0.0.1:8000/admin/

项目开发记录
============

#. 创建django project和app::

    django-admin.py startproject simple_todo_site
    cd simple_todo_site/
    python manage.py startapp simpletodo

#. 编辑settings.py完成数据库、模板、静态文件等配置，主要配置条目::

    #注：我认为django应当加更多的默认设置，这些配置改的挺烦
    DATABASES
    INSTALLED_APPS
    STATIC_ROOT
    STATICFILES_DIRS
    TEMPLATE_DIRS

#. 编辑urls.py把django admin和static文件url配置加上。

#. 编辑simpletodo/models.py，完成数据模型::

    from django.db import models
    from django.contrib import admin

    class Todo(models.Model):
        title = models.CharField( max_length=255)
        finished = models.IntegerField(default=0)

        def __unicode__(self):
            return self.title

#. 创建数据库::

    python manage.py syncdb

#. 跑起来，进django admin看看先::

    python manage.py runserver
    #http://127.0.0.1:8000/admin/
    
#. 接下来，略...
