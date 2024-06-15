#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/11 下午 10:14
@Author : rovenr32@gmail.com
@File : config.py
"""
import os
from typing import Any

from .default_config import DEFAULT_CONFIG


def _get_env(key: str) -> Any:
    """Get environment variable, if not found, return default"""
    return os.environ.get(key, DEFAULT_CONFIG.get(key))


def _get_bool_env(key: str) -> Any:
    """Get boolean environment variable"""
    value: str = _get_env(key)
    return value.lower() == "true" if value is not None else False


class Config:
    def __init__(self):
        self.WTF_CSRF_ENABLED = _get_bool_env("WTF_CSRF_ENABLED")

        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URL")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env("SQLALCHEMY_POOL_SIZE")),
            "pool_recycle": int(_get_env("SQLALCHEMY_POOL_RECYCLE")),
        }
        self.SQLALCHEMY_ECHO = _get_env("SQLALCHEMY_ECHO")
