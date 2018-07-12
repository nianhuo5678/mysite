# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import time


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        for i in range(10):
            self.send(str(i))
            time.sleep(1)

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        self.send(text_data)

