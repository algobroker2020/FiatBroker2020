# @Author: Benjamin Gates
# @Creation: @date
# @Description: This file ....
import typing

from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QTabBar, QStylePainter, QStyleOptionTab, QStyle, QTabWidget, QProxyStyle, QWidget, \
    QGridLayout, QLabel, QVBoxLayout, QLineEdit, QListWidget, QHBoxLayout, QListWidgetItem, QPushButton

from asset import Asset
import random
r = random


def get_bin_options():
    return  \
    [
        Asset(icon="icons/32x32/constellation.png", name="Binary USD/JPY", ticker="USDJPY", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
        Asset(icon="icons/32x32/consensus.png", name="Binary USD/GBP", ticker="GBPUSD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
        Asset(icon="icons/32x32/chesscoin.png", name="Binary EUR/USD", ticker="EURUSD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
        Asset(icon="icons/32x32/centurion.png", name="Binary USD/NZD", ticker="NZDUSD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
        Asset(icon="icons/32x32/bunnycoin.png", name="Binary AUD/CHF", ticker="AUDCHF", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
        Asset(icon="icons/32x32/callisto-network.png", name="Binary NZD/AUD", ticker="AUDNZD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
    ]


def get_otc_options():
    return \
        [
            Asset(icon="icons/32x32/coinpoker.png", name="OTC USD/JPY", ticker="USDJPY", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
            Asset(icon="icons/32x32/cybervein.png", name="OTC USD/GBP", ticker="GBPUSD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
            Asset(icon="icons/32x32/daneel.png", name="OTC EUR/USD", ticker="EURUSD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
            Asset(icon="icons/32x32/deuscoin.png", name="OTC USD/NZD", ticker="NZDUSD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
            Asset(icon="icons/32x32/daxxcoin.png", name="OTC AUD/CHF", ticker="AUDCHF", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
            Asset(icon="icons/32x32/darsek.png", name="OTC NZD/AUD", ticker="AUDNZD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5), is_option=True),
        ]


def get_forex():
    return \
        [
            Asset(icon="icons/32x32/edu-coin.png", name="USD/JPY", ticker="USDJPY", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/embers.png", name="USD/GBP", ticker="GBPUSD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/ejoy.png", name="EUR/USD", ticker="EURUSD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/egretia.png", name="USD/NZD", ticker="NZDUSD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/eaglecoin.png", name="AUD/CHF", ticker="AUDCHF", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/digital-money-bits.png", name="NZD/AUD", ticker="AUDNZD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
        ]


def get_cryptos():
    return \
        [
            Asset(icon="icons/32x32/bitcoin.png", name="Bitcoin", ticker="BTC-USD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/ethereum.png", name="Ethereum", ticker="ETH-USD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/bitcoin.png", name="Chainlink", ticker="LINK-USD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/litecoin.png", name="Litecoin", ticker="LTC-USD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/bitcoincash.png", name="Bitcoin cash", ticker="BCH-USD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/ripple.png", name="Ripple", ticker="XRP-USD", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
        ]


def get_commodities():
    return \
        [
            Asset(icon="icons/32x32/igtoken.png", name="Apple", ticker="AAPL", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/monero-classic.png", name="Adobe Systems,inc.", ticker="ADBE", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/ors-group.png", name="Nvidia LLC", ticker="NVDA", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/qwark.png", name="Dell Technologies", ticker="DELL", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/rentledger.png", name="Amazon", ticker="AMZN", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/reddcoin.png", name="Microsoft", ticker="MSFT", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
        ]


def get_metals():
    return \
        [
            Asset(icon="icons/32x32/equitrader.png", name="Copper", ticker="HG:CMX", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/expanse.png", name="Silver", ticker="XAG", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/eztoken.png", name="Gold", ticker="GC:CMX", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
            Asset(icon="icons/32x32/hycon.png", name="Aluminium", ticker="ALI:CMX", buy=r.randrange(100, 9999, 5), sell=r.randrange(100, 9999, 5)),
        ]


class AssetDialog(QDialog):
    def __init__(self, parent=None):
        super(AssetDialog, self).__init__(parent)
        self.setWindowTitle("Choose asset to trade")
        self.setFixedSize(QSize(490, 540))
        self.asset = ''
        self.setStyle(ProxyStyle())
        self.cancel_btn = QPushButton("Cancel")
        self.confirm_btn = QPushButton("Confirm")
        self.confirm_btn.clicked.connect(self.on_confirm)
        self.cancel_btn.clicked.connect(self.on_cancel)
        self.w = TabWidget()
        self.w.addTab(AssetList(get_bin_options()), QIcon("icons/32x32/civic.png"), "Binary options")
        self.w.addTab(AssetList(get_otc_options()), QIcon("icons/32x32/dacsee.png"), "Digital options")
        self.w.addTab(AssetList(get_forex()), QIcon("icons/32x32/c20.png"), "Forex")
        self.w.addTab(AssetList(get_cryptos()), QIcon("icons/32x32/faircoin.png"), "Cryptocurrencies")
        self.w.addTab(AssetList(get_commodities()), QIcon("icons/32x32/galactrum.png"), "Commodities")
        self.w.addTab(AssetList(get_metals()), QIcon("icons/32x32/metal.png"), "Metals")

        layout = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.confirm_btn)
        hbox.addWidget(self.cancel_btn)
        hbox.setAlignment(QtCore.Qt.AlignRight)

        layout.addWidget(self.w, 9)
        layout.addLayout(hbox, 1)
        self.setLayout(layout)

    def get_asset(self):
        self.exec()
        return self.asset

    def on_confirm(self):
        self.asset = self.w.currentWidget().selected_asset
        self.close()

    def on_cancel(self):
        self.asset = None
        self.close()


class AssetList(QWidget):
    def __init__(self, assets):
        super(AssetList, self).__init__()
        self.selected_asset = None
        vbox = QVBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Filter assets...")
        self.asset_list = QListWidget()
        self.asset_list.clicked.connect(self.select_asset)
        for asset in assets:
            item_view = AssetItem(asset)
            item = QListWidgetItem(self.asset_list)
            item.setData(QtCore.Qt.UserRole, item_view)
            item.setSizeHint(item_view.sizeHint())
            self.asset_list.addItem(item)
            self.asset_list.setItemWidget(item, item_view)

        vbox.addWidget(self.search_box)
        vbox.addWidget(self.asset_list)
        self.setLayout(vbox)

    def select_asset(self):
        self.selected_asset = self.asset_list.currentItem().data(QtCore.Qt.UserRole)


class AssetItem(QWidget):
    def __init__(self, asset):
        super(AssetItem, self).__init__()
        hbox = QHBoxLayout()
        self.asset = asset
        icon_wrapper = QLabel()
        icon = QIcon(asset.icon)
        icon_wrapper.setPixmap(icon.pixmap(32))
        hbox.addWidget(icon_wrapper, 1)
        hbox.addWidget(QLabel(asset.name), 5)
        hbox.addWidget(QLabel(str(asset.buy)), 2)
        hbox.addWidget(QLabel(str(asset.sell)), 2)
        self.setLayout(hbox)


class TabBar(QTabBar):
    def tabSizeHint(self, index: int) -> QtCore.QSize:
        s = QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QStylePainter(self)
        opt = QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QStyle.CE_TabBarTabLabel, opt)
            painter.restore()


class TabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar(self))
        self.setTabPosition(QTabWidget.West)


class ProxyStyle(QProxyStyle):
    def drawControl(self, element: QStyle.ControlElement, opt: 'QStyleOption', painter: QtGui.QPainter,
                    widget: typing.Optional[QWidget] = ...) -> None:
        if element == QStyle.CE_TabBarTabLabel:
            ic = self.pixelMetric(QStyle.PM_TabBarIconSize)
            r = QtCore.QRect(opt.rect)
            w = 0 if opt.icon.isNull() else opt.rect.width() + self.pixelMetric(QStyle.PM_TabBarIconSize)
            r.setHeight(opt.fontMetrics.width(opt.text) + w)
            r.moveBottom(opt.rect.bottom())
            opt.rect = r
        QProxyStyle.drawControl(self, element, opt, painter, widget)
