# @Author: Benjamin Gates
# @Creation: @date
# @Description: This file ....
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidget

from assetdialog import TabWidget


class Navbar(TabWidget):
    def __init__(self, menu_items):
        super().__init__()
        self.expandWidth = 300
        self.collapseWidth = 50
        self.is_expanded = True
        self.setFixedWidth(300)

        for menu_item in menu_items:
            self.addTab(QListWidget(), QIcon(""), menu_item[1])

    def expand(self):
        if self.is_expanded:
            pass
        self.setFixedWidth(self.expandWidth)
        self.is_expanded = True

    def collapse(self):
        if not self.is_expanded:
            pass
        self.setFixedWidth(self.collapseWidth)
        self.is_expanded = False
