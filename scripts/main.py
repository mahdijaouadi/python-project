from flask import Flask, jsonify
from data_construction import *
from backtesting import *


app = Flask(__name__)

# First GET function: Root endpoint
@app.route('/', methods=['GET'])
def home():
    return "Welcome to my simple web server!"

# Second GET function: /info endpoint
@app.route('/backtesting', methods=['GET'])
def data_construction_calling():
    return data_backtesting_func()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
