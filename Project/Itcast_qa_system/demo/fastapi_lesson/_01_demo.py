#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Vincent
@Time    : 2026/6/27 14:56
@File    : _01_demo.py
@Function :
"""
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


# 定义GET方法
# 输入参数空
# json {"message": "Hello World"}
@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):  # item_id 是路径参数，q 是可选查询参数
    return {"item_id": item_id, "q": q}


class UserInput(BaseModel):
    text: str


def predict(text):
    # load model
    return "体育"


@app.post("/bert/predict")
def handle_text(user_input: UserInput):
    label = predict(user_input.text)
    return {"result": {"label": label, "text": user_input.text}}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=12123)
