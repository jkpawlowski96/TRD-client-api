from MetaTrader5 import RES_E_FAIL
from src import app, api
from flask_restful import Resource
from src.data import Data
from src.models import Pair, Interval

data = Data()

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Test(Resource):
    def get(self):
        return {'results':data.test()}

class History(Resource):
    def get(self, symbol_1:str, symbol_2:str, _datetime:int):
        pair = Pair(symbol_1, symbol_2)
        res = data.history(pair, _datetime)   
        return res
class HistoryRange(Resource):
    def get(self, symbol_1:str, symbol_2:str, datetime_start:int, datetime_end:int, interval:str):
        pair = Pair(symbol_1, symbol_2)
        interval = Interval(interval)
        res = data.history(pair, datetime_start, datetime_end, interval)   
        return res

api.add_resource(HelloWorld, '/')
api.add_resource(Test,'/test')
api.add_resource(History,'/history/<string:symbol_1>/<string:symbol_2>/<int:_datetime>')
api.add_resource(HistoryRange,'/history/<string:symbol_1>/<string:symbol_2>/<int:datetime_start>/<int:datetime_end>/<string:interval>')

