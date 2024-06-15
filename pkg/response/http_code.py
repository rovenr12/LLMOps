#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/12 下午 11:23
@Author : rovenr32@gmail.com
@File : http_code.py
"""
from enum import Enum


class HttpCode(str, Enum):
    """HTTP Basic Status Codes"""
    SUCCESS = "success"
    FAIL = "fail"
    NOT_FOUND = "not found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    VALIDATE_ERROR = "validate_error"
