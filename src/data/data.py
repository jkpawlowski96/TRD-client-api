from src.data import DataApi, MT5

class Data:
    def __init__(self):
        self.mt5 = MT5()

    def test(self):
        res = []
        for api in [self.mt5]:
            _res = {str(api.__class__):self.mt5.test()} 
            res.append(_res)
        return res
