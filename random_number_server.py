'''
Serwer Proxy
'''
# coding=utf-8
import random
import socket
import time
import datetime
import os
import _thread
import threading

DATA_SIZE = 1024

def receive_data(client, ending):
  data = b''
  while ending not in data:
    data += client.recv(DATA_SIZE)
  return data

def receive_html(client):
  data = b''
  size = 2000000
  
  while True:
    data += client.recv(DATA_SIZE)
    if len(data.split(b'Content-Length:')) > 1 and len((data.split(b'Content-Length:')[1]).split(b'\r\n')
      size = int((data.split(b'Content-Length:')[1]).split(b'\r\n')[0][1:])
    
    if len(data.split(b'\r\n\r\n')) > 1 and len(data.split(b'\r\n\r\n')[1]) >= size:
      break
  return data


def one_client(client):
  proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  proxy.connect(("www.httpbin.org", 80))
  
  print(repr(client))
  data = receive_data(client, b'\r\n\r\n')
  print(data)
  proxy.sendall(data)
  
  data = receive_html(proxy)
  client.sendall(data)
  
  proxy.close()
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 1770))
s.listen(5)
try:
  while True:
    client, addr = s.accept()
    print("Connected: " + addr[0] + ' at ' + datetime.datetime.now().strftime('%H:%M:%S'))
    start_new_thread(one_client, (client, ))

except KeyboardInterrupt:
  s.close()
s.close()
