import sqlite3
from flask_restful import reqparse, Resource
from model.user import UserModel


class Usersignup(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        required = True,
                        help = 'Please enter the username'
                        )
    parser.add_argument('password',
                        required=True,
                        help='Please enter the username'
                        )

    def post(self):
        data = Usersignup.parser.parse_args()
        if UserModel.get_user_by_name(data['username']):
            return {"message" : "User already exists please enter new username"}, 400
        # conn = sqlite3.connect('user.db')
        # cursor = conn.cursor()
        # cursor.execute("Insert into user values(NULL, ?,?)",(data['username'],data['password']))
        # conn.commit()
        # conn.close
        user = UserModel(**data)
        user.save_to_db()
        return {"message":"User is created successfully"},201

