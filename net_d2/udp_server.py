from socket import *

ADDR = ("127.0.0.1",9999)
buffersize = 1024

sockfd = socket(AF_INET,SOCK_DGRAM,0)
sockfd.bind(ADDR)
while True:
    data,addr = sockfd.recvfrom(buffersize)
    print(addr,":",data.decode())
    sd = input("回复：")
    sockfd.sendto(sd.encode(),addr)
sockfd.close()
