import socket

# 1. 创建 UDP 套接字 (SOCK_DGRAM 表示 UDP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 绑定地址和端口 ('0.0.0.0' 表示监听所有网卡)
server_socket.bind(('0.0.0.0', 9999))

print("UDP 服务端已启动，监听端口 9999...")

while True:
    # 3. 接收数据 (recvfrom 会返回数据和客户端地址)
    data, client_addr = server_socket.recvfrom(1024)

    # 解码并打印
    text = data.decode('utf-8')
    print(f"收到来自 {client_addr} 的消息: {text}")

    # 4. 发送响应给该客户端
    response = f"服务端已收到: {text}".encode('utf-8')
    server_socket.sendto(response, client_addr)