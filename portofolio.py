# @Author: Benjamin Gates
# @Creation: @date
# @Description: This file ....
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel


class Portofolio(QWidget):
    def __init__(self, parent=None):
        super(Portofolio, self).__init__(parent)
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('Portofolio'))
        self.setLayout(hbox)