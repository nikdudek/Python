#Client
#...
# coding=utf-8
import socket
import ssl

try:
    with socket.create_connection(('127.0.0.1', 1772)) as s:
        number = input("Enter a number: ") + '\r\n'
        s.sendall(number.encode())
        data = b'0'
        data_all = b''
        while b'\r\n' not in data_all:
            data = s.recv(1)
            data_all += data
        data = data_all.decode()
        print ('I receive = ' + data)

except socket.error:
    print ('Error')
