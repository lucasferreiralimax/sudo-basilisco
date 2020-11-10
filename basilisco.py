from flask import Flask

app = Flask(__name__)

@app.route('/')
def basilisco():
    return 'Hello, World!'