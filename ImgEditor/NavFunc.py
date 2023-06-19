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


class NavbarFunc(MainWindow):
    # Reset
    def ResetFunc(self):
        self.image = self.tmpReset
        self.tmp = self.image
        ImgLS.LSFunc.displayImg(self)

    # Download
    def SaveFunc(self):
        fnameSave, filtered = QFileDialog.getSaveFileName(self, 'Save File', "*.jpg")
        if fnameSave:
            cv2.imwrite(fnameSave, self.image)
        else:
            ImgLS.LSFunc.displayImg(self)

    #Save
    def DoneFunc(self):
        self.tmp = self.image;
        qformat = QImage.Format_Indexed8
        if len(self.image.shape) == 3:
            if (self.image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
        img = img.rgbSwapped()
        wOri = self.ui.lblOriginImg.width()
        hOri = self.ui.lblOriginImg.height()
        self.ui.lblOriginImg.setPixmap(QPixmap.fromImage(img).scaled(wOri, hOri))


