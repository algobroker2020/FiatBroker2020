# @Author: Benjamin Gates
# @Creation: @date
# @Description: This file ....
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QComboBox, QDoubleSpinBox, \
    QPushButton, QHBoxLayout

from asset import Asset
from strategy import TradeEngine


class TradingSettings(QWidget):
    def __init__(self, asset: Asset, parent=None):
        super(TradingSettings, self).__init__(parent)
        self.asset = asset
        self.amount = QLineEdit()
        self.leverage = QComboBox()
        self.strategies = QComboBox()
        self.total = QLineEdit()
        self.spread = QLineEdit()
        self.spot_price = QLineEdit()
        self.take_profit = QDoubleSpinBox()
        self.take_profit.setMinimum(0.0)
        self.take_profit.setMaximum(100.0)
        self.take_profit.setValue(30.0)
        self.stop_loss = QDoubleSpinBox()
        self.stop_loss.setMinimum(-100.0)
        self.stop_loss.setMaximum(0.0)
        self.stop_loss.setValue(-95.0)
        self.auto_trade_btn = QPushButton("Auto Trade")
        self.buy_btn = QPushButton("Buy")
        self.sell_btn = QPushButton("Sell")
        self.strategies.addItem("Mean Reversion Bollinger Band")
        self.strategies.addItem("Momentum Strategy")
        self.strategies.addItem("Volume-weighted Average Price (VWAP)")
        self.strategies.addItem("Time-weighted Average Price (TWAP)")
        self.strategies.addItem("Percentage of Volume (POV)")
        self.strategies.addItem("Implementation Shorfall")
        self.leverage.addItem("10")
        self.leverage.addItem("20")
        self.leverage.addItem("30")
        self.leverage.addItem("50")
        self.leverage.addItem("100")
        self.leverage.addItem("500")
        self.leverage.addItem("1000")
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox1.addWidget(self.stop_loss)
        hbox1.addWidget(self.take_profit)
        hbox2.addWidget(self.sell_btn)
        hbox2.addWidget(self.buy_btn)
        vbox1.addWidget(QLabel("Amount"))
        vbox1.addWidget(self.amount)
        vbox1.addWidget(QLabel("Leverage"))
        vbox1.addWidget(self.leverage)
        vbox1.addWidget(QLabel("Total"))
        vbox1.addWidget(self.total)
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addWidget(QLabel("Spread"))
        vbox1.addWidget(self.spread)
        vbox2.addWidget(QLabel("Trading strategies"))
        vbox2.addWidget(self.strategies)
        vbox2.addWidget(self.auto_trade_btn)
        vbox2.setAlignment(Qt.AlignBottom)
        vbox1.setAlignment(Qt.AlignTop)
        vbox3.addLayout(vbox1)
        vbox3.addLayout(vbox2)
        self.auto_trade_btn.setObjectName("auto_trade")
        self.sell_btn.setObjectName("sell_btn")
        self.buy_btn.setObjectName("buy_btn")
        self.spread.setEnabled(False)
        self.total.setEnabled(False)

        self.auto_trade_btn.clicked.connect(self.auto_trade)

        self.setLayout(vbox3)

    def auto_trade(self):
        engine = TradeEngine(ticker=self.asset.ticker)
        engine.run()
