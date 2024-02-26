# Clase 7 
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    user_ip = request.remote_addr
    return 'Hello World, tu IP es {}'.format(user_ip)


# Clase 5 - 6
'''from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World2' '''
