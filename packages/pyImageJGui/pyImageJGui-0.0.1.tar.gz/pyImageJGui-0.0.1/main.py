# -*- coding: utf-8 -*-
"""
@Time : 2023/6/22 00:10
@Author : sdb20200101@gmail.com
@File: main.py
@Software : PyCharm
"""
import multiprocessing
import sys

multiprocessing.freeze_support()
from pyimagej.ui.main_ui import *
from qt_material import apply_stylesheet
from pyimagej.style.qssloader import QSSLoader

if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    window.setMinimumSize(QSize(600, 400))
    window.setCentralWidget(ImageWidget())
    apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True)
    window.setWindowTitle("PyImageJ")
    style_sheet = QSSLoader.read_qss_file("pyimagej/style/main.qss")
    window.setStyleSheet(style_sheet)
    window.show()
    sys.exit(app.exec())
