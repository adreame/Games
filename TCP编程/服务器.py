#TCP服务器编程
import socket
import threading
import time
def tcplink(sock,addr):
    print('接收一个来自%s:%s连接请求'%addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        #time.sleep(1)
        print(data.decode('utf-8'))
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('你好, %s!'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('来自%s:%s连接关闭'%addr)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8888))
s.listen(5)
print('等待客户端连接。。。')
while True:
    sock,addr = s.accept()
    print('sock:',sock)
    t = threading.Thread(target = tcplink,args = (sock,addr))
    t.start()