import sqlite3

class UserModel:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def get_user_by_name(cls, username):
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        data = cur.execute("select * from user where username = '{}'".format(username))
        data = data.fetchone()
        if data:
            return cls(*data)
        return None

    @classmethod
    def get_user_by_id(cls,_id):
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        data = cur.execute("select * from user where id = '{}'".format(_id))
        data = data.fetchone()
        if data:
            return cls(*data)
        return None