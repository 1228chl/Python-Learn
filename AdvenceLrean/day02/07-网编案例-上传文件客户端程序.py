import socket as s

client_s = s.socket(s.AF_INET, s.SOCK_STREAM)
client_s.connect(('192.168.36.57', 9999))
with open('D:\\image\\屏幕\\鬼刀\\《鬼刀》海琴烟8k电脑桌面壁纸_花猫壁纸(huamaobizhi.com) (1).jpg', 'rb') as f:
    while True:
        data = f.read(1024)
        if not data:
            print("传输完毕了")
            break
        client_s.send(data)
client_s.close()