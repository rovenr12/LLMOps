#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/9 下午 06:06
@Author : rovenr32@gmail.com
@File : router.py
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """Router"""
    app_handler: AppHandler

    def register_router(self, app: Flask):
        """Register router"""
        # 1. Create a blueprint
        bp = Blueprint('llmops', __name__, url_prefix='')

        # 2. Bind url and controller
        bp.add_url_rule('/ping', view_func=self.app_handler.ping)
        bp.add_url_rule('/app/completion', methods=["POST"], view_func=self.app_handler.completion)
        bp.add_url_rule('/app', methods=["POST"], view_func=self.app_handler.create_app)
        bp.add_url_rule('/app/<uuid:id>', view_func=self.app_handler.get_app)
        bp.add_url_rule('/app/<uuid:id>', methods=["POST"], view_func=self.app_handler.update_app)
        bp.add_url_rule('/app/<uuid:id>/delete', methods=["POST"], view_func=self.app_handler.delete_app)

        # 3. Register blueprint in the application
        app.register_blueprint(bp)
