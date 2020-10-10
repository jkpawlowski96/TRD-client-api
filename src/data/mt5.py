from datetime import datetime
from src.data.api import DataApi
 
class MT5(DataApi):
    def __init__(self):
        # connect to MetaTrader 5
        import MetaTrader5 as mt5
        if not mt5.initialize():
            print("initialize() failed")
            mt5.shutdown()
        
        # request connection status and parameters
        print(mt5.terminal_info())
        # get data on MetaTrader 5 version
        print(mt5.version())
    
    