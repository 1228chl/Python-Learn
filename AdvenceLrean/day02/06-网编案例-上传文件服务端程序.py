import socket as s

server_s = s.socket(s.AF_INET, s.SOCK_STREAM)
server_s.bind(('127.0.0.1', 8899))
server_s.listen(5)
server_c_s,client_addr = server_s.accept()
with open('data/server.txt','wb')as f:
    while True:
        data = server_c_s.recv(1024)
        if not data:
            print("数据已经传输完毕")
            break
        f.write(data)
server_c_s.close()
server_s.close()