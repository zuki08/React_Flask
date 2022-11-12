from flask import Flask, render_template, request
from werkzeug.exceptions import abort
from werkzeug.middleware.proxy_fix import ProxyFix
app=Flask(__name__)

@app.route("/info", methods=["GET"])
def getinfo():
    return {
        
    }