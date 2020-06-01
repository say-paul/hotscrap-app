from flask_restful import Resource
from utils import response
from store import get_item,post_item,put_item,delete_item
from flask import request
class Item(Resource):
    
    def get(self,ItemID):
        endpoint="store"
        key, data = get_item.findItem(ItemID)
        print(endpoint)
        if len(data) == 0:
            return response.styler(404)
        itemdetails = dict(zip(key,data[0]))

        return response.styler(200, itemdetails)

    def post(self):
        ItemName= request.form["ItemName"]
        ItemUnit= request.form["ItemUnit"]
        CurrentRate= request.form["CurrentRate"]
        err=post_item.addItem(ItemName,ItemUnit,CurrentRate)
        if err != True:
            return response.styler(200,{"ItemID": err})
        return response.styler(400)

    def put(self,ItemID):
        ItemName=request.args.get ('ItemName')
        ItemUnit=request.args.get('ItemUnit')
        CurrentRate=request.args.get("CurrentRate")
        err=put_item.updateInfo(ItemName,ItemUnit,CurrentRate,ItemID)
        if err!=True:
            return response.styler(204)
        return response.styler(400)

    def delete(self,ItemID):
        err=delete_item.dltItem(ItemID)
        if err!= True:
            return response.styler(204)
        return response.styler(404)
        

