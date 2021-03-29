# @Author: Benjamin Gates
# @Creation: @date
# @Description: This file ....
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel


class Settings(QWidget):
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('Settings'))
        self.setLayout(hbox)