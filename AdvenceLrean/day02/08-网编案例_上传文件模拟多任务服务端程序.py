import socket

# 创建被动套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip和port
server_socket.bind(('192.168.36.57', 9999))

# 设置监听
server_socket.listen(128)

# 初始的变量
count = 0
while True:
    count += 1  # 累加计数
    try:
        # 接收客户端连接
        server_client_socket, client_addr = server_socket.accept()

        # 以wb模式打开文件, 进行数据存储
        with open(f'data/image{count}.jpg', 'wb') as f:
            while True:
                # 服务端接收客户端发来的数据
                data = server_client_socket.recv(1024)
                # 判断data是否为空, 如果为空, 终止循环
                if len(data) == 0:
                    print('数据已经接收完毕...')
                    break
                f.write(data)

        server_client_socket.close()
    except Exception as e:
        print(e)

server_socket.close()
