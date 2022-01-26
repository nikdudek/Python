#Server
#...
# coding=utf-8
import sys
import socket
import asyncio
from concurrent.futures import ThreadPoolExecutor


def fib(n):
  if n == 0: return 0
  elif n == 1:  return 1
  else: return ( fib(n - 1) + fib(n - 2) )

class FibboServerProtocol(asyncio.Protocol):
  def connection_made(self, transport) -> None:
    self.transport = transport
    self.addr = transport.get_extra_info('peername')
    print('Connection from {}'.format(self.addr))
  
  def data_received(self, data):
    msg = data.decode()
    print("Data received: {}".format(msg))
    task = asyncio.create_task(self.async_fib(int(msg)))
    
  async def async_fib(self,n):
    task = await loop.run_in_executor(thread_pool,fib,n)
    response = str(task).encode() + b'\r\n'
    
    print("Data to send: {}".format(response))
        
    self.transport.write(response)
    self.transport.close()
    
thread_pool = ThreadPoolExecutor()

loop = asyncio.get_event_loop()
coroutine = loop.create_server(FibboServerProtocol,'127.0.0.1',1772)
server = loop.run_until_complete(coroutine)
  
try:
  loop.run_forever()
except KeyboardInterrupt:
  pass
    
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
