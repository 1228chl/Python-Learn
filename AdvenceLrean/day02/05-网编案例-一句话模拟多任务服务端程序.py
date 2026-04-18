"""
1.创建被动套接字  -> 只用于接收客户端发送的请求
2.将服务端程序绑定到服务器上 -> 接收元组类型 (ip, port)
3.设置监听  一般设置5, 可以设置其他的数字
4.接收客户端发来的请求, 如果没有客户端发送请求会处于等待状态  返回一个元组 (服务端数据传输的套接字, 客户端地址信息)
5.发送数据  服务端向客户端发送
6.接收数据  服务端接收客户端发来的数据
7.关闭套接字
"""
import socket as s
server_s = s.socket(s.AF_INET, s.SOCK_STREAM)
server_s.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, True)
server_s.bind(('192.168.36.67',8888))
server_s.listen(5)
print('等待客户端连接中。。。')
while True:
    try:
        server_c_s,client_addr = server_s.accept()
        print("客户端已连接。。。")
        print("客户端地址",client_addr)
        server_c_s.send('ni hao'.encode('utf-8'))
        print('服务端接收到的数据：',server_c_s.recv(1024).decode('utf-8'))
        server_c_s.close()
    except Exception as e:
        print(e)
server_s.close()
