#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/13 下午 11:30
@Author : rovenr32@gmail.com
@File : exception.py
"""
from dataclasses import field
from typing import Any

from pkg.response import HttpCode


class CustomException(Exception):
    """Basic custom exception information"""
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = None, data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomException):
    pass


class NotFoundException(CustomException):
    code = HttpCode.NOT_FOUND


class UnauthorizedException(CustomException):
    code = HttpCode.UNAUTHORIZED


class ForbiddenException(CustomException):
    code = HttpCode.FORBIDDEN


class ValidationException(CustomException):
    code = HttpCode.VALIDATE_ERROR
