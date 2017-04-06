#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    :  Jason
# @Mail      :  jczhangmail@126.com
# @File      :  a.py

from flask import Blueprint,render_template

#定义一个蓝图
bp = Blueprint('user',__name__,url_prefix='/a',template_folder='./template')

@bp.route('/')
def user():
    return render_template('user.html')
