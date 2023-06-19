# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainyEOQUV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1904, 988)
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.mainwidget = QWidget(MainWindow)
        self.mainwidget.setObjectName(u"mainwidget")
        self.mainwidget.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.FrameMain = QFrame(self.mainwidget)
        self.FrameMain.setObjectName(u"FrameMain")
        self.FrameMain.setGeometry(QRect(-1, 69, 1921, 941))
        self.FrameMain.setFrameShape(QFrame.StyledPanel)
        self.FrameMain.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.FrameMain)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -21, 1921, 951))
        self.imgPage = QWidget()
        self.imgPage.setObjectName(u"imgPage")
        self.imgpage = QFrame(self.imgPage)
        self.imgpage.setObjectName(u"imgpage")
        self.imgpage.setGeometry(QRect(9, 10, 1921, 931))
        self.imgpage.setFrameShape(QFrame.StyledPanel)
        self.imgpage.setFrameShadow(QFrame.Raised)
        self.headerFrame = QFrame(self.imgpage)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setGeometry(QRect(-10, 10, 1920, 60))
        self.headerFrame.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.btnAdd = QPushButton(self.headerFrame)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(62, 0, 61, 61))
        self.btnAdd.setAutoFillBackground(False)
        self.btnAdd.setStyleSheet(u"border: 0px")
        icon = QIcon()
        icon.addFile(u"icon/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAdd.setIcon(icon)
        self.btnAdd.setIconSize(QSize(40, 40))
        self.btnReset = QPushButton(self.headerFrame)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setGeometry(QRect(130, 0, 61, 61))
        self.btnReset.setAutoFillBackground(False)
        self.btnReset.setStyleSheet(u"border: 0px")
        icon1 = QIcon()
        icon1.addFile(u"icon/reset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnReset.setIcon(icon1)
        self.btnReset.setIconSize(QSize(35, 35))
        self.btnDone = QPushButton(self.headerFrame)
        self.btnDone.setObjectName(u"btnDone")
        self.btnDone.setGeometry(QRect(200, 0, 61, 61))
        self.btnDone.setAutoFillBackground(False)
        self.btnDone.setStyleSheet(u"border: 0px")
        icon2 = QIcon()
        icon2.addFile(u"icon/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDone.setIcon(icon2)
        self.btnDone.setIconSize(QSize(35, 35))
        self.btnIconName = QPushButton(self.headerFrame)
        self.btnIconName.setObjectName(u"btnIconName")
        self.btnIconName.setGeometry(QRect(850, -3, 51, 61))
        self.btnIconName.setStyleSheet(u"border: 0px;\n"
"alignt: center;")
        icon3 = QIcon()
        icon3.addFile(u"icon/picName.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnIconName.setIcon(icon3)
        self.btnIconName.setIconSize(QSize(35, 35))
        self.lblImgName = QLabel(self.headerFrame)
        self.lblImgName.setObjectName(u"lblImgName")
        self.lblImgName.setGeometry(QRect(900, 15, 251, 31))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.lblImgName.setFont(font1)
        self.lblImgName.setStyleSheet(u"color: #FFFFFF;")
        self.btnDownload = QPushButton(self.headerFrame)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setGeometry(QRect(1760, 10, 93, 41))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.btnDownload.setFont(font2)
        self.btnDownload.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(3, 134, 0);\n"
"color: #FFFFFF;")
        icon4 = QIcon()
        icon4.addFile(u"icon/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDownload.setIcon(icon4)
        self.btnDownload.setIconSize(QSize(30, 30))
        self.ToolFrame = QFrame(self.imgpage)
        self.ToolFrame.setObjectName(u"ToolFrame")
        self.ToolFrame.setGeometry(QRect(-10, 75, 371, 891))
        self.ToolFrame.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"border: 0px;")
        self.ToolFrame.setFrameShape(QFrame.StyledPanel)
        self.ToolFrame.setFrameShadow(QFrame.Raised)
        self.lblTool = QLabel(self.ToolFrame)
        self.lblTool.setObjectName(u"lblTool")
        self.lblTool.setGeometry(QRect(20, 10, 71, 21))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.lblTool.setFont(font3)
        self.lblTool.setStyleSheet(u"color: #838383;")
        self.ToolSA = QScrollArea(self.ToolFrame)
        self.ToolSA.setObjectName(u"ToolSA")
        self.ToolSA.setGeometry(QRect(0, 56, 387, 801))
        self.ToolSA.setStyleSheet(u"#ToolSA {\n"
"border: 0px;\n"
"border-top: 2px solid white;\n"
"padding-top: 0px;\n"
"}\n"
"")
        self.ToolSA.setWidgetResizable(True)
        self.ToolSA.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -120, 383, 1134))
        self.scrollAreaWidgetContents.setStyleSheet(u"border: 0px;")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.basicWid2 = QWidget(self.scrollAreaWidgetContents)
        self.basicWid2.setObjectName(u"basicWid2")
        self.basicWid2.setMaximumSize(QSize(361, 16777215))
        self.basicWid2.setStyleSheet(u"\n"
"#basicWid2 {\n"
"background-color: rgb(30, 30, 30);\n"
"border: 0px;\n"
"\n"
"}\n"
"\n"
"#basicWid2 QPushButton {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"	background-color: rgb(30, 30, 30);\n"
"}\n"
"#basicWid2 QPushButton:hover {\n"
"	background-color: rgb(49, 49, 49);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.basicWid2)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rotateWid = QWidget(self.basicWid2)
        self.rotateWid.setObjectName(u"rotateWid")
        self.rotateWid.setMinimumSize(QSize(0, 50))
        self.rotateWid.setStyleSheet(u"#rotateWid {\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 0px;\n"
"	\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.rotateWid)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lblRotate = QLabel(self.rotateWid)
        self.lblRotate.setObjectName(u"lblRotate")
        font4 = QFont()
        font4.setPointSize(11)
        self.lblRotate.setFont(font4)
        self.lblRotate.setStyleSheet(u"#lblRotate {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.lblRotate)

        self.btnLeft = QPushButton(self.rotateWid)
        self.btnLeft.setObjectName(u"btnLeft")
        self.btnLeft.setMinimumSize(QSize(0, 50))
        self.btnLeft.setMaximumSize(QSize(75, 16777215))
        self.btnLeft.setLayoutDirection(Qt.LeftToRight)
        self.btnLeft.setStyleSheet(u"padding-right:15px;")
        icon5 = QIcon()
        icon5.addFile(u"icon/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLeft.setIcon(icon5)
        self.btnLeft.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.btnLeft, 0, Qt.AlignRight)

        self.btnRight = QPushButton(self.rotateWid)
        self.btnRight.setObjectName(u"btnRight")
        self.btnRight.setMinimumSize(QSize(0, 50))
        self.btnRight.setMaximumSize(QSize(75, 16777215))
        self.btnRight.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"icon/rightRotate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRight.setIcon(icon6)
        self.btnRight.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.btnRight)


        self.verticalLayout.addWidget(self.rotateWid)

        self.btnFit = QPushButton(self.basicWid2)
        self.btnFit.setObjectName(u"btnFit")
        self.btnFit.setMinimumSize(QSize(0, 50))
        self.btnFit.setFont(font4)
        self.btnFit.setStyleSheet(u"#btnResize {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout.addWidget(self.btnFit)

        self.btnWrite = QPushButton(self.basicWid2)
        self.btnWrite.setObjectName(u"btnWrite")
        self.btnWrite.setMinimumSize(QSize(0, 50))
        self.btnWrite.setFont(font4)
        self.btnWrite.setStyleSheet(u"#btnResize {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout.addWidget(self.btnWrite)

        self.btnResize = QPushButton(self.basicWid2)
        self.btnResize.setObjectName(u"btnResize")
        self.btnResize.setMinimumSize(QSize(0, 50))
        self.btnResize.setFont(font4)
        self.btnResize.setStyleSheet(u"#btnResize {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout.addWidget(self.btnResize)

        self.btnCrop = QPushButton(self.basicWid2)
        self.btnCrop.setObjectName(u"btnCrop")
        self.btnCrop.setMinimumSize(QSize(0, 50))
        self.btnCrop.setFont(font4)
        self.btnCrop.setStyleSheet(u"#btnResize {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout.addWidget(self.btnCrop)

        self.btnRemoveBg = QPushButton(self.basicWid2)
        self.btnRemoveBg.setObjectName(u"btnRemoveBg")
        self.btnRemoveBg.setMinimumSize(QSize(0, 50))
        self.btnRemoveBg.setFont(font4)
        self.btnRemoveBg.setStyleSheet(u"#btnCrop {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout.addWidget(self.btnRemoveBg)


        self.gridLayout.addWidget(self.basicWid2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 248, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btnColorization_2 = QPushButton(self.widget_4)
        self.btnColorization_2.setObjectName(u"btnColorization_2")
        self.btnColorization_2.setMinimumSize(QSize(361, 50))
        font5 = QFont()
        font5.setPointSize(12)
        self.btnColorization_2.setFont(font5)
        self.btnColorization_2.setStyleSheet(u"#btnColorization_2 {\n"
"border: 0px;\n"
"color: rgb(216, 216, 216);\n"
"text-align: left;\n"
"padding-left: 20px;\n"
"border-bottom: 1px solid #636363;\n"
"}\n"
"\n"
"#btnColorization_2:hover {\n"
"	background-color: rgb(71, 71, 71);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icon/colorzition.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnColorization_2.setIcon(icon7)
        self.btnColorization_2.setIconSize(QSize(30, 30))
        self.btnColorization_2.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.btnColorization_2)


        self.gridLayout.addWidget(self.widget_4, 5, 0, 1, 1)

        self.FilterWid2 = QWidget(self.scrollAreaWidgetContents)
        self.FilterWid2.setObjectName(u"FilterWid2")
        self.FilterWid2.setStyleSheet(u"#FilterWid2 {\n"
"background-color: rgb(30, 30, 30);\n"
"border: 0px;\n"
"}\n"
"#FilterWid2 QPushButton {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"	background-color: rgb(30, 30, 30);\n"
"}\n"
"#FilterWid2 QPushButton:hover {\n"
"	background-color: rgb(49, 49, 49);\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.FilterWid2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnGray = QPushButton(self.FilterWid2)
        self.btnGray.setObjectName(u"btnGray")
        self.btnGray.setMinimumSize(QSize(0, 50))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setWeight(50)
        self.btnGray.setFont(font6)
        self.btnGray.setStyleSheet(u"#btnRotate {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	background-color: rgb(30, 30, 30);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnGray)

        self.btnGray2 = QPushButton(self.FilterWid2)
        self.btnGray2.setObjectName(u"btnGray2")
        self.btnGray2.setMinimumSize(QSize(0, 50))
        self.btnGray2.setFont(font4)
        self.btnGray2.setStyleSheet(u"#btnResize {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnGray2)

        self.btnHDR = QPushButton(self.FilterWid2)
        self.btnHDR.setObjectName(u"btnHDR")
        self.btnHDR.setMinimumSize(QSize(0, 50))
        self.btnHDR.setFont(font4)
        self.btnHDR.setStyleSheet(u"#btnCrop {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnHDR)

        self.btnSepia = QPushButton(self.FilterWid2)
        self.btnSepia.setObjectName(u"btnSepia")
        self.btnSepia.setMinimumSize(QSize(0, 50))
        self.btnSepia.setFont(font4)
        self.btnSepia.setStyleSheet(u"#btnCrop {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnSepia)

        self.btnInvert = QPushButton(self.FilterWid2)
        self.btnInvert.setObjectName(u"btnInvert")
        self.btnInvert.setMinimumSize(QSize(0, 50))
        self.btnInvert.setFont(font4)
        self.btnInvert.setStyleSheet(u"#btnCrop {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnInvert)

        self.btnGrayPencil = QPushButton(self.FilterWid2)
        self.btnGrayPencil.setObjectName(u"btnGrayPencil")
        self.btnGrayPencil.setMinimumSize(QSize(0, 50))
        self.btnGrayPencil.setFont(font4)
        self.btnGrayPencil.setStyleSheet(u"#btnCrop {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnGrayPencil)

        self.btnColorPencil = QPushButton(self.FilterWid2)
        self.btnColorPencil.setObjectName(u"btnColorPencil")
        self.btnColorPencil.setMinimumSize(QSize(0, 50))
        self.btnColorPencil.setFont(font4)
        self.btnColorPencil.setStyleSheet(u"#btnCrop {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnColorPencil)

        self.btnCartoon = QPushButton(self.FilterWid2)
        self.btnCartoon.setObjectName(u"btnCartoon")
        self.btnCartoon.setMinimumSize(QSize(0, 50))
        self.btnCartoon.setFont(font4)
        self.btnCartoon.setStyleSheet(u"#btnCrop {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnCartoon)

        self.btnWaterCartoon = QPushButton(self.FilterWid2)
        self.btnWaterCartoon.setObjectName(u"btnWaterCartoon")
        self.btnWaterCartoon.setMinimumSize(QSize(0, 50))
        self.btnWaterCartoon.setFont(font4)
        self.btnWaterCartoon.setStyleSheet(u"#btnCrop {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnWaterCartoon)

        self.btnShaperning = QPushButton(self.FilterWid2)
        self.btnShaperning.setObjectName(u"btnShaperning")
        self.btnShaperning.setMinimumSize(QSize(0, 50))
        self.btnShaperning.setFont(font4)
        self.btnShaperning.setStyleSheet(u"#btnCrop {\n"
"	border: 0px;\n"
"	color: rgb(216, 216, 216);\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnShaperning)


        self.gridLayout.addWidget(self.FilterWid2, 3, 0, 1, 1)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnFilter = QPushButton(self.widget_3)
        self.btnFilter.setObjectName(u"btnFilter")
        self.btnFilter.setMinimumSize(QSize(361, 50))
        self.btnFilter.setFont(font5)
        self.btnFilter.setStyleSheet(u"#btnFilter {\n"
"border: 0px;\n"
"color: rgb(216, 216, 216);\n"
"text-align: left;\n"
"padding-left: 20px;\n"
"border-bottom: 1px solid #636363;\n"
"}\n"
"\n"
"#btnFilter:hover {\n"
"	background-color: rgb(71, 71, 71);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icon/filter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnFilter.setIcon(icon8)
        self.btnFilter.setIconSize(QSize(30, 30))
        self.btnFilter.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnFilter)


        self.gridLayout.addWidget(self.widget_3, 2, 0, 1, 1)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border-bottom: 1px solid #636363;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnBasic = QPushButton(self.widget)
        self.btnBasic.setObjectName(u"btnBasic")
        self.btnBasic.setMinimumSize(QSize(361, 50))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setWeight(50)
        self.btnBasic.setFont(font7)
        self.btnBasic.setLayoutDirection(Qt.LeftToRight)
        self.btnBasic.setStyleSheet(u"#btnBasic {\n"
"border: 0px;\n"
"color: rgb(216, 216, 216);\n"
"text-align: left;\n"
"padding-left: 20px;\n"
"border-bottom: 1px solid #636363;\n"
"}\n"
"\n"
"#btnBasic:hover {\n"
"	background-color: rgb(71, 71, 71);\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"icon/basic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBasic.setIcon(icon9)
        self.btnBasic.setIconSize(QSize(30, 30))
        self.btnBasic.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnBasic)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btnColorization = QPushButton(self.widget_5)
        self.btnColorization.setObjectName(u"btnColorization")
        self.btnColorization.setMinimumSize(QSize(361, 50))
        self.btnColorization.setFont(font5)
        self.btnColorization.setStyleSheet(u"#btnColorization {\n"
"border: 0px;\n"
"color: rgb(216, 216, 216);\n"
"text-align: left;\n"
"padding-left: 20px;\n"
"border-bottom: 1px solid #636363;\n"
"}\n"
"\n"
"#btnColorization:hover {\n"
"	background-color: rgb(71, 71, 71);\n"
"}")
        self.btnColorization.setIcon(icon7)
        self.btnColorization.setIconSize(QSize(30, 30))
        self.btnColorization.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.btnColorization)


        self.gridLayout.addWidget(self.widget_5, 4, 0, 1, 1)

        self.ToolSA.setWidget(self.scrollAreaWidgetContents)
        self.imgFrame = QFrame(self.imgpage)
        self.imgFrame.setObjectName(u"imgFrame")
        self.imgFrame.setGeometry(QRect(367, 75, 1541, 861))
        self.imgFrame.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border-radius: 20px;")
        self.imgFrame.setFrameShape(QFrame.StyledPanel)
        self.imgFrame.setFrameShadow(QFrame.Raised)
        self.lblOriginImg = QLabel(self.imgFrame)
        self.lblOriginImg.setObjectName(u"lblOriginImg")
        self.lblOriginImg.setGeometry(QRect(10, 735, 161, 115))
        self.lblOriginImg.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.txtWeight = QPlainTextEdit(self.imgFrame)
        self.txtWeight.setObjectName(u"txtWeight")
        self.txtWeight.setGeometry(QRect(250, 740, 121, 41))
        self.txtWeight.setFont(font4)
        self.txtWeight.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"color: rgb(255, 255, 255);\n"
"padding-top: 5px;\n"
"padding-left: 10px;")
        self.lblWeight = QLabel(self.imgFrame)
        self.lblWeight.setObjectName(u"lblWeight")
        self.lblWeight.setGeometry(QRect(190, 740, 51, 41))
        font8 = QFont()
        font8.setFamily(u"Arial Narrow")
        font8.setPointSize(12)
        self.lblWeight.setFont(font8)
        self.lblWeight.setStyleSheet(u"color: #FFFFFF;")
        self.lblHeight = QLabel(self.imgFrame)
        self.lblHeight.setObjectName(u"lblHeight")
        self.lblHeight.setGeometry(QRect(190, 800, 51, 41))
        self.lblHeight.setFont(font8)
        self.lblHeight.setStyleSheet(u"color: #FFFFFF;")
        self.txtHeight = QPlainTextEdit(self.imgFrame)
        self.txtHeight.setObjectName(u"txtHeight")
        self.txtHeight.setGeometry(QRect(250, 800, 121, 41))
        self.txtHeight.setFont(font4)
        self.txtHeight.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"color: rgb(255, 255, 255);\n"
"padding-top: 5px;\n"
"padding-left: 10px;")
        self.btnResizeDone = QPushButton(self.imgFrame)
        self.btnResizeDone.setObjectName(u"btnResizeDone")
        self.btnResizeDone.setGeometry(QRect(390, 770, 93, 41))
        self.btnResizeDone.setFont(font8)
        self.btnResizeDone.setStyleSheet(u"#btnResizeDone {\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frameBrightness = QFrame(self.imgFrame)
        self.frameBrightness.setObjectName(u"frameBrightness")
        self.frameBrightness.setGeometry(QRect(510, 750, 411, 81))
        self.frameBrightness.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frameBrightness.setFrameShape(QFrame.StyledPanel)
        self.frameBrightness.setFrameShadow(QFrame.Raised)
        self.slideBrightness = QSlider(self.frameBrightness)
        self.slideBrightness.setObjectName(u"slideBrightness")
        self.slideBrightness.setGeometry(QRect(60, 42, 331, 21))
        self.slideBrightness.setOrientation(Qt.Horizontal)
        self.lblBrightNum = QLabel(self.frameBrightness)
        self.lblBrightNum.setObjectName(u"lblBrightNum")
        self.lblBrightNum.setGeometry(QRect(30, 37, 31, 31))
        font9 = QFont()
        font9.setFamily(u"Arial Narrow")
        font9.setPointSize(14)
        font9.setBold(True)
        font9.setWeight(75)
        self.lblBrightNum.setFont(font9)
        self.lblBrightNum.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblBrightness = QLabel(self.frameBrightness)
        self.lblBrightness.setObjectName(u"lblBrightness")
        self.lblBrightness.setGeometry(QRect(173, 0, 91, 31))
        font10 = QFont()
        font10.setFamily(u"Arial Narrow")
        font10.setPointSize(12)
        font10.setBold(True)
        font10.setWeight(75)
        self.lblBrightness.setFont(font10)
        self.lblBrightness.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frameTV60 = QFrame(self.imgFrame)
        self.frameTV60.setObjectName(u"frameTV60")
        self.frameTV60.setGeometry(QRect(950, 750, 531, 81))
        self.frameTV60.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frameTV60.setFrameShape(QFrame.StyledPanel)
        self.frameTV60.setFrameShadow(QFrame.Raised)
        self.slideTV60Thresh = QSlider(self.frameTV60)
        self.slideTV60Thresh.setObjectName(u"slideTV60Thresh")
        self.slideTV60Thresh.setGeometry(QRect(120, 50, 331, 21))
        self.slideTV60Thresh.setOrientation(Qt.Horizontal)
        self.lblThreshNum = QLabel(self.frameTV60)
        self.lblThreshNum.setObjectName(u"lblThreshNum")
        self.lblThreshNum.setGeometry(QRect(90, 45, 31, 31))
        self.lblThreshNum.setFont(font9)
        self.lblThreshNum.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblTV60 = QLabel(self.frameTV60)
        self.lblTV60.setObjectName(u"lblTV60")
        self.lblTV60.setGeometry(QRect(10, 20, 61, 41))
        self.lblTV60.setFont(font10)
        self.lblTV60.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.slideTV60Val = QSlider(self.frameTV60)
        self.slideTV60Val.setObjectName(u"slideTV60Val")
        self.slideTV60Val.setGeometry(QRect(120, 10, 331, 21))
        self.slideTV60Val.setOrientation(Qt.Horizontal)
        self.lblValueNum = QLabel(self.frameTV60)
        self.lblValueNum.setObjectName(u"lblValueNum")
        self.lblValueNum.setGeometry(QRect(90, 5, 31, 31))
        self.lblValueNum.setFont(font9)
        self.lblValueNum.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnTV60 = QPushButton(self.frameTV60)
        self.btnTV60.setObjectName(u"btnTV60")
        self.btnTV60.setGeometry(QRect(464, 20, 61, 41))
        font11 = QFont()
        font11.setFamily(u"Arial Narrow")
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setWeight(75)
        self.btnTV60.setFont(font11)
        self.btnTV60.setStyleSheet(u"#btnTV60 {\n"
"	;\n"
"	background-color: rgb(104, 104, 104);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frameFilterImg = QFrame(self.imgFrame)
        self.frameFilterImg.setObjectName(u"frameFilterImg")
        self.frameFilterImg.setGeometry(QRect(10, 0, 1510, 730))
        self.frameFilterImg.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frameFilterImg.setFrameShape(QFrame.StyledPanel)
        self.frameFilterImg.setFrameShadow(QFrame.Raised)
        self.lblImg = QLabel(self.frameFilterImg)
        self.lblImg.setObjectName(u"lblImg")
        self.lblImg.setGeometry(QRect(300, 0, 0, 0))
        self.lblImg.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frameFilterImg.raise_()
        self.lblOriginImg.raise_()
        self.txtWeight.raise_()
        self.lblWeight.raise_()
        self.lblHeight.raise_()
        self.txtHeight.raise_()
        self.btnResizeDone.raise_()
        self.frameBrightness.raise_()
        self.frameTV60.raise_()
        self.stackedWidget.addWidget(self.imgPage)
        self.videoPage = QWidget()
        self.videoPage.setObjectName(u"videoPage")
        self.headerFrame_3 = QFrame(self.videoPage)
        self.headerFrame_3.setObjectName(u"headerFrame_3")
        self.headerFrame_3.setGeometry(QRect(0, 21, 1920, 60))
        self.headerFrame_3.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"")
        self.headerFrame_3.setFrameShape(QFrame.StyledPanel)
        self.headerFrame_3.setFrameShadow(QFrame.Raised)
        self.btnAddVideo = QPushButton(self.headerFrame_3)
        self.btnAddVideo.setObjectName(u"btnAddVideo")
        self.btnAddVideo.setGeometry(QRect(20, 0, 61, 61))
        self.btnAddVideo.setAutoFillBackground(False)
        self.btnAddVideo.setStyleSheet(u"border: 0px")
        self.btnAddVideo.setIcon(icon)
        self.btnAddVideo.setIconSize(QSize(40, 40))
        self.toolsWid = QWidget(self.videoPage)
        self.toolsWid.setObjectName(u"toolsWid")
        self.toolsWid.setGeometry(QRect(-1, 84, 318, 591))
        self.toolsWid.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"")
        self.btnVidtoCar = QPushButton(self.toolsWid)
        self.btnVidtoCar.setObjectName(u"btnVidtoCar")
        self.btnVidtoCar.setGeometry(QRect(20, 60, 281, 41))
        self.btnVidtoCar.setFont(font10)
        self.btnVidtoCar.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(3, 134, 0);\n"
"color: #FFFFFF;")
        self.videoWid = QWidget(self.videoPage)
        self.videoWid.setObjectName(u"videoWid")
        self.videoWid.setGeometry(QRect(321, 84, 1581, 591))
        self.videoWid.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"")
        self.btnplay = QPushButton(self.videoPage)
        self.btnplay.setObjectName(u"btnplay")
        self.btnplay.setGeometry(QRect(130, 740, 61, 61))
        font12 = QFont()
        font12.setPointSize(10)
        self.btnplay.setFont(font12)
        self.btnplay.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(80, 80, 80);\n"
"color: #FFFFFF;")
        self.horizontalSlider = QSlider(self.videoPage)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(210, 760, 1551, 22))
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.btnClear = QPushButton(self.videoPage)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(1750, 870, 131, 41))
        self.btnClear.setFont(font2)
        self.btnClear.setStyleSheet(u"border-radius: 15px;\n"
"background-color: red;\n"
"color: #FFFFFF;")
        self.btnStart = QPushButton(self.videoPage)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(780, 690, 151, 31))
        self.btnStart.setFont(font12)
        self.btnStart.setStyleSheet(u"border-radius: 15px;\n"
"border-right-radius:0px;\n"
"background-color: rgb(80, 80, 80);\n"
"color: #FFFFFF;")
        self.btnEnd = QPushButton(self.videoPage)
        self.btnEnd.setObjectName(u"btnEnd")
        self.btnEnd.setGeometry(QRect(930, 690, 151, 31))
        self.btnEnd.setFont(font12)
        self.btnEnd.setStyleSheet(u"border-radius: 15px;\n"
"border-right-radius:0px;\n"
"background-color: rgb(80, 80, 80);\n"
"color: #FFFFFF;")
        self.lblStatus = QLabel(self.videoPage)
        self.lblStatus.setObjectName(u"lblStatus")
        self.lblStatus.setGeometry(QRect(4, 910, 1351, 31))
        self.lblStatus.setFont(font12)
        self.lblStatus.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;")
        self.combobox_degree = QComboBox(self.videoPage)
        self.combobox_degree.setObjectName(u"combobox_degree")
        self.combobox_degree.setGeometry(QRect(320, 830, 291, 41))
        self.combobox_degree.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"color: #FFFFFF;")
        self.lblRotateVideo = QLabel(self.videoPage)
        self.lblRotateVideo.setObjectName(u"lblRotateVideo")
        self.lblRotateVideo.setGeometry(QRect(60, 830, 241, 41))
        self.lblRotateVideo.setFont(font12)
        self.lblRotateVideo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;")
        self.btnSubclipVid = QPushButton(self.videoPage)
        self.btnSubclipVid.setObjectName(u"btnSubclipVid")
        self.btnSubclipVid.setGeometry(QRect(740, 830, 241, 41))
        self.btnSubclipVid.setFont(font4)
        self.btnSubclipVid.setStyleSheet(u"border-radius: 15px;\n"
"border-right-radius:0px;\n"
"background-color: rgb(80, 80, 80);\n"
"color: #FFFFFF;")
        self.btnSubclipAu = QPushButton(self.videoPage)
        self.btnSubclipAu.setObjectName(u"btnSubclipAu")
        self.btnSubclipAu.setGeometry(QRect(1010, 830, 241, 41))
        self.btnSubclipAu.setFont(font4)
        self.btnSubclipAu.setStyleSheet(u"border-radius: 15px;\n"
"border-right-radius:0px;\n"
"background-color: rgb(80, 80, 80);\n"
"color: #FFFFFF;")
        self.stackedWidget.addWidget(self.videoPage)
        self.paintPage = QWidget()
        self.paintPage.setObjectName(u"paintPage")
        self.widget_2 = QWidget(self.paintPage)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-10, 80, 1911, 861))
        self.lblPaper = QLabel(self.widget_2)
        self.lblPaper.setObjectName(u"lblPaper")
        self.lblPaper.setGeometry(QRect(19, 10, 1891, 841))
        self.lblPaper.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.headerFrame_2 = QFrame(self.paintPage)
        self.headerFrame_2.setObjectName(u"headerFrame_2")
        self.headerFrame_2.setGeometry(QRect(-10, 21, 1920, 60))
        self.headerFrame_2.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"")
        self.headerFrame_2.setFrameShape(QFrame.StyledPanel)
        self.headerFrame_2.setFrameShadow(QFrame.Raised)
        self.btnResetPaint = QPushButton(self.headerFrame_2)
        self.btnResetPaint.setObjectName(u"btnResetPaint")
        self.btnResetPaint.setGeometry(QRect(30, 0, 61, 61))
        self.btnResetPaint.setAutoFillBackground(False)
        self.btnResetPaint.setStyleSheet(u"border: 0px")
        self.btnResetPaint.setIcon(icon1)
        self.btnResetPaint.setIconSize(QSize(35, 35))
        self.btnSavePaint = QPushButton(self.headerFrame_2)
        self.btnSavePaint.setObjectName(u"btnSavePaint")
        self.btnSavePaint.setGeometry(QRect(1760, 10, 93, 41))
        self.btnSavePaint.setFont(font2)
        self.btnSavePaint.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(3, 134, 0);\n"
"color: #FFFFFF;")
        self.btnSavePaint.setIcon(icon4)
        self.btnSavePaint.setIconSize(QSize(30, 30))
        self.btnPen1 = QPushButton(self.headerFrame_2)
        self.btnPen1.setObjectName(u"btnPen1")
        self.btnPen1.setGeometry(QRect(840, 0, 61, 61))
        self.btnPen1.setAutoFillBackground(False)
        self.btnPen1.setStyleSheet(u"#btnPen1 {\n"
"	border:0px;\n"
"\n"
"}\n"
"\n"
"#btnPen1:hover {\n"
"	\n"
"	background-color: rgb(39, 39, 39);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"icon/pen0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPen1.setIcon(icon10)
        self.btnPen1.setIconSize(QSize(35, 35))
        self.btnPen2 = QPushButton(self.headerFrame_2)
        self.btnPen2.setObjectName(u"btnPen2")
        self.btnPen2.setGeometry(QRect(900, 0, 61, 61))
        self.btnPen2.setAutoFillBackground(False)
        self.btnPen2.setStyleSheet(u"#btnPen2 {\n"
"	border: 0px;\n"
"	border-left:0.5px solid #636363;\n"
"}\n"
"\n"
"#btnPen2:hover {\n"
"	\n"
"	background-color: rgb(39, 39, 39);\n"
"}\\")
        icon11 = QIcon()
        icon11.addFile(u"icon/pen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPen2.setIcon(icon11)
        self.btnPen2.setIconSize(QSize(35, 35))
        self.btnPen3 = QPushButton(self.headerFrame_2)
        self.btnPen3.setObjectName(u"btnPen3")
        self.btnPen3.setGeometry(QRect(960, 0, 61, 61))
        self.btnPen3.setAutoFillBackground(False)
        self.btnPen3.setStyleSheet(u"#btnPen3 {\n"
"	border:0px;\n"
"	border-left:0.5px solid #636363;\n"
"}\n"
"\n"
"#btnPen3:hover {\n"
"	\n"
"	background-color: rgb(39, 39, 39);\n"
"}\\")
        icon12 = QIcon()
        icon12.addFile(u"icon/pen2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPen3.setIcon(icon12)
        self.btnPen3.setIconSize(QSize(35, 35))
        self.btnErase = QPushButton(self.headerFrame_2)
        self.btnErase.setObjectName(u"btnErase")
        self.btnErase.setGeometry(QRect(1020, 0, 100, 61))
        self.btnErase.setAutoFillBackground(False)
        self.btnErase.setStyleSheet(u"#btnErase {\n"
"border: 0px;\n"
"	border-left:2px solid white;\n"
"\n"
"}\n"
"\n"
"#btnErase:hover {\n"
"	\n"
"	background-color: rgb(39, 39, 39);\n"
"}\\")
        icon13 = QIcon()
        icon13.addFile(u"icon/erase.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnErase.setIcon(icon13)
        self.btnErase.setIconSize(QSize(35, 35))
        self.btnColor = QPushButton(self.headerFrame_2)
        self.btnColor.setObjectName(u"btnColor")
        self.btnColor.setGeometry(QRect(460, 2, 55, 55))
        self.btnColor.setAutoFillBackground(False)
        self.btnColor.setStyleSheet(u"#btnColor {\n"
"	border-radius: 27px;\n"
"	border : 2px solid #636363;\n"
"}\n"
"\n"
"")
        self.btnColor.setIconSize(QSize(35, 35))
        self.stackedWidget.addWidget(self.paintPage)
        self.btnDrawTag = QPushButton(self.mainwidget)
        self.btnDrawTag.setObjectName(u"btnDrawTag")
        self.btnDrawTag.setGeometry(QRect(148, 14, 69, 41))
        self.btnDrawTag.setFont(font2)
        self.btnDrawTag.setStyleSheet(u"#btnDrawTag {\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border-left: 2px solid white;\n"
"	background-color: rgb(80, 80, 80);\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"#btnDrawTag:hover {\n"
"	\n"
"	background-color: rgb(39, 39, 39);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"icon/drawfr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDrawTag.setIcon(icon14)
        self.btnDrawTag.setIconSize(QSize(25, 25))
        self.btnImgTag = QPushButton(self.mainwidget)
        self.btnImgTag.setObjectName(u"btnImgTag")
        self.btnImgTag.setGeometry(QRect(11, 14, 69, 41))
        self.btnImgTag.setFont(font2)
        self.btnImgTag.setStyleSheet(u"#btnImgTag {\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	border-right: 2px solid white;\n"
"	background-color: rgb(80, 80, 80);\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"#btnImgTag:hover {\n"
"	\n"
"	background-color: rgb(39, 39, 39);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"icon/addPic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnImgTag.setIcon(icon15)
        self.btnImgTag.setIconSize(QSize(25, 25))
        self.btnVideoTag = QPushButton(self.mainwidget)
        self.btnVideoTag.setObjectName(u"btnVideoTag")
        self.btnVideoTag.setGeometry(QRect(80, 15, 69, 41))
        self.btnVideoTag.setFont(font2)
        self.btnVideoTag.setStyleSheet(u"\n"
"#btnVideoTag {\n"
"	background-color: rgb(80, 80, 80);\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"#btnVideoTag:hover {\n"
"	\n"
"	background-color: rgb(39, 39, 39);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"icon/videofr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnVideoTag.setIcon(icon16)
        self.btnVideoTag.setIconSize(QSize(25, 25))
        MainWindow.setCentralWidget(self.mainwidget)

        self.retranslateUi(MainWindow)
        self.btnBasic.toggled.connect(self.basicWid2.setVisible)
        self.btnFilter.toggled.connect(self.FilterWid2.setVisible)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OptiPics", None))
#if QT_CONFIG(tooltip)
        self.btnAdd.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p style=\"color: #FFFFFF;\">Add Picture</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnAdd.setText("")
        self.btnReset.setText("")
        self.btnDone.setText("")
        self.btnIconName.setText("")
        self.lblImgName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnDownload.setText("")
        self.lblTool.setText(QCoreApplication.translate("MainWindow", u"TOOLS", None))
        self.lblRotate.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.btnLeft.setText("")
        self.btnRight.setText("")
        self.btnFit.setText(QCoreApplication.translate("MainWindow", u"Fit", None))
        self.btnWrite.setText(QCoreApplication.translate("MainWindow", u"Text on IMG", None))
        self.btnResize.setText(QCoreApplication.translate("MainWindow", u"Resize", None))
        self.btnCrop.setText(QCoreApplication.translate("MainWindow", u"Crop", None))
        self.btnRemoveBg.setText(QCoreApplication.translate("MainWindow", u"Remove Background", None))
        self.btnColorization_2.setText(QCoreApplication.translate("MainWindow", u"  Colorization and Balance", None))
        self.btnGray.setText(QCoreApplication.translate("MainWindow", u"Gray", None))
        self.btnGray2.setText(QCoreApplication.translate("MainWindow", u"Gray +", None))
        self.btnHDR.setText(QCoreApplication.translate("MainWindow", u"HDR", None))
        self.btnSepia.setText(QCoreApplication.translate("MainWindow", u"Sepia", None))
        self.btnInvert.setText(QCoreApplication.translate("MainWindow", u"Invert", None))
        self.btnGrayPencil.setText(QCoreApplication.translate("MainWindow", u"Gray Pencil", None))
        self.btnColorPencil.setText(QCoreApplication.translate("MainWindow", u"Color Pencil", None))
        self.btnCartoon.setText(QCoreApplication.translate("MainWindow", u"Cartoon", None))
        self.btnWaterCartoon.setText(QCoreApplication.translate("MainWindow", u"Water cartoon", None))
        self.btnShaperning.setText(QCoreApplication.translate("MainWindow", u"Shaperning", None))
        self.btnFilter.setText(QCoreApplication.translate("MainWindow", u"  Filter", None))
        self.btnBasic.setText(QCoreApplication.translate("MainWindow", u"  Basic", None))
        self.btnColorization.setText(QCoreApplication.translate("MainWindow", u"  Colorization", None))
        self.lblOriginImg.setText("")
#if QT_CONFIG(whatsthis)
        self.txtWeight.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lblWeight.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.lblHeight.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.btnResizeDone.setText(QCoreApplication.translate("MainWindow", u"Resize", None))
        self.lblBrightNum.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lblBrightness.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.lblThreshNum.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lblTV60.setText(QCoreApplication.translate("MainWindow", u"TV 60s", None))
        self.lblValueNum.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btnTV60.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.lblImg.setText("")
#if QT_CONFIG(tooltip)
        self.btnAddVideo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p style=\"color: #FFFFFF;\">Add Picture</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnAddVideo.setText("")
        self.btnVidtoCar.setText(QCoreApplication.translate("MainWindow", u"Convert to Cartoon", None))
        self.btnplay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btnEnd.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.lblStatus.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.lblRotateVideo.setText(QCoreApplication.translate("MainWindow", u"Degree of rotation (clockwise)", None))
        self.btnSubclipVid.setText(QCoreApplication.translate("MainWindow", u"Subclip (Video)", None))
        self.btnSubclipAu.setText(QCoreApplication.translate("MainWindow", u"Subclip (Audio)", None))
        self.lblPaper.setText("")
        self.btnResetPaint.setText("")
        self.btnSavePaint.setText("")
        self.btnPen1.setText("")
        self.btnPen2.setText("")
        self.btnPen3.setText("")
        self.btnErase.setText("")
        self.btnColor.setText("")
        self.btnDrawTag.setText("")
        self.btnImgTag.setText("")
        self.btnVideoTag.setText("")
    # retranslateUi

