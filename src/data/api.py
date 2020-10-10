from datetime import datetime
from src.models import Pair, Interval


class DataApi:
    def __init__(self):
        pass
    def get_pair_price(self, datetime_start:datetime, 
                             datetime_end:datetime, 
                             interval:Interval,
                             pair:Pair):
        pass

    def test(self):
        return {'result':'succed'}