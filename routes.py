from flask import Flask
from flask_restful import Resource, Api
from user import getuser

app = Flask(__name__)
api = Api(app)

api.add_resource(getuser.getUserByMob, '/getuser/<string:mobile_num>')
