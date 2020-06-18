import socket
import _thread
import time
from datetime import datetime

ip = '192.168.2.20'
port = 6666


def on_new_client(client_socket, addr):
    try:
        with client_socket:
            data = client_socket.recv(1024)
            date_obj = datetime.now()
            current_time = (str(date_obj.hour) + ':' + str(date_obj.minute) + ':' + str(date_obj.second))
            print(f'Message: {data} from {addr}')
            client_socket.send(bytes(current_time, encoding='utf-8'))
    except Exception as e:
        print(e)


# Creacion de sockets con protocolo TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    print(f'Starting server on {ip} port {port}')
    # Asignacion de IP y Puerto al socket
    sock.bind((ip, port))
    # El socket esta escuchando
    sock.listen(5)
    while True:
        print('Waiting for connection!')
        connection, client_address = sock.accept()
        try:
            print(f'Client connected: {client_address}')
            # Si se detecta una nueva conexion, se creara un hilo que procese dicha informacion
            _thread.start_new_thread(on_new_client, (connection, client_address))
            time.sleep(1)

        except Exception as e:
            print(e)
