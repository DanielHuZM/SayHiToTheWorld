# -*- coding:utf-8 -*-
"""
    Author:Daniel Hu @SHU
    Datetime:2019/6/5 15:26
    Software: PyCharm
"""
from flask import render_template, url_for, flash, redirect

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    # 时间降序排列 desc=descending
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
