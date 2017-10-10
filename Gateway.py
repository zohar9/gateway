from flask import Flask
import logging
app = Flask(__name__)

@app.route('/')
def get():
    return 'Hello, World!'

@app.route('/', methods=['POST'])
def post():
    logging.warning('Watch out!')
    return "ok"
