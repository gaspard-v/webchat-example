from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
