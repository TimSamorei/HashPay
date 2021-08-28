import sqlite3
from sqlite3 import Error



def create_connection(db_file):
   
    con = None
    try:
        con = sqlite3.connect(db_file)
        return con
    except Error as e:
        print(e)

    return con

def create_account(con, username, hashIndex, hash):
    cur = con.cursor()
    if (get_account(con, username) == []):
        cur.execute("INSERT INTO users VALUES (?, ?, ?)", (username, hash, hashIndex))
        con.commit()
        return 'CREATIONSUCCESS'
    else:
         return 'CREATIONFAILURE'

def get_account(con, username):
    cur = con.cursor()
    cur.execute("select * from users where username=?", (username,))
    return cur.fetchall()
