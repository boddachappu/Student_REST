import sqlite3

conn = sqlite3.connect('user.db')
curser = conn.cursor()

query = "create table if not exists user (ID INTEGER PRIMARY KEY, username text, password text)"
curser.execute(query)

query_item = "create table if not exists student (ID INTEGER PRIMARY KEY,name text, marks text)"
curser.execute(query_item)

curser.execute("insert into student values('vinod','84')")

conn.commit()
conn.close()