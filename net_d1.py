import socket

# 获取主机名
localhost = socket.gethostname()
print("主机名：",localhost)

# 通过主机名解析IP
print("通过主机名解析IP:")
print(socket.gethostbyname('Tarena-PC'))
print(socket.gethostbyname('localhost'))

# gethostbyaddr()方法
print("gethostbyaddr()方法:")
# print(socket.gethostbyaddr("www.baidu.com"))

print("ip地址 --> 二进制:")
print(socket.inet_aton("192.168.1.2"))
print(socket.inet_pton(socket.AF_INET,"192.168.1.2"))  # AF_INET 或AF_INET6

print("二进制转十进制：")
print(socket.inet_ntoa(b'\xc0\xa8\x01\x02'))
print(socket.inet_ntop(socket.AF_INET ,b'\xc0\xa8\x01\x02'))

print("获取一个应用的端口：")
# print(socket.getservbyname('mysql'))
# print(socket.getservbyport(3306))

s = socket.socket()

print("获取套接字描述符：")
print(s.fileno())

print("获得套接字类型：")
print(s.type)

print("获取套接字绑定的地址：")
# print(s.getsockname())

print("使用accept生成的套接字调用，获取该套接字对应的客户端的地址：")
print(s.getpeername())
