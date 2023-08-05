# -*- coding: utf-8 -*-
"""
@Time : 2023/6/22 00:10
@Author : sdb20200101@gmail.com
@File: main_ui.py
@Software : PyCharm
"""
import os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import cv2 as cv
from pyimagej.ui.imageView import ImageViewer
from pyimagej.ui.constant import ROI

path = os.path.dirname(os.path.dirname(__file__))


class ImageWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QVBoxLayout(self)
        self.button_layout = QHBoxLayout()

        self.last_open_dir = '/'
        self.roi = ROI.Hand

        self.rectangle_button = Button(QIcon(os.path.join(path, 'icon', 'rectangle.svg')), '', ROI.Rectangle)
        icon_size = self.rectangle_button.style().pixelMetric(QStyle.PixelMetric.PM_ButtonIconSize)
        self.rectangle_button.setIconSize(QSize(icon_size, icon_size))
        self.angle_button = Button(QIcon(os.path.join(path, 'icon', 'angle.svg')), '', ROI.Angle)
        self.angle_button.setIconSize(QSize(icon_size, icon_size))
        self.circle_button = Button(QIcon(os.path.join(path, 'icon', 'circle.svg')), '', ROI.Circle)
        self.circle_button.setIconSize(QSize(icon_size, icon_size))
        self.freehand_button = Button(QIcon(os.path.join(path, 'icon', 'freehand.svg')), '', ROI.Freehand)
        self.freehand_button.setIconSize(QSize(icon_size, icon_size))
        self.line_button = Button(QIcon(os.path.join(path, 'icon', 'line.svg')), '', ROI.Line)
        self.line_button.setIconSize(QSize(icon_size, icon_size))
        self.ellipse_button = Button(QIcon(os.path.join(path, 'icon', 'elliptical.svg')), '', ROI.Ellipse)
        self.ellipse_button.setIconSize(QSize(icon_size, icon_size))
        self.mag_button = Button(QIcon(os.path.join(path, 'icon', 'magnifier.svg')), '', ROI.Magnifier)
        self.mag_button.setIconSize(QSize(icon_size, icon_size))
        self.hand_button = Button(QIcon(os.path.join(path, 'icon', 'hand.svg')), '', ROI.Hand)
        self.hand_button.setIconSize(QSize(icon_size, icon_size))
        self.hand_button.setEnabled(False)
        self.clear_button = QPushButton(QIcon(os.path.join(path, 'icon', 'clear.svg')), '')
        self.clear_button.setIconSize(QSize(icon_size, icon_size))
        self.file_button = QPushButton(QIcon(os.path.join(path, 'icon', 'file.svg')), '')
        self.file_button.setIconSize(QSize(icon_size, icon_size))
        self.button_layout.addWidget(self.rectangle_button)
        self.button_layout.addWidget(self.circle_button)
        self.button_layout.addWidget(self.ellipse_button)
        self.button_layout.addWidget(self.line_button)
        self.button_layout.addWidget(self.angle_button)
        self.button_layout.addWidget(self.freehand_button)
        self.button_layout.addWidget(self.mag_button)
        self.button_layout.addWidget(self.hand_button)
        self.button_layout.addWidget(self.clear_button)
        self.button_layout.addWidget(self.file_button)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setSpacing(0)
        self.button_layout.addStretch(30)

        self.information = QLineEdit()
        self.roi_information = QPushButton("Measure")
        self.information_layout = QHBoxLayout()
        self.information_layout.addWidget(self.information)
        self.information_layout.addWidget(self.roi_information)
        self.figure = ImageViewer(self.information, self.roi, self)
        self.layout.addLayout(self.button_layout, 10)
        self.layout.addLayout(self.information_layout, 10)
        self.layout.addWidget(self.figure, 80)

        self.file_button.clicked.connect(self.file_btn_click)
        self.clear_button.clicked.connect(self.clear_btn_click)
        self.btn_connect()

    def file_btn_click(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择存储路径",  # 标题
            self.last_open_dir  # 起始目录
        )
        self.last_open_dir = os.path.dirname(filePath)
        if filePath:
            img = cv.imread(filePath, 0)
            self.figure.setImageNoQImage(img)
            self.figure.setFocus()

    def btn_connect(self):
        buttons = self.findChildren(Button)
        for button in buttons:
            button.clicked.connect(self.roi_btn_click)

    def roi_btn_click(self):
        sender = self.sender()
        buttons = self.findChildren(Button)
        for button in buttons:
            if button.roi == self.roi:
                button.setEnabled(True)
        sender.setEnabled(False)
        self.roi = sender.roi
        self.figure.roi_state = self.roi

        if sender.roi == ROI.Hand or sender.roi == ROI.Magnifier:
            self.figure.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
            self.figure.mouseMoveEvent = self.figure.mouseMoveEventNoRoi
            self.figure.mousePressEvent = self.figure.mousePressEventNoRoi
            self.figure.mouseReleaseEvent = self.figure.mouseReleaseEventNoRoi
        elif sender.roi == ROI.Rectangle or sender.roi == ROI.Circle or sender.roi == ROI.Line or sender.roi == ROI.Ellipse:
            self.figure.setDragMode(QGraphicsView.DragMode.NoDrag)
            self.figure.mouseMoveEvent = self.figure.mouseMoveEventRoi
            self.figure.mousePressEvent = self.figure.mousePressEventRoi
            self.figure.mouseReleaseEvent = self.figure.mouseReleaseEventRoi
        elif sender.roi == ROI.Angle:
            self.figure.setDragMode(QGraphicsView.DragMode.NoDrag)
            self.figure.mouseMoveEvent = self.figure.mouseMoveAngleEvent
            self.figure.mousePressEvent = self.figure.mousePressAngleEvent
            self.figure.mouseReleaseEvent = self.figure.mouseReleaseAngleEvent

    def clear_btn_click(self):
        for item in self.figure.scene.items():
            if isinstance(item, QGraphicsPixmapItem):
                continue
            self.figure.scene.removeItem(item)

        self.figure.roi = None


class Button(QPushButton):
    def __init__(self, icon: QIcon, string: str, roi: ROI):
        QPushButton.__init__(self, icon, string)
        self.roi = roi
