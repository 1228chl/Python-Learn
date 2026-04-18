"""
1.创建被动套接字  -> 只用于接收客户端发送的请求
2.将服务端程序绑定到服务器上 -> 接收元组类型 (ip, port)
3.设置监听  一般设置5, 可以设置其他的数字
4.接收客户端发来的请求, 如果没有客户端发送请求会处于等待状态  返回一个元组 (服务端数据传输的套接字, 客户端地址信息)
5.发送数据  服务端向客户端发送
6.接收数据  服务端接收客户端发来的数据
7.关闭套接字
"""
import socket

# 1.创建被动套接字  -> 只用于接收客户端发送的请求
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.将服务端程序绑定到服务器上 -> 接收元组类型 (ip, port)
server_socket.bind(('127.0.0.1', 8888))

# 3.设置监听  一般设置5, 可以设置其他的数字
# backlog: 监听的最大设备数, 超过后就需要排队等待
server_socket.listen(5)

print('等待客户端连接中...')
# 4.接收客户端发来的请求, 如果没有客户端发送请求会处于等待状态  返回一个元组 (服务端数据传输的套接字, 客户端地址信息)
# server_client_socket: 此套接字用于服务端的数据传输
server_client_socket, client_addr = server_socket.accept()
print('客户端已连接...')
print('客户端地址:', client_addr)

# 5.发送数据  服务端向客户端发送
server_client_socket.send('你好!'.encode('utf-8'))

# 6.接收数据  服务端接收客户端发来的数据
data = server_client_socket.recv(1024).decode('utf-8')
print('服务端接收到的数据:', data)

# 7.关闭套接字
server_client_socket.close()
server_socket.close()  # 一般不关闭, 服务端程序就停止了
