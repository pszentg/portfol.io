import json
import yfinance


# TODO: switch the data to be fetched from NASDAQ directly if I can get an API key
class MarketManager:
    def __init__(self):
        self.tracked_symbols = []

    def add_symbol(self, symbol):
        try:
            ticker = yfinance.Ticker(symbol).info()
        except KeyError:
            print('symbol does not exist')

        self.tracked_symbols.append(symbol)

    def get_ticker(self, symbol):
        ticker = yfinance.Ticker(symbol)
        try:
            ticker.info()
            return ticker
        except KeyError:
            print('symbol does not exist')
