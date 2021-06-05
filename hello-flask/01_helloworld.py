# $ flask --app 01_helloworld run
# $ curl http://127.0.0.1:5000

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
