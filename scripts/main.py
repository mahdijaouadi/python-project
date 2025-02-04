from flask import Flask, jsonify
from data_construction import *
from backtesting import *
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
app = Flask(__name__)

# First GET function: Root endpoint
@app.route('/', methods=['GET'])
def home():
    return "Welcome to my simple web server!"

# Second GET function: /info endpoint
@app.route('/backtesting', methods=['GET'])
def backtesting_calling():
    # llm=ChatGoogleGenerativeAI(model='gemini-1.5-flash-8b')
    # response=llm.invoke('hello')
    return {"status": "Self-healing task has been launched"}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
