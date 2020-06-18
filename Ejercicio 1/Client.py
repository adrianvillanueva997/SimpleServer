import socket

ip = '192.168.2.20'
port = 6666

# Establecer conexion TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    while True:
        sock.connect((ip, port))
        print(f'connecting to {ip} port {port}')
        message = b'Cliente 1'
        sock.sendall(message)
        data = sock.recv(1024)
        print(data)
