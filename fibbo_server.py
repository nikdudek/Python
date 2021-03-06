import asyncio

def fib(n):
   if n == 0: return 0
   elif n == 1:  return 1
   else: return (fib(n-1)+fib(n-2))


class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))
        
        response = str(fib(int(data))).encode()  

        print('Send: {!r}'.format(message))
        self.transport.write(response)

        print('Close the client socket')
        self.transport.close()

loop = asyncio.get_event_loop()

coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 1772)
server = loop.run_until_complete(coro)

print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
