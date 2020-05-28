from flask_restful import Resource
from utils import response
from store import store_item
class Item(Resource):
    def get(self,ItemID):
        

   def post(self,ItemId):
        ItemN=request.form["Name"]
        email=request.form["Email"]
        account_type=request.form["account_type"]
        err=add_user.addUser(mobile_num,name,email,account_type)
        if err != True:
            return response.styler(204)
        return response.styler(400)

    def put():

    def delete():

