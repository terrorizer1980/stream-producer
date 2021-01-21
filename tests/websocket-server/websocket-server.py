#! /usr/bin/env python3

from simple_websocket_server import WebSocketServer, WebSocket


class SimpleEcho(WebSocket):

    def __init__(self):
        self.counter = 0

    def handle(self):
        # echo message back to client
        self.counter += 1
        print(self.counter)
#         self.send_message(self.data)

    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')


server = WebSocketServer('127.0.0.1', 8000, SimpleEcho)
server.serve_forever()
