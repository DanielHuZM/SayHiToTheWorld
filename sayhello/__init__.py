# -*- coding:utf-8 -*-
"""
    Author:Daniel Hu @SHU
    Datetime:2019/6/5 14:45
    Software: PyCharm
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
# 测试Debug调用
# from flask_debugtoolbar import DebugToolbarExtension

# 1. 创建实例 2.加载配置 3.初始化扩展
app = Flask('sayhello')
app.config.from_pyfile('settings.py')
# 去除jinja模板中的多余空格
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
# 测试DEBUG调用
# toolbar = DebugToolbarExtension(app)
# DEBUG_TB_INTERCEPT_REDIRECTS = False

# 注册视图函数和错误函数，避免循环依赖，因此放末尾定义
from sayhello import views, errors, commands
