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
		data_string = ''
		data_string = input("Dane: ") + "\r\n\r\n"
		s.sendall(data_string.encode('utf-8'))

		port = b''
		while not b'\r\n\r\n' in port:
			port += s.recv(DATA_SIZE)
		port.replace('\r\n\r\n', '')
		s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
        		s2.connect(('localhost', port.decode('utf-8')))
        		print("Connected to FTP\n")
        		data_recived = b''
			while not b'\r\n\r\n' in data_recived:
        			data_recived = s2.recv(DATA_SIZE)
        		data_recived.replace('\r\n\r\n', '')
        		print(data_recived.decode('utf-8'))
        	except socket.error:
        		print("ERROR")
        s2.close()

	except KeyboardInterrupt:
		print("Turn-off")
		s.close()

	s.close()
except socket.error:
	print("ERROR")
