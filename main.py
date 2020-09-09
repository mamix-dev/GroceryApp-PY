from flask import Flask

webApp = Flask(__name__)

@app.route("/")
def landing_page():
    print("Test")
