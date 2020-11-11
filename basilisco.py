#!/usr/bin/env python
#encoding: utf-8
# -*- coding: utf-8 -*-

from flask import Flask, json, Response

app = Flask(__name__)

data = {
    "username": "basilisco",
    "theme": "Câmara Secreta"
}

@app.route('/')
def basilisco():
    return 'Do you saying with old snakes?'

@app.route("/basilisco")
def basilisco_say():    
    json_string = json.dumps(data,ensure_ascii = False)
    #creating a Response object to set the content type and the encoding
    response = Response(json_string,content_type="application/json; charset=utf-8")
    return response