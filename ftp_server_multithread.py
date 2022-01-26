'''
Serwer
'''
# coding=utf-8
import socket
import sys
import datetime
import os

DATA_SIZE = 1

def one_client(client):
	
	data_all = b""
	data = ""
	while not b"\r\n\r\n" in data_all:
		data = client.recv(DATA_SIZE)
		data_all += data
	data_all = data_all.decode('utf-8')
	data_all.replace('\r\n\r\n', '')
	
	try:
    		f = open(data_all)
	except FileNotFoundError:
    		print("Nie ma takiego pliku")
	else:
		try:
    			s2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s2.bind(("localhost", 0))
			s2.listen(DATA_SIZE)
			port = s2.getsockname()[1] + '\r\n\r\n'
			client.sendall(port.encode('utf-8'))
			data_to_send = b''
			while True:
				client2, addr2 = s2.accept()
				print("Connected to FTP: " + addr[0] + ' at ' + datetime.datetime.now().strftime('%H:%M:%S'))
				while True:
					file_read = f.read(DATA_SIZE)
					if not file_read:
						break
					data_to_send += file_read
				data_to_send += '\r\n\r\n'
				client2.sendall(data_to_send.encode('utf-8'))
				client2.close()
			s2.close()
		except KeyboardInterrupt:
			s2.close
	finally:
	    	f.close()
	client.close()
	
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost", 1769))
s.listen(DATA_SIZE)

try:
	while True:

	client, addr = s.accept()
	print("Connected: " + addr[0] + ' at ' + datetime.datetime.now().strftime('%H:%M:%S'))
	start_new_thread(one_client, (client, ))

s.close()
except KeyboardInterrupt:
    s.close()
