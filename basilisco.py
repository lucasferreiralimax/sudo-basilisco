#!/usr/bin/env python
#encoding: utf-8
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

data = [
    {
        "username": "basilisco",
        "status": "hidden secrect",
        "theme": "Câmara Secreta",
        "age": "XV"
    }
]

def basilisco_say():
    response = make_response(jsonify(data), 201)
    return response

def basilisco_eye():
    response = make_response(jsonify({"error": "hidden eye"}), 500)
    return response

@app.route('/')
def basilisco_home():
    return 'Do you saying with old snakes?'

@app.route("/basilisco", methods=['GET', 'POST'])
def basilisco_api():    
    if request.method == 'POST':
        return basilisco_eye()
    else:
        return basilisco_say()