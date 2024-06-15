#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/15 上午 10:50
@Author : rovenr32@gmail.com
@File : test_app_handler.py
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:
    @pytest.mark.parametrize("query", [None, "Hi, Who are you?"])
    def test_completion(self, query, client):
        response = client.post("/app/completion", json={"query": query})
        assert response.status_code == 200
        if query is None:
            assert response.json.get("code") == HttpCode.VALIDATE_ERROR
        else:
            assert response.json.get("code") == HttpCode.SUCCESS
