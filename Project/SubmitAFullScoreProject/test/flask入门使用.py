# 0.安装：pip install flask
# 1.导包
from flask import Flask
# 2.创建对象
app = Flask(__name__)

# 3.使用对象接收web请求，并给出响应结果
@app.route('/',methods=['GET'])
def predict1():
    # 根据请求资源路径，获取对应的资源并返回
    return '跳转到首页'

# 4.启动服务
app.run(host='0.0.0.0',port=8888,debug=True)
