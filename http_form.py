import socket

DATA_SIZE = 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.httpbin.org", 80))
s.sendall("""POST /post HTTP/1.1\r\nHost: www.httpbin.org\r\nAccept: *\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 176\r\ncustname=Dominik&custtel=789456123&custemail=dominikdudek%40poczta.pl&size=large&topping=cheese&topping=onion&topping=mushroom&delivery=17%3A00&comments=number+6+with+extra+dip\r\n\r\n""".encode('utf-8'))

data = b''
sum = b''
size = 0

while not b'\r\n\r\n' in sum:
  data = s.recv(DATA_SIZE)
  sum += data

size = int((sum.split(b'Content-Length:')[1]).split(b'\r\n')[0][1:])
headerLen = len(sum)
print("Header: ",sum[:headerLen].decode())

while len(sum) < size + headerLen:
  data = s.recv(DATA_SIZE)
  sum += data

print("Response: ",sum[headerLen:].decode())

s.close

