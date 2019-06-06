# -*- coding:utf-8 -*-
"""
    Author:Daniel Hu @SHU
    Datetime:2019/6/5 15:36
    Software: PyCharm
"""

from sayhello import db
from datetime import datetime


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    # Note : not datatime.now(),否则将在加载模块时就被执行，不是正确的时间戳
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
