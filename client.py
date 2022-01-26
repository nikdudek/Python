'''
Klient
'''
# coding=utf-8
import socket
import sys

DATA_SIZE = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('localhost', 1769))
    try:
        length = 0
        data_string = ''
        data_string = input("Dane: ") + "\r\n\r\n"
        s.sendall(data_string.encode('utf-8'))

        data = b''
        while not b'\r\n\r\n' in data:
            data += s.recv(DATA_SIZE)

        print(data.decode('utf-8'))

    except KeyboardInterrupt:
        print("Turn-off")
        s.close()

    s.close()
except socket.error:
    print("ERROR")
