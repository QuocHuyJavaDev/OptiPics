import numpy as np
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, QRect
from PyQt5.QtWidgets import QMenuBar, QStatusBar, QLabel, QFrame, QPushButton, QWidget, QFileDialog
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import QPixmap
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import cv2
import sys

from ImgEditor import ImgLS
from main import MainWindow


class BasicFunc(MainWindow):
    def LeftRotate(self):
        # self.image = self.tmp
        (h, w) = self.image.shape[:2]
        #   (h, w, d) = self.image.shape
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, -90, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        # tính toán giá trị newWidth, newHeight
        newWidth = int(w * cos + h * sin)
        newHeight = int(w * sin + h * cos)
        # phép tịnh tiến trong Rotation Matrix
        M[0, 2] += (newWidth / 2) - center[0]
        M[1, 2] += (newHeight / 2) - center[1]
        self.image = cv2.warpAffine(self.image, M, (newWidth, newHeight))
        ImgLS.LSFunc.displayImg(self)
    def RightRotate(self):
        # self.image = self.tmp
        (h, w) = self.image.shape[:2]
        #   (h, w, d) = self.image.shape
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, 90, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        # tính toán giá trị newWidth, newHeight
        newWidth = int(w * cos + h * sin)
        newHeight = int(w * sin + h * cos)
        # phép tịnh tiến trong Rotation Matrix
        M[0, 2] += (newWidth / 2) - center[0]
        M[1, 2] += (newHeight / 2) - center[1]
        self.image = cv2.warpAffine(self.image, M, (newWidth, newHeight))
        ImgLS.LSFunc.displayImg(self)

    def FitImg(self):
        qformat = QImage.Format_Indexed8
        if len(self.image.shape) == 3:
            if (self.image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
        img = img.rgbSwapped()
        wFil = self.ui.lblImg.width()
        hFil = self.ui.lblImg.height()
        self.ui.lblImg.setPixmap(QPixmap.fromImage(img).scaled(wFil, hFil))