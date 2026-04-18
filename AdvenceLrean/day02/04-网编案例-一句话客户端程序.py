"""
1.创建套接字 -> 客户端数据传输的套接字
"""
import socket as s
# 1.创建套接字 -> 客户端数据传输的套接字
client_s = s.socket(s.AF_INET, s.SOCK_STREAM)
# 2.连接服务端程序，服务端的ip和port
# client_s.connect(('192.168.36.57', 8888))
client_s.connect(('192.168.36.57', 8888))

# 3.接收服务端发来的数据
data = client_s.recv(1024).decode('utf-8')
print(data)
# 4.发送数据给服务端
for i in range(10):
    client_s.send("张键烨是天才".encode('utf-8'))
    client_s.send("伍锦滨也是天才".encode('utf-8'))
# 5.关闭连接
client_s.close()