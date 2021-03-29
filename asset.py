# @Author: Benjamin Gates
# @Creation: @date
# @Description: This file ....


class Asset:
    def __init__(self, icon, name, buy, sell, is_option=False, ticker=str('')):
        self.icon = icon
        self.name = name
        self.ticker = ticker
        self.buy = buy
        self.sell = sell
        self.is_option = is_option
