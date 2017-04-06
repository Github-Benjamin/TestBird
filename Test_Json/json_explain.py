import json

data_two ={
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

#dict1 = json.loads(data_two)  # Decode into a Python object
dict1 = json.dumps(data_two) # Encode the data

print dict1["data"]
