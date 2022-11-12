from flask import Flask, render_template, request
from db_conn import db_conn_func

connection = db_conn_func()

app=Flask(__name__)

@app.route("/info")
def getinfo():
    response_body = {
        "name": "Heffe",
        "purpose": "Trying to connect React to Flask, making this an API"
    }
    return response_body

@app.route('/db-test')
def getSong():
    db_cursor = connection.cursor()
    q = 'select * from musicvid where id = 9'
    db_cursor.execute(q)
    res = db_cursor.fetchall()
    res = res[0]
    response_body = {
        "id": res[0],
        "title": res[1],
        "vid_id": res[2]
    }
    return response_body