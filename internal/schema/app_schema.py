#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/11 下午 10:10
@Author : rovenr32@gmail.com
@File : app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionRequest(FlaskForm):
    query = StringField("query", validators=[
        DataRequired(message="the query is required"),
        Length(max=2000, message="the query maximum length is 2000")
    ])
