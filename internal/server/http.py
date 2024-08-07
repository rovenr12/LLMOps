#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/9 下午 06:13
@Author : rovenr32@gmail.com
@File : http.py
"""
import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config
from internal.exception import CustomException
from internal.router import Router
from pkg.response import Response, json, HttpCode
from pkg.sqlalchemy import SQLAlchemy


class Http(Flask):
    """Http server engine"""

    def __init__(self, *args, conf: Config, db: SQLAlchemy, migrate: Migrate, router: Router, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialise application setting
        self.config.from_object(conf)

        # Register exception handler
        self.register_error_handler(Exception, self._register_error_handler)

        db.init_app(self)
        migrate.init_app(self, db, directory="internal/migration")

        CORS(self, resources={
            r"/*": {
                "origins": "*",
                "supports_credentials": True,
            }
        })

        # Register application router
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {}
            ))

        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise error

        return json(Response(
            code=HttpCode.FAIL,
            message=str(error),
            data={}
        ))
