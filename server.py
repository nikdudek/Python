'''
Serwer
'''
# coding=utf-8
import socket
import sys
import datetime
import os

DATA_SIZE = 1

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost", 1769))
s.listen(1)

try:
    while True:

        data_all = b""
        client, addr = s.accept()
        print("Connected: " + addr[0] + ' at ' + datetime.datetime.now().strftime('%H:%M:%S'))
        data = "cos"

        while not b"\r\n\r\n" in data_all:
            data = client.recv(DATA_SIZE)
            print("Downloaded: %s\n" % (data.decode('utf-8')))
            data_all += data

        print(f'WHOLE MSG: {data_all.decode("utf-8")}')
        client.sendall("UDALO SIE\r\n\r\n".encode('utf-8'))
        client.close()
    s.close()
except KeyboardInterrupt:
    s.close()
