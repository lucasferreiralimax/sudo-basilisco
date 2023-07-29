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

themes = [
    {
        "name": "Câmara Secreta",
        "level": 1,
    }б
    {
        "name": "World",
        "level": 2,
    }
]

def basilisco_say():
    response = make_response(jsonify(data), 201)
    return response

def basilisco_eye():
    data.append({
        "username": "basilisco_child",
        "status": "hidden secrect",
        "theme": "Câmara Secreta 2",
        "age": "L"
    })
    response = make_response(jsonify({"error": "hidden eye"}), 500)
    return response

@app.route('/')
def basilisco_home():
    return 'Do you saying with old snakes?'

@app.route("/basilisco", methods=['GET', 'POST'])
def basilisco_api():    
    if request.method == 'POST':
        return basilisco_eye()
    
    return basilisco_say()

@app.route("/temas", methods=['GET'])
def basilisco_themes():
    response = make_response(jsonify(themes), 201)
    return response
