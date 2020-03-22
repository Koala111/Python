import socket

HOST = '127.0.0.0'  # 标准的回环地址
PORT = 65432    # 监听的端口

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # (因特网IPv4地址族， TCP的socket类型，协议将被用来 在网络中传输消息))
    s.bind(HOST, PORT)  # 关联socket到指定的网络接口
    s.listen()
    conn, addr = s.accept() # 阻塞 并等待传入连接
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
