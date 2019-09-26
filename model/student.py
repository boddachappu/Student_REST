import sqlite3
from db import db


class StudentModel(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15))
    marks = db.Column(db.Float(precision=2))

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def json(self):
        return {'name' : self.name,'marks':self.marks}

    @classmethod
    def get_by_name(cls, name):
        # conn = sqlite3.connect('user.db')
        # cursor = conn.cursor()
        # data = cursor.execute("select * from student where name =? ", (name,))
        # data = data.fetchone()
        # conn.commit()
        # conn.close()
        # if data:
        #     return cls(*data)
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        # conn = sqlite3.connect('user.db')
        # cursor = conn.cursor()
        # cursor.execute("insert into student values(?,?)", (self.name,self.marks))
        # conn.commit()
        # conn.close()
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        # conn = sqlite3.connect('user.db')
        # cursor = conn.cursor()
        # cursor.execute('update student set marks = ? where name = ?', (self.marks,self.name))
        # conn.commit()
        # conn.close()
        db.session.delete(self)
        db.session.commit()