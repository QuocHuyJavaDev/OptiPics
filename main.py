import os

import numpy as np
from PyQt5.QtWidgets import QColorDialog, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import QSize, Qt, QUrl
from PySide2.QtCore import QUrl
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QFileDialog, QShortcut
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtMultimediaWidgets import QVideoWidget


from ImgEditor import *
from main_ui import *
from VideoEditor import *
from show_dialog import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        layout = QVBoxLayout()
        self.ui.frameFilterImg.setLayout(layout)
        layout.addWidget((self.ui.lblImg))
        layout.setAlignment(self.ui.lblImg, Qt.AlignCenter)

        ### PAGE NAVIGATION
        # Img Editor Page
        self.ui.btnImgTag.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.imgPage))
        # Video Page
        self.ui.btnVideoTag.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.videoPage))
        # Painting Page
        self.ui.btnDrawTag.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.paintPage))

        #### EVENT HANDLE
        ### Image Editor
        ## Navbar
        # Upload Img
        self.ui.btnAdd.clicked.connect(lambda: ImgLS.LSFunc.UploadImg(self))
        #self.lblOriginImg.setAlignment(Qt.AlignCenter)
        # Reset
        self.ui.btnReset.clicked.connect(lambda: NavFunc.NavbarFunc.ResetFunc(self))
        #Save
        self.ui.btnDone.clicked.connect(lambda: NavFunc.NavbarFunc.DoneFunc(self))
        # Download
        self.ui.btnDownload.clicked.connect(lambda: NavFunc.NavbarFunc.SaveFunc(self))
        ## Basic
        # Rotate
        self.ui.btnLeft.clicked.connect(lambda: BasicEditor.BasicFunc.LeftRotate(self))
        self.ui.btnRight.clicked.connect(lambda: BasicEditor.BasicFunc.RightRotate(self))
        # Fit
        self.ui.btnFit.clicked.connect(lambda: BasicEditor.BasicFunc.FitImg(self))
        # Resize
        self.ui.btnResize.clicked.connect(lambda: BasicEditor.BasicFunc.ResizeImg(self))
        self.ui.btnResizeDone.clicked.connect(lambda: BasicEditor.BasicFunc.ResizeDone(self))
        # Remove background
        self.ui.btnRemoveBg.clicked.connect(lambda: BasicEditor.BasicFunc.removeBackground(self))
        # Write
        self.pos_x, self.pos_y = None, None
        #self.ui.btnWrite.clicked.connect(lambda: BasicEditor.BasicFunc.writeOnImage(self))
        self.ui.btnWrite.clicked.connect(self.startWrite)
        # Crop
        self.start_x, self.start_y = None, None
        self.end_x, self.end_y = None, None
        self.is_cropping = False

        self.ui.btnCrop.clicked.connect(self.startCrop)

        ## Filter
        # Gray
        self.ui.btnGray.clicked.connect(lambda: ColorFilter.ColorFunc.GrayFilter(self))
        # Gray + (Invert)
        self.ui.btnGray2.clicked.connect(lambda: ColorFilter.ColorFunc.GrayPlusFilter(self))
        # HDR
        self.ui.btnHDR.clicked.connect(lambda: ColorFilter.ColorFunc.HDRFilter(self))
        # Sepia
        self.ui.btnSepia.clicked.connect(lambda: ColorFilter.ColorFunc.SepiaFilter(self))
        # Invert Color
        self.ui.btnInvert.clicked.connect(lambda: ColorFilter.ColorFunc.InvertColor(self))
        #Gray pencil
        self.ui.btnGrayPencil.clicked.connect(lambda: ColorFilter.ColorFunc.GrayPencilSketch(self))
        # Color pencil
        self.ui.btnColorPencil.clicked.connect(lambda: ColorFilter.ColorFunc.ColorPencilSketch(self))
        # Cartoon
        self.ui.btnCartoon.clicked.connect(lambda: ColorFilter.ColorFunc.CartoonImg(self))
        # Water Cartoon
        self.ui.btnWaterCartoon.clicked.connect(lambda: ColorFilter.ColorFunc.WaterCartoonImg(self))
        # Sharpening
        self.ui.btnShaperning.clicked.connect(lambda: ColorFilter.ColorFunc.SharpeningFilter(self))

        ## Colorization
        self.ui.btnColorization.clicked.connect(lambda: ImgColorization.ColorizationClass.mauhoa_anh1(self))
        ## Colorization & Balance
        self.ui.btnColorization_2.clicked.connect(lambda: ImgColorization.ColorizationClass.mauhoa_anh2(self))

        ### FOOTER
        self.ui.txtWeight.setEnabled(False)
        #self.ui.txtHeight.setEnabled(False)
        self.ui.btnResizeDone.setEnabled(False)
        #Brightness
        self.ui.slideBrightness.setMinimum(0)
        self.ui.slideBrightness.setMaximum(150)
        self.ui.slideBrightness.setValue(100)
        self.ui.slideBrightness.valueChanged.connect(lambda: BasicFunc.Brightness(self))
        #TV60s
        self.ui.slideTV60Val.setMinimum(0)
        self.ui.slideTV60Val.setMaximum(255)
        self.ui.slideTV60Val.setValue(0)

        self.ui.slideTV60Thresh.setMinimum(0)
        self.ui.slideTV60Thresh.setMaximum(100)
        self.ui.slideTV60Thresh.setValue(0)

        self.ui.slideTV60Val.valueChanged.connect(lambda: BasicFunc.SlideTV60s(self))
        self.ui.slideTV60Thresh.valueChanged.connect(lambda: BasicFunc.SlideTV60s(self))
        self.ui.btnTV60.clicked.connect(lambda: BasicFunc.Tv60Func(self))


        ##################### PAINTING ###########################
        self.previousPoint = None


        self.canvas = QPixmap(QSize(self.ui.lblPaper.width(), self.ui.lblPaper.height()))
        self.canvas.fill(QColor("white"))

        self.pen = QPen()
        self.pen.setWidth(2)
        #Nét bút
        self.pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        self.colorPen = None
        self.erase = None

        self.ui.lblPaper.setPixmap(self.canvas)
        self.ui.lblPaper.mouseMoveEvent = self.label_mouseMoveEvent
        self.ui.lblPaper.mouseReleaseEvent = self.label_mouseReleaseEvent

        self.ui.btnErase.clicked.connect(self.EraseFunc)
        self.ui.btnColor.clicked.connect(self.changeColor)
        self.ui.btnSavePaint.clicked.connect(self.savePaint)
        self.ui.btnPen1.clicked.connect(self.pen1)
        self.ui.btnPen2.clicked.connect(self.pen2)
        self.ui.btnPen3.clicked.connect(self.pen3)
        self.ui.btnResetPaint.clicked.connect(self.resetPaint)

        ################ VIDEO ####################3
        self.ui.combobox_degree.addItem('0')
        self.ui.combobox_degree.addItem('90')
        self.ui.combobox_degree.addItem('180')
        self.ui.combobox_degree.addItem('270')

        self.is_finished = True
        self.thread = None
        self.record_start_time = None
        self.record_end_time = None
        self.video_name = ""

        # Create a QVideoWidget object
        self.widget_video = QVideoWidget()

        self.ui.horizontalSlider.setRange(0, 0)
        self.ui.horizontalSlider.sliderMoved.connect(self.set_position)
        self.video_duration = 0

        # Set the QVideoWidget as the video output of the QMediaPlayer
        self.video_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.video_player.setVideoOutput(self.widget_video)
        self.video_player.positionChanged.connect(self.position_changed)
        self.video_player.durationChanged.connect(self.duration_changed)
        self.video_player.error.connect(self.error_control)

        layout = QVBoxLayout()
        layout.addWidget(self.widget_video)
        self.ui.videoWid.setLayout(layout)

        self.ui.btnAddVideo.clicked.connect(self.openFile)
        self.ui.btnplay.clicked.connect(self.play_video)
        self.ui.btnStart.clicked.connect(self.record_start)
        self.ui.btnEnd.clicked.connect(self.record_end)
        self.ui.btnClear.clicked.connect(self.record_clear)
        self.ui.btnSubclipVid.clicked.connect(self.record_subclip_video)
        self.ui.btnSubclipAu.clicked.connect(self.record_subclip_audio)

        QShortcut(QKeySequence(Qt.Key_Up), self, self.arrow_up)
        QShortcut(QKeySequence(Qt.Key_Down), self, self.arrow_down)
        QShortcut(QKeySequence(Qt.Key_Left), self, self.arrow_left_event)
        QShortcut(QKeySequence(Qt.Key_Right), self, self.arrow_right_event)
        QShortcut(QKeySequence(Qt.Key_Space), self, self.play_video)

        # Convert video to cartoon
        self.ui.btnVidtoCar.clicked.connect(lambda: CartoonEffect.CartoonVideoFunc.convertVidtoCartoon(self))

        ############## HIDE MENU WIDGET WHEN START #####################
        self.ui.basicWid2.hide()
        self.ui.FilterWid2.hide()

        ### SHOW ==> MAIN WINDOW
        self.show()


    ### Write
    def startWrite(self):
        self.ui.lblImg.mouseDoubleClickEvent = self.mouse_click_event


    def mouse_click_event(self, event):
        self.pos_x, self.pos_y = event.x(), event.y()
        self.image = self.tmp
        dialog = MultiInputDialog(self.image, self.pos_x, self.pos_y)
        dialog.exec_()
        ImgLS.LSFunc.displayImg(self)

    #### Crop
    def startCrop(self):
        self.ui.lblImg.mousePressEvent = self.mouse_press_event
        self.ui.lblImg.mouseMoveEvent = self.mouse_move_event
        self.ui.lblImg.mouseReleaseEvent = self.mouse_release_event
        
    def mouse_press_event(self, event):
        self.start_x, self.start_y = event.x(), event.y()
        self.end_x, self.end_y = None, None
        self.is_cropping = True
        self.update()

    def mouse_move_event(self, event):
        if self.is_cropping:
            self.end_x, self.end_y = event.x(), event.y()

    def mouse_release_event(self, event):
        self.is_cropping = False
        self.crop_image()
        self.update()

    def crop_image(self):
        if self.start_x is not None and self.end_x is not None:
            x = min(self.start_x, self.end_x)
            y = min(self.start_y, self.end_y)
            width = abs(self.start_x - self.end_x)
            height = abs(self.start_y - self.end_y)
            print(x)
            print(y)
            print(width)
            print(height)
            self.image = self.image[y:y + height, x:x + width]
            self.image = np.ascontiguousarray(self.image)
            self.tmp = self.image
            qformat = QImage.Format_Indexed8
            if len(self.image.shape) == 3:
                if (self.image.shape[2]) == 4:
                    qformat = QImage.Format_RGBA8888
                else:
                    qformat = QImage.Format_RGB888
            img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
            img = img.rgbSwapped()
            self.ui.lblImg.setPixmap(QPixmap.fromImage(img))
            print("Image cropped and saved as cropped_image.png")

    ############################# VIDEO ###############################
    # up volume
    def arrow_up(self):
        # if video not stop
        if self.video_player.state() != QMediaPlayer.StoppedState:
            self.video_player.setVolume(min(self.video_player.volume() + 10, 100))

    # up volume
    def arrow_down(self):
        if self.video_player.state() != QMediaPlayer.StoppedState:
            self.video_player.setVolume(max(self.video_player.volume() - 10, 0))

    # Fast-forward to 10 seconds later.
    def arrow_left_event(self):
        self.set_position(self.ui.horizontalSlider.value() - 10 * 1000)

    #  Go back to 10 seconds ago.
    def arrow_right_event(self):
        self.set_position(self.ui.horizontalSlider.value() + 10 * 1000)

    # video_player function
    # Change the position of the slider when video play.
    def position_changed(self, position):
        self.ui.horizontalSlider.setValue(position)

    #Set range slider
    def duration_changed(self, duration):
        self.ui.horizontalSlider.setRange(0, duration)
        self.video_duration = duration
        self.record_start_time = 0
        self.record_end_time = 0

    # Change video pos when slider changer
    def set_position(self, position):
        self.video_player.setPosition(position)


    def error_control(self):
        self.button_play.setEnabled(False)
        self.ui.lblStatus.setText(
            "Error: An error occurs while opening the video.")

    def openFile(self):
        #set WMF ưu tiên phát video
        os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
        video_name, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                    QDir.homePath())
        self.video_name = video_name

        if self.video_name != '':
            if self.video_name[-4:] == '.flv':
                self.ui.lblStatus.setText(self.video_name[-4:])
                self.video_name = self.flv2mp4(self.video_name, self.video_name[: -4] + '.mp4')

            self.video_player.setMedia(
                QMediaContent(QUrl.fromLocalFile(self.video_name)))

            self.ui.btnplay.setEnabled(True)
            self.video_player.play()
            #  tìm vị trí cuối cùng của ký tự /
            index = self.video_name.rfind('/')
            self.ui.lblStatus.setText(
                # bỏ qua ký tự / và lấy phần tên tệp video sau dấu /
                "Info: Playing the video '" + self.video_name[(index + 1):]
                + "' ...")

    def flv2mp4(self, video_name, output_name='tmp.mp4'):
        import subprocess
        # Lệnh CHuyen đổi định dạng video từ video name sang ouput name
        command = [
            'ffmpeg', '-y', '-i', video_name, '-c', 'copy', '-copyts', output_name
        ]
        # Chạy lệnh
        ffmpeg = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        ffmpeg.communicate()

        return output_name

    # Sự kiện nút play
    def play_video(self):
        if self.video_player.state() == QMediaPlayer.PlayingState:
            self.video_player.pause()
        else:
            self.video_player.play()

    def record_start(self):
        self.record_start_time = self.ui.horizontalSlider.sliderPosition()
        if self.record_end_time is not None and self.record_end_time != 0 and self.record_start_time > self.record_end_time:
            self.record_start_time, self.record_end_time = self.record_end_time, self.record_start_time

        self._show_record_time()

    def record_end(self):
        self.record_end_time = self.ui.horizontalSlider.sliderPosition()
        if self.record_start_time is not None and self.record_start_time > self.record_end_time:
            self.record_start_time, self.record_end_time = self.record_end_time, self.record_start_time

        self._show_record_time()

    def _show_record_time(self):
        if self.record_start_time is not None and self.record_end_time is not None:
            self.ui.lblStatus.setText(
                "Info: Starting time: ({}), and Ending time: ({}) (Duration: {}).".format(
                self.record_start_time / 1000, self.record_end_time / 1000, self.video_duration / 1000))

    def record_clear(self):
        self.record_start_time = 0
        self.record_end_time = 0

        self.ui.lblStatus.setText(
                "Info: Starting time: ({}), and Ending time: ({}).".format(self.record_start_time, self.record_end_time))

    def _check_duration(self):
        if self.video_name == "":
            self.ui.lblStatus.setText(
                "Error: Please open a video first.")
        elif self.record_start_time == self.record_end_time:
            self.ui.lblStatus.setText(
                "Error: Duration can NOT be 0.")
        elif self.record_start_time > self.record_end_time:
            self.ui.lblStatus.setText(
                "Error: The start time should be earlier than the end time.")
        else:
            return True

        return False

    def record_subclip_video(self):
        if self._check_duration():
            self.ui.lblStatus.setText(
                "Info: Please wait until the process ends.")
            self.thread = Thread()
            self.is_finished = False
            self.thread.set_params(Thread.MSG_CUT_VIDEO, self.video_name,
                                   self.record_start_time / 1000, self.record_end_time / 1000,
                                   self.ui.combobox_degree.currentText())
            self.thread.signal_return_value.connect(self.thread_done)
            self.thread.start()

    def record_subclip_audio(self):
        if self._check_duration():
            self.ui.lblStatus.setText(
                "Info: Please wait until the process ends.")
            self.thread = Thread()
            self.is_finished = False
            self.thread.set_params(Thread.MSG_EXTRACT_AUDIO, self.video_name,
                                   self.record_start_time / 1000, self.record_end_time / 1000)
            self.thread.signal_return_value.connect(self.thread_done)
            self.thread.start()

    def thread_done(self, return_value, video_name):
        if return_value:
            self.is_finished = True
            self.ui.lblStatus.setText(
                "Info: The process has done and saved as {}.".format(video_name))

    def closeEvent(self, event):
        if not self.is_finished:
            self.thread.stop()
        event.accept()

    ############################## PEN ################################3
    def pen1(self):
        self.pen.setColor(self.colorPen)
        self.pen.setWidth(2)

    def pen2(self):
        self.pen.setColor(self.colorPen)
        self.pen.setWidth(5)

    def pen3(self):
        self.pen.setColor(self.colorPen)
        self.pen.setWidth(10)

    def resetPaint(self):
        self.canvas.fill(QColor("white"))
        self.ui.lblPaper.setPixmap(self.canvas)

    def savePaint(self):
        dialog = QFileDialog()
        dialog.setNameFilter("*.jpg")
        dialog.setDefaultSuffix(".jpg")
        clickedOk = dialog.exec()
        print(dialog.selectedFiles())
        if clickedOk:
            self.canvas.save(dialog.selectedFiles()[0])


    def changeColor(self):
        self.dialog = QColorDialog()
        clickedOk =  self.dialog.exec()
        if clickedOk:
            self.pen.setColor(self.dialog.currentColor())
            self.colorPen = self.dialog.currentColor()
            self.ui.btnColor.setStyleSheet(u"#btnColor {\n"
                                        "	border-radius: 27px;\n"
                                        "	border : 2px solid #636363;\n"
                                        "	background-color: %s;\n"
                                        "}\n"
                                        "\n"
                                        "" %  self.dialog.currentColor().name())


    def label_mouseMoveEvent(self, event):
        position = event.pos()
        painter = QPainter(self.canvas)
        painter.setPen(self.pen)
        if self.previousPoint:
            painter.drawLine(self.previousPoint.x(), self.previousPoint.y(),
                             position.x(), position.y())
        else:
            painter.drawPoint(position.x(), position.y())
        painter.end()
        self.ui.lblPaper.setPixmap(self.canvas)
        self.previousPoint = position

    def label_mouseReleaseEvent(self, event):
        self.previousPoint = None
        self.erase = None

    def EraseFunc(self):
        self.erase = True
        self.pen.setWidth(20)
        self.pen.setColor("#FFFFFF")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
