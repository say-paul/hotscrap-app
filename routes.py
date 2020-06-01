from flask import Flask
from flask_restful import Resource, Api
from user import user_routes
from store import store_routes

app = Flask(__name__)
api = Api(app)

api.add_resource(user_routes.User, '/user/<string:mobile_num>')

api.add_resource(store_routes.Item,'/store/<string:ItemID>',endpoint= "Item")
api.add_resource(store_routes.Item,'/store', endpoint="addItem")