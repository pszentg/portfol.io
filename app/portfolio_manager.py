class PortfolioManager:
    def __init__(self, portfolio=None):
        if portfolio is None:
            portfolio = {}
        self.portfolio = portfolio

    def buy_asset(self, symbol, amount):
        if symbol not in self.portfolio:
            self.portfolio[symbol] = 0
        self.portfolio[symbol] += amount

    def sell_asset(self, symbol, amount):
        if symbol not in self.portfolio or amount > int(self.portfolio[symbol]):
            print('Not enough assets to sell')
        else:
            self.portfolio[symbol] -= amount


class SymbolError(Exception):
    pass
