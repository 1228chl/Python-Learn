import socket as s

client_s = s.socket(s.AF_INET,s.SOCK_STREAM)
client_s.connect(('127.0.0.1',8888))
client_s.send('data'.encode('utf-8'))
client_s.close()

server_s = s.socket(s.AF_INET,s.SOCK_STREAM)
server_s.bind(('127.0.0.1',8888))
server_s.listen()
server_c_s,client_addr = server_s.accept()
data = server_c_s.recv(1024).decode('utf-8')
server_c_s.close()
server_s.close()

