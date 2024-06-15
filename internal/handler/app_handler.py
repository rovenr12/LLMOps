#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/9 下午 06:04
@Author : rovenr32@gmail.com
@File : app_handler.py
"""
import os

from flask import request
from openai import OpenAI

from internal.exception import FailException
from internal.schema.app_schema import CompletionRequest
from pkg.response import success_json, validate_error_json


class AppHandler:
    """Application Controller"""

    def completion(self):
        req = CompletionRequest()
        if not req.validate():
            return validate_error_json(req.errors)

        # extract input from interface
        query = request.json.get("query")
        # build OpenAPI client, and send request
        client = OpenAI(base_url=os.getenv("OPENAI_API_BASE"))
        # get request response and send response to front-end
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role": "system",
                    "content": "You are a chat robot developed by OpenAI, please response based on the user input"
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
        )

        content = completion.choices[0].message.content

        return success_json({"content": content})

    def ping(self):
        raise FailException("DATA NOT FOUND")
        # return {"ping": "pong"}
