# @Author: Benjamin Gates
# @Creation: @date
# @Description: This file ....
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel


class Tutorials(QWidget):
    def __init__(self, parent=None):
        super(Tutorials, self).__init__(parent)
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('Vidéos Tutorials'))
        self.setLayout(hbox)