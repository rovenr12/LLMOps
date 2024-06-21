#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/9 下午 06:04
@Author : rovenr32@gmail.com
@File : app_handler.py
"""
import uuid
from dataclasses import dataclass

from injector import inject
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

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

    def debug(self, app_id: uuid.UUID):
        req = CompletionRequest()
        if not req.validate():
            return validate_error_json(req.errors)

        prompt = ChatPromptTemplate.from_template("{query}")
        llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
        parser = StrOutputParser()

        chain = prompt | llm | parser

        content = chain.invoke({"query": req.query.data})

        return success_json({"content": content})

    def ping(self):
        raise FailException("DATA NOT FOUND")
        # return {"ping": "pong"}
