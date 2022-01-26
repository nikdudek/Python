import socket
import time

DATA_SIZE = 1

sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(1000)]
for sock in sockets:
  while True:
    sock.connect(("www.mattkozlowski.pl", 80))
    sock.sendall("""GET  HTTP/1.1\r\nHost: https://www.mattkozlowski.pl\r\n\r\n""".encode('utf-8'))
    data = b''
    while not b'\r\n\r\n' in data:
      data += sock.recv(DATA_SIZE)
    print(data.decode('utf-8'))
    time.sleep(100)

for sock in sockets:
  sock.close
