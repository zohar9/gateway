from flask import Flask
import logging
import os
app = Flask(__name__)

@app.route('/')
def get():
    return 'Hello, World!'

@app.route('/', methods=['POST'])
def post():
    logging.warning('Watch out!')
    return "ok"

app.run(host='0.0.0.0',port=int(os.environ.get("PORT", 5000)))
