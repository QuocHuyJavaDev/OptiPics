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


class ColorFunc(MainWindow):
    # Gray - Histogram
    def GrayFilter(self):
        self.image = self.tmp
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.equalizeHist(self.image)
        ImgLS.LSFunc.displayImg(self)

    # Gray+ - Invert Pixels
    def GrayPlusFilter(self):
        self.image = self.tmp
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = 255 - self.image
        ImgLS.LSFunc.displayImg(self)

    # Sepia
    def SepiaFilter(self):
        self.image = self.tmp
        self.image = np.array(self.image, dtype=np.float64)  # converting to float to prevent loss
        self.image = cv2.transform(self.image, np.matrix([[0.272, 0.534, 0.131],
                                                          [0.349, 0.686, 0.168],
                                                          [0.393, 0.769,
                                                           0.189]]))  # multipying image with special sepia matrix
        self.image[np.where(self.image > 255)] = 255  # normalizing values greater than 255 to 255
        self.image = np.array(self.image, dtype=np.uint8)  # converting back to int
        ImgLS.LSFunc.displayImg(self)

    # Invert Color
    def InvertColor(self):
        self.image = cv2.bitwise_not(self.image)
        ImgLS.LSFunc.displayImg(self)

    # Sharpening
    def SharpeningFilter(self):
        self.image = cv2.detailEnhance(self.image, sigma_s=10, sigma_r=0.15)
        ImgLS.LSFunc.displayImg(self)
