# @Author: Benjamin Gates
# @Creation: 24 Feb 2021
# @Description: This file contains scripts for my trading strategy
from datetime import datetime

import numpy as np
import pandas as pd
import backtrader as bt


class MRBollingerBandStrategy(bt.Strategy):
    """
        This is a simple mean reversion bollinger band strategy.
        Entry criteria:
            -Long:
                -Price closes below the lower band
                -Stop Order entry when price crosses back above the lower band
            -Short:
                -Price close above the upper band
                -Stop order entry when price crosses back below the upper band
        Exit criteria:
            -Long/Short: Price touching the media line
    """

    params = (("period", 20), ("devfactor", 2), ("size", 20), ("debug", False))

    def __init__(self):
        self.boll = bt.indicators.BollingerBands(period=self.p.period, devfactor=self.p.devfactor)
        self.sx = bt.indicators.CrossDown(self.data.close, self.boll.lines.top)
        self.lx = bt.indicators.CrossUp(self.data.close, self.boll.lines.bot)

    def next(self):
        orders = self.broker.get_orders_open()
        # Cancel open orders so we can track the media line
        if orders:
            for order in orders:
                self.broker.cancel(order)

        if not self.position:
            if self.data.close > self.boll.lines.top:
                self.sell(exectype=bt.Order.Stop, price=self.boll.lines.top[0], size=self.p.size)
            if self.data.close < self.boll.lines.bot:
                self.buy(exectype=bt.Order.Stop, price=self.boll.lines.bot[0], size=self.p.size)
        else:
            if self.position.size > 0:
                self.sell(exectype=bt.Order.Limit, price=self.boll.lines.mid[0], size=self.p.size)
            else:
                self.sell(exectype=bt.Order.Limit, price=self.boll.lines.mid[0], size=self.p.size)

        if self.p.debug:
            print('------------------------NEXT-----------------------------')
            print('1.Data Name:  {}'.format(self.data._name))
            print('2. Bar Num:  {}'.format(len(self.data)))
            print('3. Current date :  {}'.format(self.data.datetime.datetime()))
            print('4. Open :  {}'.format(self.data.open[0]))
            print('5. High :  {}'.format(self.data.high[0]))
            print('6. Low :  {}'.format(self.data.low[0]))
            print('7. Close :  {}'.format(self.data.close[0]))
            print('8. Volume :  {}'.format(self.data.volume[0]))
            print('9. Position Size :  {}'.format(self.position.size))
            print('---------------------------------------------------------')

    def notify_trade(self, trade):
        if trade.isclosed:
            dt = self.data.datetime.date()
            print('------------------------TRADE-----------------------------')
            print('1.Data Name:  {}'.format(trade.data._name))
            print('2. Bar Num:  {}'.format(len(trade.data)))
            print('3. Current date :  {}'.format(dt))
            print('4. Status :  Trade complete')
            print('5. Ref :  {}'.format(trade.ref))
            print('6. Pnl :  {}'.format(round(trade.pnl, 2)))
            print('---------------------------------------------------------')

    def __str__(self):
        return str.format("This strategy is used to trade asset")


class TradeEngine:
    def __init__(self, ticker: str):
        self.ticker = ticker

    def run(self):
        start_cash = 1000  # our starting cash
        cerebro = bt.Cerebro()  # create an instance of cerebro
        cerebro.addstrategy(MRBollingerBandStrategy)  # add our strategy
        data = bt.feeds.Quandl(dataname=self.ticker, fromdate=datetime(2017, 1, 1), todate=datetime(2018, 1, 1))
        # add datas to cerebro
        cerebro.adddata(data)
        # add sizer
        cerebro.addsizer(bt.sizers.FixedReverser, stake=10)
        # run over everything
        try:
            cerebro.run()
        except Exception as e:
            print('Error occured, {}'.format(str(e)))

        # Get final portofolio value
        portvalue = cerebro.broker.getvalue()
        pnl = portvalue - start_cash
        # Print out the final result
        print('Final portofolio value: {}'.format(round(portvalue, 2)))
        print('P/L: ${}'.format(round(pnl, 2)))
