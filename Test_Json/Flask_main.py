#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
app = Flask(__name__)

data_one ={
    "opr": "add",
    "data": {
        "userName": "98997",
        "disc": "whoami",
        "expDate":"2",
        "ip": [
            "10.10.11.1",
            "10.10.11.2",
            "10.10.11.3"
        ]
    }
}

@app.route('/test.json' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = request.get_data()
        #return json.dumps(a)
        return a
    else:
       # return '<h1>只接受post请求！</h1>'
       return json.dumps(data_one)

@app.route('/user/<name>')
def user(name):
    return'<h1>hello, %s</h1>' % name

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
