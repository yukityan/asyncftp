# import asyncio
#
#
# class EchoClientProtocol(asyncio.Protocol):
#     def __init__(self, message, on_con_lost, loop):
#         self.message = message
#         self.loop = loop
#         self.on_con_lost = on_con_lost
#
#     def connection_made(self, transport):
#         transport.write(self.message.encode())
#         print('Data sent: {!r}'.format(self.message))
#
#     def data_received(self, data):
#         print('Data received: {!r}'.format(data.decode()))
#
#     def connection_lost(self, exc):
#         print('The server closed the connection')
#         self.on_con_lost.set_result(True)
#
#
# async def main():
#     # Get a reference to the event loop as we plan to use
#     # low-level APIs.
#     loop = asyncio.get_running_loop()
#
#     on_con_lost = loop.create_future()
#     message = 'Hello World!'
#
#     transport, protocol = await loop.create_connection(
#         lambda: EchoClientProtocol(message, on_con_lost, loop),
#         '127.0.0.1', 8888)
#
#     # Wait until the protocol signals that the connection
#     # is lost and close the transport.
#     try:
#         await on_con_lost
#     finally:
#         transport.close()


import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.run(tcp_echo_client('Hello World!'))
