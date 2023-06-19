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
        if absPath == "":
            print("No image choose")
        else:

            self.image = cv2.imread(absPath)
            self.tmpOr = self.image

            imgH = self.image.shape[0]
            imgW = self.image.shape[1]
            #

            x_label = 1510
            y_label = 730
            if imgH > y_label:
                imgW = imgW - (imgH - y_label)
                imgH = y_label
                #self.image = cv2.resize(self.image, (int(imgW), int(imgH)))
            elif imgW > x_label:
                imgH = imgH - (imgW - x_label)
                imgW = x_label
                #self.image = cv2.resize(self.image, (int(imgW), int(imgH)))
            elif imgW > x_label and imgH > y_label:
                imgW = x_label
                imgH = y_label

            self.image = cv2.resize(self.image, (int(imgW), int(imgH)))
            self.tmp = self.image
            self.tmpReset = self.image
            self.ui.lblImg.resize(imgW, imgH)
            #
            qformat = QImage.Format_Indexed8
            if len(self.image.shape) == 3:
                if (self.image.shape[2]) == 4:
                    qformat = QImage.Format_RGBA8888
                else:
                    qformat = QImage.Format_RGB888
            img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
            img = img.rgbSwapped()
            # Fit size img vs label and display
            wOri = self.ui.lblOriginImg.width()
            hOri = self.ui.lblOriginImg.height()
            self.ui.lblOriginImg.setPixmap(QPixmap.fromImage(img).scaled(wOri, hOri))
            self.ui.lblImg.setPixmap(QPixmap.fromImage(img))
            # Get Img name
            fileObject = absPath.split('/')
            imgName = fileObject[len(fileObject) - 1]
            self.ui.lblImgName.setText(imgName)
            LSFunc.upImgHW(self)

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
        #self.ui.lblImg.setPixmap(QPixmap.fromImage(img))

    def upImgHW(self):
        h = self.image.shape[0]
        w = self.image.shape[1]
        self.ui.txtHeight.setPlainText(str(h))
        self.ui.txtWeight.setPlainText(str(w))
