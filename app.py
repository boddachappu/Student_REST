from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from setting import authentication, identity
from resource.User import Usersignup
from resource.student import Student, StudentMarks, Display

app = Flask(__name__)
app.secret_key = 'abcd'
api = Api(app)

Students = []

jwt = JWT(app,authentication,identity) #/auth

api.add_resource(Display,'/student')
api.add_resource(Student,'/student/<string:name>')
api.add_resource(StudentMarks,'/<string:name>/marks')
api.add_resource(Usersignup,'/signup')

if __name__ == '__main__':
    app.run(port=5000,debug=True)