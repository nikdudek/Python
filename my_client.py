#klient
import socket, pickle, sys

class Klasa:
	id = 0
	data = 0
	other = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

data = Klasa()
data_string = pickle.dumps(data)

try:
    s.connect(('localhost', 1769))
    while True:
        s.send(data_string)
        data = s.recv(1024)
        if not data:
            break

    s.close()
except socket.error:
    print ('Error')
