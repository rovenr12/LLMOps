#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/13 下午 11:09
@Author : rovenr32@gmail.com
@File : response.py
"""
from dataclasses import field, dataclass
from typing import Any

from flask import jsonify

from .http_code import HttpCode


@dataclass
class Response:
    """Basic HTTP interface response format"""
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    """Basic response interface"""
    return jsonify(data), 200


def success_json(data: Any = None):
    """Success data response"""
    return json(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Any = None):
    """Fail data response"""
    return json(Response(code=HttpCode.FAIL, message="", data=data))


def validate_error_json(errors: dict = None):
    """Validation error response"""
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ""
    return json(Response(code=HttpCode.VALIDATE_ERROR, message=msg, data=errors))


def message(code: HttpCode = None, msg: str = ""):
    """Basic message response, only return message"""
    return json(Response(code=code, message=msg, data={}))


def success_message(msg: str = ""):
    """success message response, only return message"""
    return message(code=HttpCode.SUCCESS, msg=msg)


def fail_message(msg: str = ""):
    """fail message response, only return message"""
    return message(code=HttpCode.FAIL, msg=msg)


def not_found_message(msg: str = ""):
    """not found message response, only return message"""
    return message(code=HttpCode.NOT_FOUND, msg=msg)


def unauthorized_message(msg: str = ""):
    """unauthorized message response, only return message"""
    return message(code=HttpCode.UNAUTHORIZED, msg=msg)


def forbidden_message(msg: str = ""):
    """success message response, only return message"""
    return message(code=HttpCode.FORBIDDEN, msg=msg)
