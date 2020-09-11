from flask import Flask
import os

directory = os.path.dirname(os.path.abspath(__file__))

webApp = Flask(__name__)

@app.route("/")
def landing_page():
    print("Test")
