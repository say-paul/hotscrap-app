from flask_restful import Resource
from utils import response
from user import add_user,get_user
from flask import request

class User(Resource):
    def get(self,mobile_num):
        key, data = get_user.findUserByMob(mobile_num)
        if len(data) == 0:
            return response.styler(404)
        dictionary = dict(zip(key,data[0]))
        return response.styler(200, dictionary)
    def post(self,mobile_num):
        name=request.form["Name"]
        email=request.form["Email"]
        mobile_num=request.form["mobile_num"]
        account_type=request.form["account_type"]
        err=add_user.addUser(mobile_num,name,email,account_type)
        if err:
            return response.styler(400)
        return response.styler(204)