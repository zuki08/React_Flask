from flask import Flask, render_template, request
from werkzeug.exceptions import abort
from werkzeug.middleware.proxy_fix import ProxyFix

app=Flask(__name__)

@app.route("/info")
def getinfo():
    response_body = {
        "name": "Heffe",
        "purpose": "Trying to connect React to Flask, making this an API"
    }
    return response_body