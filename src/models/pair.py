class Pair:
    def __init__(self, symbol_1:str, symbol_2:str):
        self.symbol_1 = self.preporcess_symbol(symbol_1)
        self.symbol_2 = self.preporcess_symbol(symbol_2)

    @staticmethod
    def preporcess_symbol(symbol:str):
        symbol = symbol.upper()
        return symbol

    def get_name(self):
        return self.symbol_1 + self.symbol_2