import flask
import random
from flask import Response
from prometheus_flask_exporter import PrometheusMetrics

app = flask.Flask(__name__)
metrics = PrometheusMetrics(app)
# app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>hey there</p>"

@app.route('/ping', methods=['GET'])
def pingpong():
    resp = Response('pong', status=200, mimetype='application/json')
    return resp

@app.route('/breakme', methods=['GET'])
def breakAll():
    resp = Response('nope', status=500, mimetype='application/json')
    return resp

@app.route('/unauth', methods=['GET'])
def rejectUser():
    resp = Response('go away', status=401, mimetype='application/json')
    return resp

@app.route('/status', methods=['GET'])
def reportStatus():
    if random.choice([True, False]):
        resp = Response('OK', status=200, mimetype='application/json')
    else:
        resp = Response('failure', status=500, mimetype='application/json')
    return resp

app.run(host='0.0.0.0')
