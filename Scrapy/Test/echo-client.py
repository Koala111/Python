import socket

HOST = '127.0.0.1'  # 服务器的主机名或IP地址
PORT = 65432    # 服务器使用的端口号

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello world')
    data = s.recv(1024)

print('Received', repr(data))
