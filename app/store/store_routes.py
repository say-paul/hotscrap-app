from flask_restful import Resource
from utils import response
from store import get_item,post_item,put_item,delete_item
class Item(Resource):
    def get(self,ItemID):
        key, data = get_item.findItem(ItemID)
        if len(data) == 0:
            return response.styler(404)
        itemdetails = dict(zip(key,data[0]))
        return response.styler(200, itemdetails)

   def post(self,ItemId):
        ItemName=request.form["ItemName"]
        ItemUnit=request.form["ItemUnit"]
        CurrentRate=request.form["CurrentRate"]
        err=post_item.addItem(ItemName,ItemUnit,CurrentRate)
        if err != True:
            return response.styler(204)
        return response.styler(400)

    def put():
        

    def delete(self,ItemID):
        err=delete_item.dltItem(ItemID)
        if err!= True:
            return response.styler(204)
        return response.styler(404)
        

