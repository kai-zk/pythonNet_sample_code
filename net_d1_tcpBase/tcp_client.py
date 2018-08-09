from socket import *

sockfd = socket(family=AF_INET,type=SOCK_STREAM,proto=0)

conn = sockfd.connect(('127.0.0.1',8888))
while True:
    msg = input("发送：")
    sockfd.send(msg.encode())

    data = sockfd.recv(1024)
    print("回话：",data.decode())

sockfd.close()