from src.models.interval import Interval
from src.data import DataApi, MT5
from src.models import Pair
from datetime import datetime

class Data:
    def __init__(self):
        self.mt5 = MT5()

    def history(self, pair:Pair, datetime_start:int, datetime_end:int=None, interval:Interval=None):
        api = self.mt5
        datetime_start = datetime.fromtimestamp(datetime_start)
        if not interval:
            interval = Interval('m1')
        if datetime_end:
            # range
            datetime_end = datetime.fromtimestamp(datetime_end)
            res = api.get_pair_range_price( pair=pair, 
                                            datetime_start=datetime_start, 
                                            datetime_end=datetime_end, 
                                            interval=interval)
        else:
            # single 
            res = api.get_pair_price(pair=pair, _datetime=datetime_start, interval=interval)
        return res

    def test(self):
        res = []
        for api in [self.mt5]:
            _res = {'mt5':self.mt5.test()} 
            res.append(_res)
        return res
