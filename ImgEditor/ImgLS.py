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

from main import MainWindow


class LSFunc(MainWindow):
    def UploadImg(self):
        fname = QFileDialog.getOpenFileName(filter='*.jpg *.png *.tif')
        absPath = fname.__getitem__(0)
        self.image = cv2.imread(absPath)
        self.tmp = self.image
        qformat = QImage.Format_Indexed8
        if len(self.image.shape) == 3:
            if (self.image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
        img = img.rgbSwapped()
        # Fit size img vs label and display
        imgH = QPixmap.fromImage(img).height()
        imgW = QPixmap.fromImage(img).width()
        wOri = self.ui.lblOriginImg.width()
        hOri = self.ui.lblOriginImg.height()
        self.ui.lblOriginImg.setPixmap(QPixmap.fromImage(img).scaled(wOri, hOri))
        wFil = self.ui.lblImg.width()
        hFil = self.ui.lblImg.height()
        if imgW > wFil and imgH > hFil:
            self.ui.lblImg.setPixmap(QPixmap.fromImage(img).scaled(wFil, hFil))
        else:
            self.ui.lblImg.setPixmap(QPixmap.fromImage(img))
        # Get Img name
        fileObject = absPath.split('/')
        imgName = fileObject[len(fileObject) - 1]
        self.ui.lblImgName.setText(imgName)

    def displayImg(self):
        qformat = QImage.Format_Indexed8
        if len(self.image.shape) == 3:
            if (self.image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
        img = img.rgbSwapped()
        self.ui.lblImg.setPixmap(QPixmap.fromImage(img))

