# 0.安装：pip install fastapi/uvicorn
# 1.导包
from fastapi import FastAPI
from fastapi import Response
import uvicorn

# 2.创建app对象
app = FastAPI()
# 3.创建路由
@app.get('/')
def predict():
    return '跳转首页'

@app.get('/index.html')
def predict():
    return '跳转首页'
@app.get('/favicon.ico')
def predict():
    with open('resource/favicon.ico','rb') as f:
        data = f.read()
    return Response(content=data,media_type='image/x-icon')

uvicorn.run(app,host='0.0.0.0',port=8088)
