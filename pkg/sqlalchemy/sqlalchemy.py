#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/15 下午 11:17
@Author : rovenr32@gmail.com
@File : sqlalchemy.py
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
