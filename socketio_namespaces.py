from socketio.namespace import BaseNamespace
import redis
import signal
import json
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)

class ChatNamespace(BaseNamespace):
    def on_chat(self, msg):
        self.emit('chat', msg)
