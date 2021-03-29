# @Author: Benjamin Gates
# @Creation: @date
# @Description: This file ....
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel


class PriceAlerts(QWidget):
    def __init__(self, parent=None):
        super(PriceAlerts, self).__init__(parent)
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('Price moves and alerts'))
        self.setLayout(hbox)