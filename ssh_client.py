# Client
# ...
# coding=utf-8
import socket
import ssl

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile='venv/server.crt')
context.load_cert_chain(certfile='client.crt', keyfile='client.key')

try:
    with socket.create_connection(('localhost', 1772)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as s:
            print(s.version())
            number = input("Enter a number: ") + '\r\n'
            s.sendall(number.encode())
            data = b'0'
            data_all = b''
            while b'\r\n' not in data_all:
                data = s.recv(1024)
                data_all += data
            data = data_all.decode()
            print('I receive = ' + data)
            s.close()

except socket.error:
    print('Error')

