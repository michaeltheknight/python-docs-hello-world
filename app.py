from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "K.I.T.T.: Hallo, Michael!"
