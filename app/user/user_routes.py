from flask_restful import Resource
from utils import response
from user import get_user

class GetUser(Resource):
    def get(self,mobile_num):
        key, data = get_user.findUserByMob(mobile_num)
        if len(data) == 0:
            return response.styler(404)
        dictionary = dict(zip(key,data[0]))
        return response.styler(200, dictionary)
