from socket import *

# 1.创建套接字
sockfd = socket(family=AF_INET,type=SOCK_STREAM,proto=0)
# 2.绑定ip和端口号
sockfd.bind(('127.0.0.1',8888))
# 3.使套接字具有监听功能
sockfd.listen(5)

while True:
    print("等待客户端连接。。。")
    sc,addr = sockfd.accept()
    print(addr,"已连接")
    while True:
        data = sc.recv(1024)
        if not data:
            break
        print(addr,":",data.decode())
        re = input("回复:")
        sc.send(re.encode())
    sc.close()
sockfd.close()

