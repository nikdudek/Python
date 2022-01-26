import socket

DATA_SIZE = 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.httpbin.org", 80))
s.sendall("""GET /html HTTP/1.1\r\nHost: www.httpbin.org\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A)\r\n\r\n""".encode())

data = b''
sum = b''
size = 0

while not b'\r\n\r\n' in sum:
  data = s.recv(DATA_SIZE)
  sum += data

size = int((sum.split(b'Content-Length:')[1]).split(b'\r\n')[0][1:])
headerLen = len(sum.split(b'\r\n\r\n')[0]) + 4
print(headerLen)

while len(sum) < size + headerLen:
  data = s.recv(DATA_SIZE)
  sum += data

s.close

sum = sum.decode()
print(sum)

index = sum.find('<html')
content = sum[index:]

text_file = open("index.html", "w+")
text_file.write(content)
text_file.close()
