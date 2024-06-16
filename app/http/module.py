#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/15 上午 11:51
@Author : rovenr32@gmail.com
@File : module.py
"""
from flask_migrate import Migrate
from injector import Module, Binder

from internal.extension.database_extension import db
from internal.extension.migrate_extension import migrate
from pkg.sqlalchemy import SQLAlchemy


class ExtensionModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)
