import socket

DATA_SIZE = 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.httpbin.org", 80))
s.sendall("""GET /image/png HTTP/1.1\r\nHost: www.httpbin.org\r\n\r\n""".encode('utf-8'))

data = b''
sum = b''
size = 0

while not b'\r\n\r\n' in sum:
  data = s.recv(DATA_SIZE)
  sum += data

size = int((sum.split(b'Content-Length:')[1]).split(b'\r\n')[0][1:])
headerLen = len(sum)
print(sum[:headerLen].decode())

while len(sum) < size + headerLen:
  data = s.recv(DATA_SIZE)
  sum += data

s.close

outfile = open("image.png", "wb")
outfile.write(sum[headerLen:])
outfile.close()
