from flask import Flask

webApp = Flask(__name__)

@app.route("/"):
    print("Test")
