#Server
#...
# coding=utf-8
import socket
import _thread

def fib(n):
    if n < 0:
        return("Incorrect number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))


def one_client(client):
    data_all = b''
    data = b'0'
    
    while b'\r\n' not in data_all:
        data = client.recv(1)
        data_all += data
    
    data = data_all.decode()
    response = (str(fib(int(data[:-2]))) + '\r\n').encode
    
    client.sendall(response)
    client.close()
    
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",1768))
s.listen(5)

while True:
    client, addr = s.accept()
    print("Connected: " + addr[0])
    start_new_thread(one_client, (client, ))

s.close()
