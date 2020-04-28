#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/28 5:00 下午
# @Author : admin
# @Software: PyCharm
# @File: aio_http_demo1.py

import requests

def hello():
    response = requests.get("http://httpbin.org/get")
    return response

print(hello())
