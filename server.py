import circle_detection as bd
import os

from flask import Flask
from flask import send_file
from flask import g

app = Flask(__name__)


# decorator to run a function after ball detection response is formed
def after_bd_response(fn):
    if not hasattr(g, 'call_after_bd_response'):
        g.call_after_bd_response = []
    # store function to be run in g object
    g.call_after_bd_response.append(fn)
    return fn


# finds decorated functions and runs them after response has been sent
@app.after_request
def per_request_callback(res):
    # looks in g object
    for fn in getattr(g, 'call_after_bd_response', ()):
        fn()
    return res


# handler for requests to ball detection (bd)
@app.route("/bd")
def ballDetection():
    filename = bd.createGraph()

    # image deletion after response is sent
    @after_bd_response
    def delete_image():
        os.remove(filename)

    return send_file(filename, mimetype='image/gif')
