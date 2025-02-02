import pandas as pd
import yfinance as yf
import sys
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

gemini_llm=ChatGoogleGenerativeAI(model='gemini-1.5-flash-8b')
response=gemini_llm.invoke('hello')
print(response.content)