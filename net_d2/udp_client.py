from socket import *

ADDR = ("127.0.0.1",9999)
BUFFERSIZE = 1024

sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    sd = input("发送：")
    sockfd.sendto(sd.encode(),ADDR)
    data,addr = sockfd.recvfrom(BUFFERSIZE)
    print("接收：",data.decode())
sockfd.close()