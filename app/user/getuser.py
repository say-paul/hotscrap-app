from utils import  database
from flask_restful import Resource


class getUserByMob(Resource):
    def get(self,mobile_num):
        db =  database.Db()
        query = ("SELECT * FROM UserProfile WHERE MobileNum=%s")
        params = (mobile_num, )
        key,data = db.select(query,params)
        if len(data) == 0:
            return {"body" : {"msg":"User Not found"}},404
        dictionary = dict(zip(key,data[0]))
        return {"body": dictionary}, 200, {'content-type': 'application/json'}
