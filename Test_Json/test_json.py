# -*- coding: utf-8 -*-
import requests

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
data_two ={
    'one':'123',
    'two':'123'
}

url = 'http://127.0.0.1/test.json'
#html = requests.get(url,data=data_two).text
html = requests.post(url,data=data_one).text
print html
print data_one

