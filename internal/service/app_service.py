#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/15 下午 10:31
@Author : rovenr32@gmail.com
@File : app_service.py
"""
import uuid
from dataclasses import dataclass

from injector import inject

from internal.model import App
from pkg.sqlalchemy import SQLAlchemy


@inject
@dataclass
class AppService:
    db: SQLAlchemy

    def create_app(self) -> App:
        with self.db.auto_commit():
            app = App(name="測試機器人", icon="", account_id=uuid.uuid4(),
                      description="這是一個簡單的聊天機器人")
            self.db.session.add(app)
        return app

    def get_app(self, id: uuid.UUID) -> App:
        app = self.db.session.query(App).get(id)
        return app

    def update_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit():
            app = self.get_app(id)
            app.name = "Judy聊天機器人"
        return app

    def delete_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit():
            app = self.get_app(id)
            self.db.session.delete(app)
        return app
