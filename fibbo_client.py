# coding=utf-8
import socket
import ssl


try:

    with socket.create_connection(('localhost', 1772)) as ssock:
        ssock.sendall('5'.encode())
        data_all = []
        data = 'nothing'
        while data:
            data = ssock.recv(1)
            data_all.append(data)
        data = b''.join(i for i in data_all)
        print ('I receive = ' + data.decode())

except socket.error:
    print ('Error')
