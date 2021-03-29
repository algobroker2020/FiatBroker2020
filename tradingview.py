# @Author: Benjamin Gates
# @Creation: @date
# @Description: This file ....
import sys

from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import mplfinance as mpf
import pandas as pd
import matplotlib.animation as animation
from matplotlib.figure import Figure
import numpy as np

from asset import Asset
from tradingoptions import TradingSettings


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        idf = pd.read_csv('datas/SPY_20110701_20120630_Bollinger.csv', index_col=0, parse_dates=True)
        idf.shape
        idf.head(3)
        idf.tail(3)
        self.df = idf.loc['2011-07-01':'2011-12-30', :]
        self.df = self.df.iloc[0:30]
        self.exp12 = self.df['Close'].ewm(span=12, adjust=False).mean()
        self.exp26 = self.df['Close'].ewm(span=26, adjust=False).mean()
        self.macd = self.exp12 - self.exp26
        self.signal = self.macd.ewm(span=9, adjust=False).mean()
        self.histogram = self.macd - self.signal
        self.apds = [mpf.make_addplot(self.exp12, color='lime'),
                     mpf.make_addplot(self.exp26, color='c'),
                     mpf.make_addplot(self.histogram, type='bar', width=0.7, panel=1, color='dimgray', alpha=1,
                                      secondary_y=False),
                     mpf.make_addplot(self.macd, panel=1, color='fuchsia', secondary_y=True),
                     mpf.make_addplot(self.signal, panel=1, color='b', secondary_y=True),
                     ]

        s = mpf.make_mpf_style(base_mpf_style='starsandstripes', rc={'figure.facecolor': 'lightgray'})
        self.fig, self.axes = mpf.plot(self.df, type='candle', addplot=self.apds, figscale=1.5, figratio=(7, 5),
                                       title='\n\nMACD', style=s, volume=True, volume_panel=2, panel_ratios=(6, 3, 2),
                                       returnfig=True)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        self.ax_main = self.axes[0]
        self.ax_emav = self.ax_main
        self.ax_hisg = self.axes[2]
        self.ax_macd = self.axes[3]
        self.ax_sign = self.ax_macd
        self.ax_volu = self.axes[4]
        self.df = idf.loc['2011-07-01':'2011-12-30', :]
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=250)

    def animate(self, ival):
        if (20 + ival) > len(self.df):
            print('no more data to plot')
            return
        data = self.df.iloc[0:(30 + ival)]
        self.exp12 = data['Close'].ewm(span=12, adjust=False).mean()
        self.exp26 = data['Close'].ewm(span=26, adjust=False).mean()
        self.macd = self.exp12 - self.exp26
        self.signal = self.macd.ewm(span=9, adjust=False).mean()
        self.histogram = self.macd - self.signal
        self.apds = [mpf.make_addplot(self.exp12, color='lime', ax=self.ax_emav),
                mpf.make_addplot(self.exp26, color='c', ax=self.ax_emav),
                mpf.make_addplot(self.histogram, type='bar', width=0.7, color='dimgray', alpha=1, ax=self.ax_hisg),
                mpf.make_addplot(self.macd, color='fuchsia', ax=self.ax_macd),
                mpf.make_addplot(self.signal, color='b', ax=self.ax_sign),
                ]

        for ax in self.axes:
            ax.clear()
        mpf.plot(data, type='candle', addplot=self.apds, ax=self.ax_main, volume=self.ax_volu)

    # def plot(self):
    #     x = np.array([50, 30, 40])
    #     labels = ["Apples", "Bananas", "Melons"]
    #     ax = self.figure.add_subplot(111)
    #     ax.pie(x, labels=labels)


class TradingView(QWidget):
    def __init__(self, asset: Asset, parent=None):
        super(TradingView, self).__init__(parent)

        hbox = QHBoxLayout()

        chart = Canvas(width=8, height=8)
        tro = TradingSettings(asset)

        hbox.addWidget(chart, 8)
        hbox.addWidget(tro, 2)

        self.setLayout(hbox)
