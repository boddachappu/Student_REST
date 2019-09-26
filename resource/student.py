import sqlite3
from flask import  request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from model.student import StudentModel


class Display(Resource):
    def get(self):
        return {'student' : [student.json() for student in StudentModel.query.all()]}


class Student(Resource):
    @jwt_required()
    def get(self,name):
        row = StudentModel.get_by_name(name)
        if row:
            return row.json(), 200
        return {'Message' : 'Not found'}, 404

    def post(self,name):

        if StudentModel.get_by_name(name):
            return {'message' : "student {} already present".format(name)}
        data_jason = request.get_json()
        ob = StudentModel(name, data_jason['marks'])
        ob.save_to_db()
        return {'Message': "The student record is inserted successfully"}, 201

    def delete(self,name):
        student = StudentModel.get_by_name(name)
        if student:
            # conn = sqlite3.connect('user.db')
            # cursor = conn.cursor()
            # cursor.execute("delete from student where name = ?", (name,))
            # conn.commit()
            # conn.close()
            student.delete_from_db()
            return {'Message':'The student {} is delete from the table'.format(name)}
        return {'Message': 'The student {} is not present in the table'.format(name)}, 201

    def put(self,name):
        # parser = reqparse.RequestParser()
        # parser.add_argument('marks',
        #                     required=True,
        #                     help='Please enter the marks scored in all types of education'
        #                     )
        # data = parser.parse_args()
        # row = StudentModel.get_by_name(name)
        # ob = StudentModel(name,data['marks'])
        # if row:
        #     ob.update()
        #     return {'Message':'The student {} is got updated in the table'.format(name)}, 202
        # ob.insert()
        # return {'Message': "The student record is inserted successfully"}, 201

        parser = reqparse.RequestParser()
        parser.add_argument('marks',
                            required=True,
                            help='Please enter the marks scored in all types of education'
                            )
        student = StudentModel.get_by_name(name)
        data = parser.parse_args()
        if student:
            student.marks = data['marks']
            return {'Message': "The student record is updated successfully"},
        else:
            student = StudentModel(name,data['marks'])
        student.save_to_db()
        return {'Message': "The student record is inserted successfully"},


class StudentMarks(Resource):
    def get(self,name):
        row = StudentModel.get_by_name(name)
        if row:
            return {'student marks' : row.marks}, 200
        return {'Message':'Not found'}, 404

    def post(self,name):
        data_jason = request.get_json()
        row = StudentModel.get_by_name(name)
        if row:
            row.marks = data_jason['marks']
            row.save_to_db()
            return {'Message': 'The marks of the student {} has been updated in the table'.format(name)},201
        return {'Message':'not found'}, 404

