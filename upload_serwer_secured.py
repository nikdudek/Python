import socket
import datetime
import config
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(config.networkTuple)
s.listen(5)

SIZE = 1
while True:
  client, addr = s.accept()
  print("Connected: " + addr[0])
  data = b''
  
  while not b'\r\n\r\n' in data:
    data += client.recv(SIZE)
  
  size = int((data.split(b'Size:')[1]).split(b'\r\n')[0])
  print(size)
  client.sendall('GO AHEAD\r\n'.encode())
  
  content_lenght = 0
  with open('{0:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now()),'w') as f:
    while content_length < size:
      data = client.recv(SIZE)
      content_length += len(data)
      data = data.decode()
      print('RECEIVED = ' + str((100.0*content_length/size)) + '%')
      f.write(data)
  f.close()
  client.close()
s.close()
