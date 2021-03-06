from datetime import datetime
from src.models import Pair, Interval


class DataApi:
    def __init__(self):
        pass

    def get_pair_price(self,  
                       _datetime:datetime, 
                       interval:Interval,
                       pair:Pair):
        pass

    def get_pair_range_price(self, 
                             datetime_start:datetime, 
                             datetime_end:datetime, 
                             interval:Interval,
                             pair:Pair):
        pass

    def test(self):
        res = {'get_pair_price':self.get_pair_price(Pair('eur','usd'), datetime(2010,9,2,12), Interval()),
               'get_pair_range_price':self.get_pair_range_price(Pair('eur','usd'), datetime(2020,9,2,12), datetime(2020,9,2,13), Interval())}

        return res