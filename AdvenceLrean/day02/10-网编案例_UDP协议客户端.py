import socket

# 1. 创建 UDP 套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 服务端地址
server_addr = ('127.0.0.1', 9999)

# 3. 发送消息 (sendto 需要指定目标地址)
message = "Hello, UDP!".encode('utf-8')
client_socket.sendto(message, server_addr)
print(f"已发送: {message.decode('utf-8')}")

# 4. 接收服务端响应
data, addr = client_socket.recvfrom(1024)
print(f"收到回复: {data.decode('utf-8')}")

# 5. 关闭套接字
client_socket.close()