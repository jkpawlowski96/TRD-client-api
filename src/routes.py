from src import app, api
from flask_restful import Resource
from src.data import Data

data = Data()

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Test(Resource):
    def get(self):
        return {'results':data.test()}

api.add_resource(HelloWorld, '/')
api.add_resource(Test,'/test')
