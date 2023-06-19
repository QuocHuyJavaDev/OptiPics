import cv2
import numpy as np
from main import MainWindow
from PySide2.QtGui import QPixmap, QPainter, QPen
from PySide2.QtCore import Qt, QRect
import sys

from ImgEditor import ImgLS
from main import MainWindow

class ColorizationClass(MainWindow):
    def mauhoa_anh1(self):  # Định nghĩa hàm để màu hóa ảnh bằng phương pháp 1 và hiển thị ảnh lênh label
        self.image = self.tmp
        #Đọc mô hình từ tệp "c1.prototxt" và trọng số từ tệp "c2.caffemodel"
        # để tạo một đối tượng mạng nơ-ron tích chập
        print("[INFO] Nạp mô hình phương pháp 1...")
        net = cv2.dnn.readNetFromCaffe("ImgEditor/Models/c1.prototxt", "ImgEditor/Models/c2.caffemodel")
        # Tải các điểm mô phỏng màu từ tệp "c3.npy" và lưu vào biến pts
        pts = np.load("ImgEditor/Models/c3.npy")

        # add the cluster centers as 1x1 convolutions to the model
        class8 = net.getLayerId("class8_ab")
        conv8 = net.getLayerId("conv8_313_rh")
        pts = pts.transpose().reshape(2, 313, 1, 1)
        net.getLayer(class8).blobs = [pts.astype("float32")]
        net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]


        scaled = self.image.astype("float32") / 255.0
        lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
        resized = cv2.resize(lab, (224, 224))
        L = cv2.split(resized)[0]
        L -= 50
        net.setInput(cv2.dnn.blobFromImage(L))
        ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
        ab = cv2.resize(ab, (self.image.shape[1], self.image.shape[0]))
        L = cv2.split(lab)[0]
        colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
        colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
        colorized = np.clip(colorized, 0, 1)
        colorized = (255 * colorized).astype("uint8")
        self.image = colorized
        ImgLS.LSFunc.displayImg(self)



    def mauhoa_anh2(self):  # Định nghĩa hàm để màu hóa ảnh bằng phương pháp 1 và hiển thị ảnh lênh label
        self.image = self.tmp
        print("[INFO] Nạp mô hình phương pháp 2...")
        net = cv2.dnn.readNetFromCaffe("ImgEditor/Models/c1.prototxt", "ImgEditor/Models/c2_norebal.caffemodel")
        pts = np.load("ImgEditor/Models/c3.npy")

        # add the cluster centers as 1x1 convolutions to the model
        class8 = net.getLayerId("class8_ab")
        conv8 = net.getLayerId("conv8_313_rh")
        pts = pts.transpose().reshape(2, 313, 1, 1)
        net.getLayer(class8).blobs = [pts.astype("float32")]
        net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]


        scaled = self.image.astype("float32") / 255.0
        lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
        resized = cv2.resize(lab, (224, 224))
        L = cv2.split(resized)[0]
        L -= 50
        net.setInput(cv2.dnn.blobFromImage(L))
        ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
        ab = cv2.resize(ab, (self.image.shape[1], self.image.shape[0]))
        L = cv2.split(lab)[0]
        colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
        colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
        colorized = np.clip(colorized, 0, 1)
        colorized = (255 * colorized).astype("uint8")
        self.image = colorized
        ImgLS.LSFunc.displayImg(self)



