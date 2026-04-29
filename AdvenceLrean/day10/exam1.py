import socket as s

client_s = s.socket(s.AF_INET, s.SOCK_STREAM)

client_s.connect(('192.168.108.88', 8000))


data = client_s.recv(1024).decode('utf-8')
print(data)

for i in range(10):
    client_s.send("hello,itheima".encode('utf-8'))

client_s.close()