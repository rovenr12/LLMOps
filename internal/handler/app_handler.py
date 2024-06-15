#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/9 下午 06:04
@Author : rovenr32@gmail.com
@File : app_handler.py
"""
import os
import uuid
from dataclasses import dataclass

from flask import request
from injector import inject
from openai import OpenAI

from internal.exception import FailException
from internal.schema.app_schema import CompletionRequest
from internal.service import AppService
from pkg.response import success_json, validate_error_json, success_message


@inject
@dataclass
class AppHandler:
    """Application Controller"""
    app_service: AppService

    def create_app(self):
        app = self.app_service.create_app()
        return success_message(f"The app was successfully created, id: {app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"The app was successfully retrieved, name: {app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"The app was successfully modified, name: {app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"The app was successfully deleted, id: {app.id}")

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
