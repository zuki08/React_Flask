import mysql.connector as SQLConnect

def db_conn_func():
    dbconn = SQLConnect.connect(
        host = 'localhost',
        user = 'j1',
        password = 'sqlpass1!',
        database = 'flaskmv'
    )
    return dbconn