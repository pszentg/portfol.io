import csv
import json
import os

from app.portfolio_manager import PortfolioManager


class PlatformManager:
    def __init__(self):
        self.platforms = {}
        with open('configs/platforms.json') as f:
            data = json.load(f)
            platforms = []
            if 'platforms' not in data:
                print('please add at least a platform you use to trade:')
                platform = input()
                platforms.append(platform)
            else:
                platforms = data['platforms']

            for platform in platforms:
                self.platforms[platform] = PortfolioManager()
                if os.path.exists(f'platforms/{platform}.csv'):
                    with open(f'platforms/{platform}.csv') as f:
                        data = csv.DictReader(f)
                        for row in data:
                            self.platforms[platform].buy_asset(row['symbol'], float(row['amount']))

    def buy_asset(self, platform, symbol, amount):
        self.platforms[platform].buy_asset(symbol, amount)

    def sell_asset(self, platform, symbol, amount):
        self.platforms[platform].sell_asset(symbol, amount)

    def save_portfolio(self):
        for platform in self.platforms:
            with open(f'platforms/{platform}.csv', 'w+') as f:
                writer = csv.DictWriter(f, ['symbol', 'amount'])
                writer.writeheader()
                for symbol in self.platforms[platform].portfolio:
                    writer.writerow({'symbol': symbol,
                                     'amount': self.platforms[platform].portfolio[symbol]})
