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
        ItemName, ItemUnit, CurrentRate = None, None, None
        if request.form.get('ItemName', None):
            ItemName = request.form['ItemName']
        if request.form.get('ItemUnit', None):
            ItemUnit = request.form['ItemUnit']
        if request.form.get('CurrentRate', None):
            CurrentRate = request.form["CurrentRate"]
        print("The values are , {} , {} , {}".format(ItemName, ItemUnit,
                                                     CurrentRate))
        err = put_item.updateInfo(ItemID,ItemName, ItemUnit, CurrentRate)
        if err!=True:
            return response.styler(204)
        return response.styler(400)

    def delete(self,ItemID):

        err=delete_item.dltItem(ItemID)
        print(err)
        if err!= True:
            return response.styler(204)
        return response.styler(404)

class Table(Resource):
    def get(self):
        key,data= get_table.getTable()
        if len(data)==0:
            return response.styler(404)
        dictionary=dict(zip(key,data))
        return response.styler(200,dictionary)