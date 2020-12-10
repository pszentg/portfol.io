import csv
import json
import os

from app.market_manager import MarketManager as mm


class PortfolioManager:
    def __init__(self):
        with open('configs/platforms.json') as f:
            data = json.load(f)
            self.platforms = data['platforms']
        self.portfolio = {}

        if self.platforms is None:
            self.platforms = []
            print('please add at least a platform you use to trade:')
            platform = input()
            self.platforms.append(platform)

        for platform in self.platforms:
            self.portfolio[platform] = {}
            if os.path.exists(f'configs/{platform}.csv'):
                with open(f'configs/{platform}.csv') as f:
                    data = csv.DictReader(f)
                    for row in data:
                        self.portfolio[platform][row['symbol']] = row['amount']

    def update_portfolio(self, platform, symbol, amount):
        if symbol not in self.portfolio[platform]:
            self.portfolio[platform][symbol] = 0
        self.portfolio[platform][symbol] = amount

