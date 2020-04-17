#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/18 3:00
# @Author : Tom_tao
# @Site : 
# @File : demo01.py
# @Software: PyCharm

from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
async def main():
    return {"msg":"HelloWorld,FastAPI"}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)