# @Author: Benjamin Gates
# @Creation: 24 Feb 2021
# @Description: This file contains scripts for my trading strategy

# Native imports
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QHBoxLayout, QFrame

from mainwindow import MainWindow

# custom libraries import

# 3rd party libraries import

def start():
    app = QtWidgets.QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    w = MainWindow()
    w.show()

    sys.exit(app.exec())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

# Below we implement realtime stock charts
# from collections import OrderedDict
#
# import pandas as pd
# import datetime
# import requests
# import math
# from requests.exceptions import ConnectionError
# from bs4 import BeautifulSoup
# from matplotlib import pyplot as plt
# from matplotlib import animation as anim
# from matplotlib import gridspec as grid
# from matplotlib import ticker as ticker
# from mplfinance.original_flavor import candlestick_ochl
#
# tickers = ['MSFT', 'AAPL', 'ADBE', 'FB', 'BRK-B', 'TWTR', 'PYPL', 'AMZN']
#
# fig = plt.figure()
# fig.patch.set_facecolor('#121416')
# gs = fig.add_gridspec(6, 6)
# ax1 = fig.add_subplot(gs[0:4, 0:4])
# ax2 = fig.add_subplot(gs[0, 4:6])
# ax3 = fig.add_subplot(gs[1, 4:6])
# ax4 = fig.add_subplot(gs[2, 4:6])
# ax5 = fig.add_subplot(gs[3, 4:6])
# ax6 = fig.add_subplot(gs[4, 4:6])
# ax7 = fig.add_subplot(gs[5, 4:6])
# ax8 = fig.add_subplot(gs[4, 0:4])
# ax9 = fig.add_subplot(gs[5, 0:4])
#
#
# def figure_design(ax):
#     ax.set_facecolor('#091217')
#     ax.tick_params(axis='both', labelsize=14, colors='white')
#     ax.ticklabel_format(useOffset=False)
#     ax.spines['top'].set_color('#808080')
#     ax.spines['left'].set_color('#808080')
#     ax.spines['right'].set_color('#808080')
#     ax.spines['bottom'].set_color('#808080')
#
#
# def string_to_number(df, column):
#     # if isinstance(df.iloc[0, df.columns.get_loc(column)], str):
#     #     df[column] = df[column].str.replace(',', '')
#     try:
#         df[column] = df[column].astype(float)
#     except ValueError:
#         df[column] = 0
#     return df
#
#
# def read_data_ohlc(filename, ticker, usecols):
#     df = pd.read_csv(filename, header=None, usecols=usecols,
#                      names=['time', 'price', 'change', 'volume', 'pattern', 'target'], index_col='time',
#                      parse_dates=True)  # time
#     index_with_nan = df.index[df.isnull().any(axis=1)]
#     df.drop(index_with_nan, 0, inplace=True)
#     df.index = pd.DatetimeIndex(df.index)
#
#     df['price'] = string_to_number(df, 'price')
#     df['volume'] = string_to_number(df, 'volume')
#     df['target'] = string_to_number(df, 'target')
#
#     latest_price = str(df['price'])
#     latest_change = str(df['change'])
#
#     df_vol = df['volume'].resample('1Min').mean()
#
#     data = df.resample('1Min').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last'})
#     print(data)
#
#     data['MA5'] = data['close'].rolling(5).mean()
#     data['MA10'] = data['close'].rolling(10).mean()
#     data['MA20'] = data['close'].rolling(20).mean()
#
#     data['volune_diff'] = df_vol.diff()
#     data[data['volume_diff'] < 0] = None
#
#     index_with_nan = data.index[data.isnull().any(axis=1)]
#     data.drop(index_with_nan, 0, inplace=True)
#     data.reset_index(drop=True, inplace=True)
#
#     return data, latest_price, latest_change, df['pattern'][-1], df['target'][-1], df['volume'][-1]
#
#
# def animate(i):
#     # time_stamp = datetime.datetime.now() - datetime.timedelta(hours=6)
#     # time_stamp = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
#     # filename = 'datas/{} prices_info.csv'.format(str(time_stamp))
#     filename = 'datas/2021-03-27 price_infos.csv'
#     data, price, change, pattern, target, volume = read_data_ohlc(filename, tickers[0], [1, 2, 3, 4, 5, 6])
#
#     candle_counter = range(len(data['open']) - 1)
#     ohcl = []
#     for candle in candle_counter:
#         append_me = candle_counter[candle], data['open'][candle], \
#                     data['high'][candle], data['low'][candle], data['close'][candle]
#         ohcl.append(append_me)
#
#     ax1.clear()
#     candlestick_ochl(ax1, ohcl, width=0.4, colorup='#18b800', colordown='#ff3503')
#     ax1.plot(data['MA5'], color='pink', linestyle='-', linewidth=1, label='5 min Moving Average')
#     ax1.plot(data['MA10'], color='orange', linestyle='-', linewidth=1, label='10 min Moving Average')
#     ax1.plot(data['MA20'], color='#08a0e9', linestyle='-', linewidth=1, label='20 min Moving Average')
#
#     leg = ax1.legend(loc='upper left', facecolor='#121416', fontsize=10)
#     for text in leg.get_texts():
#         plt.set(text, color='w')
#
#     figure_design(ax1)
#
#     ax1.text(0.005, 1.05, tickers[0], transform=ax1.transAxes,
#              color='black', fontsize=18, fontweight='bold', horizontalalignment='left',
#              verticalalignment='center', bbox=dict(facecolor='#ff8f00'))
#     ax1.text(0.2, 1.05, price, transform=ax1.transAxes,
#              color='white', fontsize=18, fontweight='bold', horizontalalignment='center',
#              verticalalignment='center')
#     if change[0] == '+':
#         colorcode = '#18b800'
#     else:
#         colorcode = '#ff3503'
#     ax1.text(0.4, 1.05, change, transform=ax1.transAxes,
#              color=colorcode, fontsize=18, fontweight='bold', horizontalalignment='center',
#              verticalalignment='center')
#
#     ax1.text(0.6, 1.05, target, transform=ax1.transAxes,
#              color='#08a0e9', fontsize=18, fontweight='bold', horizontalalignment='center',
#              verticalalignment='center')
#
#     time_stamp = datetime.datetime.now()
#     time_stamp = time_stamp.strftime('%Y-%m-%d %H-%M-%S')
#
#     ax1.text(1.4, 1.015, time_stamp, transform=ax1.transAxes,
#              color='white', fontsize=12, fontweight='bold', horizontalalignment='center',
#              verticalalignment='center')
#
#     ax1.grid(True, color='gray', linestyle='-', which='major', axis='both', linewidth=0.3)
#     ax1.set_xticklabels([])
#
#
# ani = anim.FuncAnimation(fig, animate, interval=1000)
# plt.show()
#
#
# def web_content_div(web_content, class_path):
#     web_content_divs = web_content.find_all('div', {'class': class_path})
#     try:
#         spans = web_content_divs[0].find_all('span')
#         texts = [span.get_text() for span in spans]
#     except IndexError:
#         texts = []
#     return texts
#
#
# def real_time_price(ticker):
#     volume, one_year_target = [], []
#     url = 'https://finance.yahoo.com/quote/{}?p={}&.tsrc=fin-srch'.format(ticker, ticker)
#     try:
#         r = requests.get(url)
#         web_content = BeautifulSoup(r.text, 'lxml')
#         texts = web_content_div(web_content, 'D(ib) Mend(20px)')
#         # Retrieve the current price and the price change
#         if texts != []:
#             price, change = texts[0], texts[1]
#         else:
#             price, change = [], []
#
#         # Retrieve the market volume from the webcontent
#         texts = web_content_div(web_content,
#                                 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')
#         if texts != []:
#             for count, vol in enumerate(texts):
#                 if vol == 'Volume':
#                     volume = texts[count + 1]
#         else:
#             volume = []
#         # This pattern tells wether the market trend is bullish, bearish or neutral
#         pattern = web_content_div(web_content, 'Fz(x5) Mb(4px)')
#         try:
#             latest_pattern = pattern[0]
#         except IndexError:
#             latest_pattern = []
#         # Retrieve the target
#         texts = web_content_div(web_content,
#                                 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)')
#         if texts != []:
#             for count, target in enumerate(texts):
#                 if target == '1y Target Est':
#                     one_year_target = texts[count + 1]
#         else:
#             one_year_target = []
#
#     except ConnectionError:
#         price, change, volume, latest_pattern, one_year_target = [], [], [], [], []
#
#     return price, change, volume, latest_pattern, one_year_target

# while True:
#     infos = []
#     time_stamp = datetime.datetime.now() - datetime.timedelta(hours=6)
#     time_stamp = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
#     ticker = tickers[0]:
#     price, change, volume, latest_pattern, one_year_target = real_time_price(ticker)
#     infos.append([time_stamp, price, change, volume, latest_pattern, one_year_target])
#
#
#     df = pd.DataFrame(infos)
#     df.transpose()
#     df.to_csv('datas/{}price_infos.csv'.format(str(time_stamp[0:11])), mode='a', header=False)
#     print(infos, end='\n')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
