import sys

import cv2
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QDialog, QLabel, QLineEdit, \
    QComboBox, QColorDialog

from ImgEditor import ImgLS


class MultiInputDialog(QDialog):
    def __init__(self,image, x_pos, y_pos, parent=None):
        super(MultiInputDialog, self).__init__(parent)
        self.setWindowTitle("Text on image")
        self.xpos = x_pos
        self.ypos = y_pos
        self.img = image
        self.labels = ['Text:']
        self.line_edits = []

        layout = QVBoxLayout()

        for label_text in self.labels:
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.line_edits.append(line_edit)
            layout.addWidget(label)
            layout.addWidget(line_edit)

        label1 = QLabel('Font:')
        self.combo_box1 = QComboBox()
        self.combo_box1.addItem("HERSHEY_SIMPLEX")
        self.combo_box1.addItem("HERSHEY_PLAIN")
        self.combo_box1.addItem("HERSHEY_DUPLEX")
        self.combo_box1.addItem("HERSHEY_COMPLEX")
        self.combo_box1.addItem("HERSHEY_TRIPLEX")
        self.combo_box1.addItem("HERSHEY_COMPLEX_SMALL")
        self.combo_box1.addItem("HERSHEY_SCRIPT_SIMPLEX")
        self.combo_box1.addItem("HERSHEY_SCRIPT_COMPLEX")
        layout.addWidget(label1)
        layout.addWidget(self.combo_box1)

        label2 = QLabel('Size:')
        self.combo_box2 = QComboBox()
        self.combo_box2.addItem("0.5")
        self.combo_box2.addItem("1")
        self.combo_box2.addItem("1.5")
        self.combo_box2.addItem("2")
        self.combo_box2.addItem("2.5")
        self.combo_box2.addItem("3")
        self.combo_box2.addItem("3.5")
        self.combo_box2.addItem("4")
        self.combo_box2.addItem("4.5")
        self.combo_box2.addItem("5")
        layout.addWidget(label2)
        layout.addWidget(self.combo_box2)

        self.button1 = QPushButton("Color")
        self.button1.clicked.connect(self.changeColor)
        layout.addWidget(self.button1)
        self.blue = 0
        self.green = 0
        self.red = 0

        button = QPushButton("Submit")
        button.clicked.connect(self.submit)
        layout.addWidget(button)

        self.setLayout(layout)

    def changeColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.blue = color.blue()
            self.green = color.green()
            self.red = color.red()
            self.button1.setStyleSheet(u"#button1 {\n"
                                       "	border-radius: 27px;\n"
                                       "	border : 2px solid #636363;\n"
                                       "	background-color: %s;\n"
                                       "}\n"
                                       "\n"
                                       "" % color.name())


    def submit(self):
        name = self.line_edits[0].text()
        sizeText = str(self.combo_box2.currentText())
        index = self.combo_box1.currentIndex()
        print(index)
        cv2.putText(self.img,
                    text=name,
                    org=(self.xpos, self.ypos),  # bottom left
                    fontFace=index,
                    fontScale=float(sizeText),
                    color=(int(self.blue), int(self.green), int(self.red)),  # BGR on cv2.imshow
                    thickness=2,
                    lineType=cv2.LINE_AA);

        self.close()