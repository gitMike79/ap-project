import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                            user = "root",
                            passwd = "tired",
                            db = "bachapp")
    c = conn.cursor()

    return c, connMySQLdb
