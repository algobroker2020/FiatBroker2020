# @Author: Benjamin Gates
# @Creation: @date
# @Description: This file ....
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel


class Chats(QWidget):
    def __init__(self, parent=None):
        super(Chats, self).__init__(parent)
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('Chats'))
        self.setLayout(hbox)