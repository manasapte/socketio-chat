from flask import Flask, render_template, request, session, abort, jsonify
from socketio_namespaces import ChatNamespace
from socketio import socketio_manage
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/socket.io/<path:rest>')
def push_stream(rest):
    try:
        socketio_manage(request.environ, {'/chat' : ChatNamespace}, request)
    except:
        app.logger.error("Exception while handling socketio connection",
                     exc_info=True)
