# -*- coding:utf-8 -*-
"""
    Author:Daniel Hu @SHU
    Datetime:2019/6/5 15:06
    Software: PyCharm
"""

import os

from sayhello import app

#
dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
