from flask import Flask
from flask_restful import Resource, Api
from user import user_routes

app = Flask(__name__)
api = Api(app)

api.add_resource(user_routes.User, '/user/<string:mobile_num>')
