"""
套接字是进程之间数据传输的载体
客户端和服务器端分别有自己的套接字 ->两个人打电话，需要两部手机
客户端：C端用户的设备上：客户端程序
服务端：使用的软件所属公司的设备上：服务端程序

服务端程序有2个套接字
客户端程序有1个套接字
"""
# 导包
import socket

# 创建套接字对象
# family：ip地址类型 AF_INET:IPv4 AF_INET6:IPv6
# type：socket类型/协议类型 SOCK_STREAM:TCP协议 SOCK_DGRAM:UDP协议
st = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
print('st--->',st)
