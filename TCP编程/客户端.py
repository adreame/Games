import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8888))
print(s.recv(1024).decode('utf-8'))
while True:
# for data in [b'mical',b'decod',b'print']:
    data = input('请输入传输数据：')
    s.send(data.encode())
    if data == 'exit' or data == '':
        break
    print(s.recv(1024).decode('utf-8'))

s.close()
