# Server
# ...
# coding=utf-8
import socket
import ssl
from _thread import start_new_thread


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def one_client(client):
    data_all = b''

    while b'\r\n' not in data_all:
        data = client.recv(1)
        data_all += data

    data = data_all.decode()
    print("RECEIVED ", data)
    response = (str(fib(int(data[:-2]))) + '\r\n').encode()

    client.sendall(response)
    client.close()


def create_ssl_context():
    cont = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    cont.verify_mode = ssl.CERT_REQUIRED
    cont.load_cert_chain(certfile='server.crt', keyfile='server.key')
    cont.load_verify_locations(cafile='../client.crt')
    return cont


context = create_ssl_context()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(("localhost", 1772))
    sock.listen(5)
    with context.wrap_socket(sock, server_side=True) as ssock:
        while True:
            try:
                conn, addr = ssock.accept()
                print("Connected: " + addr[0])
                start_new_thread(one_client, (conn,))
            except socket.error:
                ssock.close()

