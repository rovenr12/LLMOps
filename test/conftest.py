#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/15 上午 10:55
@Author : rovenr32@gmail.com
@File : conftest.py
"""
import pytest

from app.http.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
