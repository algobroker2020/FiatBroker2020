# Import libraries
# import pandas as pd
# from bs4 import BeautifulSoup
# import matplotlib.pyplot as plt
# from urllib.request import urlopen, Request
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
#
# # Parameters
# n = 3  # the # of article headlines displayed per ticker
# tickers = ['AAPL', 'TSLA', 'AMZN', 'MSFT', 'ADBE', 'FB']
#
# # Get Data
# finwiz_url = 'https://finviz.com/quote.ashx?t='
# news_tables = {}
#
# for ticker in tickers:
#     url = finwiz_url + ticker
#     req = Request(url=url, headers={'user-agent': 'my-app/0.0.1'})
#     resp = urlopen(req)
#     html = BeautifulSoup(resp, features="lxml")
#     news_table = html.find(id='news-table')
#     news_tables[ticker] = news_table
#
# try:
#     for ticker in tickers:
#         df = news_tables[ticker]
#         df_tr = df.findAll('tr')
#
#         print('\n')
#         print('Recent News Headlines for {}: '.format(ticker))
#
#         for i, table_row in enumerate(df_tr):
#             a_text = table_row.a.text
#             td_text = table_row.td.text
#             td_text = td_text.strip()
#             print(a_text, '(', td_text, ')')
#             if i == n - 1:
#                 break
# except KeyError:
#     pass
#
# # Iterate through the news
# parsed_news = []
# for file_name, news_table in news_tables.items():
#     for x in news_table.findAll('tr'):
#         text = x.a.get_text()
#         date_scrape = x.td.text.split()
#
#         if len(date_scrape) == 1:
#             time = date_scrape[0]
#
#         else:
#             date = date_scrape[0]
#             time = date_scrape[1]
#
#         ticker = file_name.split('_')[0]
#
#         parsed_news.append([ticker, date, time, text])
#
# # Sentiment Analysis
# analyzer = SentimentIntensityAnalyzer()
#
# columns = ['Ticker', 'Date', 'Time', 'Headline']
# news = pd.DataFrame(parsed_news, columns=columns)
# scores = news['Headline'].apply(analyzer.polarity_scores).tolist()
#
# df_scores = pd.DataFrame(scores)
# news = news.join(df_scores, rsuffix='_right')
#
# # View Data
# news['Date'] = pd.to_datetime(news.Date).dt.date
#
# unique_ticker = news['Ticker'].unique().tolist()
# news_dict = {name: news.loc[news['Ticker'] == name] for name in unique_ticker}
#
# values = []
# for ticker in tickers:
#     dataframe = news_dict[ticker]
#     dataframe = dataframe.set_index('Ticker')
#     dataframe = dataframe.drop(columns=['Headline'])
#     print('\n')
#     print(dataframe.head())
#
#     mean = round(dataframe['compound'].mean(), 2)
#     values.append(mean)
#
# df = pd.DataFrame(list(zip(tickers, values)), columns=['Ticker', 'Mean Sentiment'])
# df = df.set_index('Ticker')
# df = df.sort_values('Mean Sentiment', ascending=False)
# print('\n')
# print(df)
from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QWidget, QListWidgetItem, QFrame, QLabel, QVBoxLayout, QHBoxLayout
from stocknews import StockNews
import pandas as pd


class NewsItem(QWidget):
    def __init__(self, ticker: str, date, title, summary):
        super().__init__()
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        symbol = QLabel('{}'.format(ticker))

        date = QLabel('{}'.format(date))
        title = QLabel('{}'.format(title))
        summary = QLabel('{}'.format(summary))
        symbol.setObjectName("symbol")
        date.setObjectName("date")
        title.setObjectName("title")
        summary.setObjectName("summary")
        symbol.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        date.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        hbox.addWidget(symbol)
        hbox.addWidget(date)
        vbox.addLayout(hbox)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setLineWidth(1)
        vbox.addWidget(line)
        vbox.addWidget(title)
        vbox.addWidget(summary)
        self.setObjectName("news")
        self.setLayout(vbox)


class NewsList(QWidget):
    def __init__(self):
        super().__init__()
        self.tickers = ['AAPL', 'MSFT', 'NFLX', 'ADBE', 'FB', 'TSLA']
        vbox = QVBoxLayout()
        self.title = QLabel("MARKET NEWS & ANALYSIS")
        self.news_list = QListWidget()
        # sn = StockNews(self.tickers, wt_key='MY_WORLD_TRADING_DATA_KEY')
        # sn.summarize()
        news_datas = pd.read_csv("data/news.csv", sep=';', index_col=0, parse_dates=True)
        for index, news_data in news_datas.iterrows():
            news_item_view = NewsItem(news_data['stock'], news_data['published'], news_data['title'],
                                      news_data['summary'])
            news_item = QListWidgetItem(self.news_list)
            news_item.setData(QtCore.Qt.UserRole, news_item_view)
            news_item.setSizeHint(news_item_view.sizeHint())
            self.news_list.addItem(news_item)
            self.news_list.setItemWidget(news_item, news_item_view)

        vbox.addWidget(self.title)
        vbox.addWidget(self.news_list)
        self.setLayout(vbox)
#
# from bs4 import BeautifulSoup
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from urllib.request import urlopen, Request
#
# finviz_url = 'https://finviz.com/quote.ashx?t='
# tickers = ['AMZN', 'MSFT', 'AAPL', 'FB', 'AMZ']
#
# news_datas = {}
#
# for ticker in tickers:
#     url = '{}{}'.format(finviz_url, ticker)
#     req = Request(url, headers={'user-agent' : 'Fiat Broker'})
#     response = urlopen(req, timeout=15000)
#
#     html = BeautifulSoup(response, 'lxml')
#     news_data = html.find(id='news-table')
#     news_datas[ticker] = news_data
#
#
# parsed_data = []
# for ticker, news_data in news_datas.items():
#     for index, row in enumerate(news_data.find_all('tr')):
#         title = row.a.get_text()
#         newslink = row.a['href']
#         date_data = row.td.text.split(' ')
#         if len(date_data) == 1:
#             time = date_data[0]
#         else:
#             date = date_data[0]
#             time = date_data[1]
#         parsed_data.append([ticker, date, str(time).replace('\xa0', ''), title, newslink])
#
# df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title', 'newslink'])
# vader = SentimentIntensityAnalyzer()
#
# f = lambda title: vader.polarity_scores(title)['compound']
#
# df['compound'] = df['title'].apply(f)
#
# print(df.head())

# from GoogleNews import GoogleNews
# googlenews = GoogleNews()
# googlenews.set_lang('en')
# googlenews.set_period('7d')
# googlenews.set_time_range('02/01/2020', '02/28/2020')
# googlenews.set_encode('utf-8')
# googlenews.get_news('APPLE')
# googlenews.search('AAPLE')
# print(googlenews.get_page(2))
# result = googlenews.page_at(2)
# print(result)
# print(googlenews.total_count())
# results = googlenews.results(sort=True)
# print(results)
# titles = googlenews.get_texts()
# print(titles)
# links = googlenews.get_links()
# print(links)