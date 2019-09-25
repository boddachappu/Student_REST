import sqlite3
from flask import  request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from model.student import StudentModel


class Display(Resource):
    def get(self):
        data_list = []
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        data = cursor.execute("select * from student")
        row = data.fetchall()
        if row:
            for data in row:
                data_l = ({'name':data[0],'marks':data[1]})
                data_list.append(data_l)
            return {'students': data_list}, 200
        return {'Message': 'Not found'}, 404


class Student(Resource):
    @jwt_required()
    def get(self,name):
        row = StudentModel.get_by_name(name)
        if row:
            return row.json(), 200
        return {'Message' : 'Not found'}, 404

    def post(self,name):
        data_jason = request.get_json()
        row = StudentModel.get_by_name(name)
        ob = StudentModel(data_jason['name'],data_jason['marks'])
        if row:
            return {'message' : "student {} already present".format(name)}
        else:
            ob.insert()
            return {'Message': "The student record is inserted successfully"}, 201

    def delete(self,name):
        row = StudentModel.get_by_name(name)
        if row:
            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()
            cursor.execute("delete from student where name = ?", (name,))
            conn.commit()
            conn.close()
            return {'Message':'The student {} is delete from the table'.format(name)}
        return {'Message': 'The student {} is not present in the table'.format(name)}, 201

    def put(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument('marks',
                            required=True,
                            help='Please enter the marks scored in all types of education'
                            )
        data = parser.parse_args()
        row = StudentModel.get_by_name(name)
        ob = StudentModel(name,data['marks'])
        if row:
            ob.update()
            return {'Message':'The student {} is got updated in the table'.format(name)}, 202
        ob.insert()
        return {'Message': "The student record is inserted successfully"}, 201


class StudentMarks(Resource):
    def get(self,name):
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        data = cursor.execute("select * from student where name =? ", (name,))
        row = data.fetchone()
        if row:
            return {'student marks' : row[1]}, 200
        return {'Message':'Not found'}, 404

    def post(self,name):
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        data_jason = request.get_json()
        data_row = cursor.execute("select * from student where name =? ", (name,))
        row = data_row.fetchone()
        if row:
            cursor.execute('update student set marks = ? where name = ?',(data_jason['marks'],row[0],))
            conn.commit()
            conn.close()
            return {'Message': 'The marks of the student {} has been updated in the table'.format(name)},201
        return {'Message':'not found'}, 404

