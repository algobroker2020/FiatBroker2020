# @Author: Benjamin Gates
# @Creation: @date
# @Description: This file is the mainwindow of the application
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QToolButton, \
     QToolBar, QTabWidget, QLineEdit

from assetdialog import AssetDialog
from tradingview import TradingView


class TradeRoom(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.asset_dialog = AssetDialog(self)

        self.tool_bar = QToolBar()
        self.btn_add_asset = QPushButton("+")
        self.btn_add_asset.clicked.connect(self.add_symbol)
        self.tool_bar.addWidget(self.btn_add_asset)

        self.tab_layout = QTabWidget()
        vbox = QVBoxLayout()
        vbox.addWidget(self.tool_bar)
        vbox.addWidget(self.tab_layout)

        self.reload_btn, self.account_settings_btn = QToolButton(), QToolButton()
        self.reload_btn.setIcon(QIcon('icons/cil-reload.png'))
        self.reload_btn.setToolTip('Reload the balance')
        self.account_settings_btn.setIcon(QIcon('icons/cil-settings.png'))
        self.account_settings_btn.setToolTip('Open the account settings')
        self.account_balance = QLineEdit('100.000 USD')
        self.account_balance.setFixedWidth(120)
        self.account_balance.setEnabled(False)
        self.balance_label = QLabel('Balance')
        self.balance_label.setFixedWidth(100)
        self.balance_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.trades_count, self.trades_win, self.trades_lost = QLabel('103'), QLabel('75 (72.81%)'), QLabel('28 (27.18%)')
        self.trades_count_label, self.trades_win_label, self.trades_lost_label = QLabel('Trades : '), QLabel('Win : '), QLabel('Lost : ')

        main_layout = QVBoxLayout()
        titlebar_layout = QHBoxLayout()
        hbox1, hbox2, hbox3 = QHBoxLayout(), QHBoxLayout(), QHBoxLayout()

        # Create the trades options Layout
        hbox2.addWidget(self.trades_count_label)
        hbox2.addWidget(self.trades_count)
        hbox2.addWidget(self.trades_win_label)
        hbox2.addWidget(self.trades_win)
        hbox2.addWidget(self.trades_lost_label)
        hbox2.addWidget(self.trades_lost)
        hbox2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Create the balance layout
        hbox3.addWidget(self.balance_label)
        hbox3.addWidget(self.account_balance)
        hbox3.addWidget(self.reload_btn)
        hbox3.addWidget(self.account_settings_btn)
        hbox3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.w_title = QLabel("Trade Room")

        hbox1.addWidget(self.w_title)

        titlebar_layout.addLayout(hbox1, 3)
        titlebar_layout.addLayout(hbox2, 4)
        titlebar_layout.addLayout(hbox3, 3)

        css = open('styles/dark_theme.css', 'r').read()

        self.setStyleSheet(css)
        title_bar = QWidget()
        title_bar.setObjectName("TitleBar")
        title_bar.setLayout(titlebar_layout)

        main_layout.addWidget(title_bar)
        main_layout.addLayout(vbox)

        self.setLayout(main_layout)

    def add_symbol(self):
        asset = self.asset_dialog.get_asset()
        if asset is None:
            return
        self.tab_layout.addTab(TradingView(asset.asset), QIcon(asset.asset.icon), asset.asset.name)
