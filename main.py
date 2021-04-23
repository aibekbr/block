
from flask import Flask, request
import json
data={}
app = Flask(__name__)

@app.route('/register/', methods=["POST"])
def register():
    
    data.update(json.loads(request.data.decode()))
    return "Hello"

@app.route('/login/', methods=["POST"])
def login():
    # global data=json.loads(request.data.decode())
    name=data.get('name')
    password=data.get('password')

    data1=json.loads(request.data.decode())
    ser_name=data1.get("name")
    ser_password=data1.get("password")

    if name==ser_name and password==ser_password:
        return "Login success!!!"
    else:
        return "Login Failed!!!"


if __name__=='__main__':
    app.run()