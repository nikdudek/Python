#serwer
import socket, pickle

class Klasa:
    id = 0
    data = 0
    other = 0

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost", 1769))
s.listen(5)

while True:
    client, addr = s.accept()
    print("Connected: " + addr[0])

    while True:
        data = client.recv(4096)
        if not data:
            break;

    data_var = pickle.loads(data)
    print(data_var)
    
    client.close()

s.close()
