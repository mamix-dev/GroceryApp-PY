from flask import Flask
import os

directory = os.path.dirname(os.path.abspath(__file__))

webApp = Flask(__name__)

# The landing page for the app.
@webApp.route("/")
def landing_page():
    return directory + "/index.html"
