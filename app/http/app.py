#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/9 下午 06:16
@Author : rovenr32@gmail.com
@File : app.py
"""
import dotenv
from flask_migrate import Migrate
from injector import Injector

from config import Config
from internal.router import Router
from internal.server import Http
from pkg.sqlalchemy import SQLAlchemy
from .module import ExtensionModule

dotenv.load_dotenv()
conf = Config()
injector = Injector([ExtensionModule])

app = Http(__name__, router=injector.get(Router),
           conf=conf, db=injector.get(SQLAlchemy), migrate=injector.get(Migrate))

if __name__ == '__main__':
    app.run(debug=True)
