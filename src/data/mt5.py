from datetime import datetime
from src.data.api import DataApi
from src.models import Interval, Pair
import MetaTrader5 as mt5
import numpy as np

class MT5(DataApi):

    intervals = {'m1': mt5.TIMEFRAME_M1}

    def __init__(self):
        # connect to MetaTrader 5
        if not mt5.initialize():
            print("initialize() failed")
            mt5.shutdown()
        
        # request connection status and parameters
        print(mt5.terminal_info())
        # get data on MetaTrader 5 version
        print(mt5.version())

    def get_pair_price(self,
                       pair:Pair,  
                       _datetime:datetime, 
                       interval:Interval):

        rates = mt5.copy_rates_from(pair.get_name(), 
                                    self.intervals[interval.get_name()],
                                    _datetime, 1000)
        rates = price_extractor(rates[0])
        return rates

    def get_pair_range_price(self, 
                             pair:Pair,   
                             datetime_start:datetime, 
                             datetime_end:datetime, 
                             interval:Interval):

        rates = mt5.copy_rates_range(pair.get_name(), 
                                    self.intervals[interval.get_name()],
                                    datetime_start, datetime_end)
        
        rates = [price_extractor(row) for row in rates]
        return rates

def price_extractor(arr):
    return [arr[1], # open
            arr[2], # high
            arr[3], # low
            arr[4], # close
            float(arr[6]) # spread
            ]
