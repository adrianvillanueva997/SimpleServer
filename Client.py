import socket

ip = '192.168.2.20'
port = 6666

while True:
    # Establecer conexion TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        print(f'connecting to {ip} port {port}')
        message = b'Cliente 1'
        print(f'sending {message}')
        sock.sendall(message)
        data = sock.recv(1024)
        print(data)
