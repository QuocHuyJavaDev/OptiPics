import numpy as np
from rembg import remove
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
        self.tmp = self.image
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
        self.tmp = self.image
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


    def ResizeImg(self):
        self.ui.txtHeight.setEnabled(True)
        self.ui.txtWeight.setEnabled(True)
        self.ui.btnResizeDone.setEnabled(True)


    def ResizeDone(self):
        h = self.ui.txtHeight.toPlainText()
        w = self.ui.txtWeight.toPlainText()
        self.image = cv2.resize(self.image, (int(w), int(h)))
        self.tmp = self.image
        ImgLS.LSFunc.displayImg(self)
        ImgLS.LSFunc.upImgHW(self)

    def Brightness(self):
        self.image = self.tmp
        value = str(self.ui.slideBrightness.value())
        self.ui.lblBrightNum.setText(value)
        datas = self.ui.slideBrightness.value()
        # H:  màu sắc, S: độ bão hòa, V : giá trị
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        hsv = np.array(hsv, dtype=np.float64)
        datas = datas / 100  # dividing by 100 to get in range 0-1.5

        # scale pixel values up or down for channel 1(Saturation)
        hsv[:, :, 1] = hsv[:, :, 1] * datas
        hsv[:, :, 1][hsv[:, :, 1] > 255] = 255  # setting values > 255 to 255.
        # scale pixel values up or down for channel 2(Value)
        hsv[:, :, 2] = hsv[:, :, 2] * datas
        hsv[:, :, 2][hsv[:, :, 2] > 255] = 255  # setting values > 255 to 255.

        hsv = np.array(hsv, dtype=np.uint8)
        self.image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        ImgLS.LSFunc.displayImg(self)

    #TV60s
    def SlideTV60s(self):
        value1 = str(self.ui.slideTV60Val.value())
        self.ui.lblValueNum.setText(value1)
        value2 = str(self.ui.slideTV60Thresh.value())
        self.ui.lblThreshNum.setText(value2)

    def Tv60Func(self):
        self.image = self.tmp
        (height, width) = self.image.shape[:2]
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        thresh = self.ui.slideTV60Thresh.value()
        val = self.ui.slideTV60Val.value()
        # duyệt từng pixrl ảnh
        for i in range(height):
            for j in range(width):
                if np.random.randint(100) <= thresh:
                    if np.random.randint(2) == 0:
                        gray[i, j] = min(gray[i, j] + np.random.randint(0, val + 1),
                                         255)  # adding noise to image and setting values > 255 to 255.

                    else:
                        gray[i, j] = max(gray[i, j] - np.random.randint(0, val + 1),
                                         0)  # subtracting noise to image and setting values < 0 to 0.
        self.image = gray
        ImgLS.LSFunc.displayImg(self)

    def removeBackground(self):
        self.image = self.tmp
        self.image = remove(self.image)
        ImgLS.LSFunc.displayImg(self)

    def writeOnImage(self):
        self.image = self.tmp
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(self.image,
                    text='HELLO',
                    org=(200, 300),  # bottom left
                    fontFace=font,
                    fontScale=5,
                    color=(0, 0, 255),  # BGR on cv2.imshow
                    thickness=3,
                    lineType=cv2.LINE_AA);
        ImgLS.LSFunc.displayImg(self)



