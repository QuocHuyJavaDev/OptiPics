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
        self.image = self.tmp
        ImgLS.LSFunc.displayImg(self)

    # Download
    def SaveFunc(self):
        fnameSave, filtered = QFileDialog.getSaveFileName(self, 'Save File', "*.jpg")
        if fnameSave:
            cv2.imwrite(fnameSave, self.image)
        else:
            ImgLS.LSFunc.displayImg(self)


