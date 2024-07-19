#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/15 上午 11:59
@Author : rovenr32@gmail.com
@File : app.py
"""
import uuid
from datetime import datetime

from sqlalchemy import Column, UUID, String, Text, DateTime, PrimaryKeyConstraint, Index, text

from internal.extension.database_extension import db


class App(db.Model):
    __tablename__ = "app"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_app_id"),
        Index("idx_app_account_id", "account_id")
    )

    id = Column(UUID, default=uuid.uuid4, nullable=False, server_default=text("uuid_generate_v4()"))
    account_id = Column(UUID, nullable=False, server_default=text("'':character varying"))
    name = Column(String(255), nullable=False, server_default=text("'':character varying"))
    icon = Column(String(255), nullable=False, server_default=text("'':text"))
    description = Column(Text, nullable=False, server_default=text("'':character varying"))
    updated_at = Column(DateTime, onupdate=datetime.now, nullable=False,
                        server_default=text("CURRENT_TIMESTAMP(0)"),
                        server_onupdate=text("CURRENT_TIMESTAMP(0)"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP(0)"))
