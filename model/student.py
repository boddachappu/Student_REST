import sqlite3


class StudentModel:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def json(self):
        return {'name' : self.name,'marks':self.marks}

    @classmethod
    def get_by_name(cls, name):
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        data = cursor.execute("select * from student where name =? ", (name,))
        data = data.fetchone()
        conn.commit()
        conn.close()
        if data:
            return cls(*data)

    def insert(self):
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute("insert into student values(?,?)", (self.name,self.marks))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute('update student set marks = ? where name = ?', (self.marks,self.name))
        conn.commit()
        conn.close()