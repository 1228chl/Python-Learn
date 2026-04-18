import socket


# 点对点发送
# # AF_INET: ipv4地址  SOCK_DGRAM:UDP协议
# udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # 飞秋服务器地址和端口号
# server = ('192.168.36.57', 2425)
# # 消息内容
# content = '1:134871264:川建国:黑马程序员:32:今天周六，股市休市，继续打伊朗！'
# # sendto():发送消息  注意:编码是gbk
# udp_client_socket.sendto(content.encode('gbk'), server)


# 群发
import socket

# AF_INET: ipv4地址  SOCK_DGRAM:UDP协议
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# TODO 设置广播SO_BROADCAST
udp_client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# 飞秋服务器地址和端口号
server = ('192.168.36.57', 2425)
# 消息内容
content = '1:134871264:川建国:黑马程序员:32:今天周六，股市休市，继续打伊朗！'
# sendto():发送消息  注意:编码是gbk
udp_client_socket.sendto(content.encode('gbk'), server)