import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    password = db.Column(db.String(8))

    def __init__(self,username,password):
        self.username = username
        self.password = password


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user_by_name(cls, username):
        # conn = sqlite3.connect('user.db')
        # cur = conn.cursor()
        # data = cur.execute("select * from user where username = '{}'".format(username))
        # data = data.fetchone()
        # if data:
        #     return cls(*data)
        # return None
        return cls.query.filter_by(username=username).first()


    @classmethod
    def get_user_by_id(cls,_id):
        #     conn = sqlite3.connect('user.db')
        #     cur = conn.cursor()
        #     data = cur.execute("select * from user where id = '{}'".format(_id))
        #     data = data.fetchone()
        #     if data:
        #         return cls(*data)
        #     return None
        return cls.query.filter_by(id=_id).first()