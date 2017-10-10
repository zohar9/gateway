from flask import Flask
import logging
import os
app = Flask(__name__)

app.run(host='0.0.0.0',post=int(os.environ.get("PORT", 5000)))

@app.route('/')
def get():
    return 'Hello, World!'

@app.route('/', methods=['POST'])
def post():
    logging.warning('Watch out!')
    return "ok"
