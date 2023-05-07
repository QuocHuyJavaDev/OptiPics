import os
import sys

from PyQt5.QtWidgets import QColorDialog, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import QSize, Qt, QUrl
from PySide2.QtCore import QUrl
from PySide2.QtGui import QPalette, QColor
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFileDialog, QPushButton,QShortcut
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtMultimediaWidgets import QVideoWidget

from ImgEditor import *
from main_ui import *
from VideoEditor import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        # Reset
        self.ui.btnReset.clicked.connect(lambda: NavFunc.NavbarFunc.ResetFunc(self))
        # Download
        self.ui.btnDownload.clicked.connect(lambda: NavFunc.NavbarFunc.SaveFunc(self))
        ## Basic
        # Rotate
        self.ui.btnLeft.clicked.connect(lambda: BasicEditor.BasicFunc.LeftRotate(self))
        self.ui.btnRight.clicked.connect(lambda: BasicEditor.BasicFunc.RightRotate(self))
        # Fit
        self.ui.btnFit.clicked.connect(lambda: BasicEditor.BasicFunc.FitImg(self))
        ## Filter
        # Gray
        self.ui.btnGray.clicked.connect(lambda: ColorFilter.ColorFunc.GrayFilter(self))
        # Gray + (Invert)
        self.ui.btnGray2.clicked.connect(lambda: ColorFilter.ColorFunc.GrayPlusFilter(self))
        # Sepia
        self.ui.btnSepia.clicked.connect(lambda: ColorFilter.ColorFunc.SepiaFilter(self))
        # Invert Color
        self.ui.btnInvert.clicked.connect(lambda: ColorFilter.ColorFunc.InvertColor(self))
        # Sharpening
        self.ui.btnShaperning.clicked.connect(lambda: ColorFilter.ColorFunc.SharpeningFilter(self))

        ### PAINTING
        self.previousPoint = None

        self.canvas = QPixmap(QSize(self.ui.lblPaper.width(), self.ui.lblPaper.height()))
        self.canvas.fill(QColor("white"))

        self.pen = QPen()
        self.pen.setWidth(2)
        self.pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        self.ui.lblPaper.setPixmap(self.canvas)
        self.ui.lblPaper.mouseMoveEvent = self.label_mouseMoveEvent
        self.ui.lblPaper.mouseReleaseEvent = self.label_mouseReleaseEvent
        self.ui.btnColor.clicked.connect(self.changeColor)
        self.ui.btnSavePaint.clicked.connect(self.savePaint)
        self.ui.btnPen1.clicked.connect(self.pen1)
        self.ui.btnPen2.clicked.connect(self.pen2)
        self.ui.btnPen3.clicked.connect(self.pen3)
        self.ui.btnResetPaint.clicked.connect(self.resetPaint)

        ### VIDEO
        self.video_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.is_finished = True
        self.thread = None

        self.record_start_time = None
        self.record_end_time = None
        self.video_name = ""

        # Create a QVideoWidget object
        self.widget_video = QVideoWidget()

        self.ui.btnAddVideo.clicked.connect(self.openFile)
        self.ui.btnplay.clicked.connect(self.play_video)

        self.ui.horizontalSlider.setRange(0, 0)
        self.ui.horizontalSlider.sliderMoved.connect(self.set_position)
        self.video_duration = 0

        # Set the QVideoWidget as the video output of the QMediaPlayer
        self.video_player.setVideoOutput(self.widget_video)
        self.video_player.positionChanged.connect(self.position_changed)
        self.video_player.durationChanged.connect(self.duration_changed)
        self.video_player.error.connect(self.error_control)

        layout = QVBoxLayout()
        layout.addWidget(self.widget_video)
        self.ui.videoWid.setLayout(layout)

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

        ### HIDE MENU WIDGET WHEN START
        self.ui.basicWid2.hide()
        self.ui.FilterWid2.hide()

        ### SHOW ==> MAIN WINDOW
        self.show()

    #### Painting Event
    def arrow_up(self):
        if self.video_player.state() != QMediaPlayer.StoppedState:
            self.video_player.setVolume(min(self.video_player.volume() + 10, 100))

    def arrow_down(self):
        if self.video_player.state() != QMediaPlayer.StoppedState:
            self.video_player.setVolume(max(self.video_player.volume() - 10, 0))

    def arrow_left_event(self):
        """ Slot function:
        Action after the key 'arrow left' is pressed.
        Fast-forward to 10 seconds later.
        """

        self.set_position(self.video_slider.value() - 10 * 1000)

    def arrow_right_event(self):
        """ Slot function:
        Action after the key 'arrow right' is pressed.
        Go back to 10 seconds ago.
        """

        self.set_position(self.video_slider.value() + 10 * 1000)
    def mousePressEvent(self, event):
        """ Slot function:
        The starting position of the slider is 50.
        Note: This function still can't not accurately move the slider to the
        clicked position.
        """

        slider_start_pos = self.ui.horizontalSlider.geometry().topLeft().x()
        if 42 <= self.height() - event.pos().y() <= 62:
            position = self.ui.horizontalSlider.minimum() + (
                        event.pos().x() - slider_start_pos) / self.video_slider.width() * self.video_duration
            if position != self.ui.horizontalSlider.sliderPosition():
                self.set_position(position)


    def position_changed(self, position):
        """ Slot function:
        Change the position of the slider.
        """

        self.ui.horizontalSlider.setValue(position)

    def duration_changed(self, duration):
        """ Slot function:
        If the duration of the video changed, change the range of the slider.
        This slot function is called after opening a video.
        """

        self.ui.horizontalSlider.setRange(0, duration)
        self.video_duration = duration
        self.record_start_time = 0
        self.record_end_time = 0

    def set_position(self, position):
        """ Slot function:
        Change the progress of the video.
        """

        self.video_player.setPosition(position)

    def error_control(self):
        """ Slot function:
        If an error occurs while opening the video, this slot function is
        called.
        """

        self.button_play.setEnabled(False)
        self.statusbar.showMessage(
            "Error: An error occurs while opening the video.")

    def openFile(self):
        """ Slot function:
                Open a video from the file system.
                """
        os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
        video_name, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                    QDir.homePath())
        self.video_name = video_name

        if self.video_name != '':
            if self.video_name[-4:] == '.flv':
                self.statusbar.showMessage(self.video_name[-4:])
                self.video_name = self.flv2mp4(self.video_name, self.video_name[: -4] + '.mp4')

            self.video_player.setMedia(
                QMediaContent(QUrl.fromLocalFile(self.video_name)))
            self.ui.btnplay.setEnabled(True)
            self.video_player.play()

            index = self.video_name.rfind('/')
            self.ui.lblStatus.setText(
                "Info: Playing the video '" + self.video_name[(index + 1):]
                + "' ...")

    def flv2mp4(self, video_name, output_name='tmp.mp4'):
        import subprocess
        command = [
            'ffmpeg', '-y', '-i', video_name, '-c', 'copy', '-copyts', output_name
        ]
        ffmpeg = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        ffmpeg.communicate()

        return output_name

    def play_video(self):
        """ Slot function:
        The slot function for the 'play' button.
        If the video player is currently paused, then play the video;
        otherwise, pause the video.
        """

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

    def pen1(self):
        self.pen.setWidth(2)

    def pen2(self):
        self.pen.setWidth(5)

    def pen3(self):
        self.pen.setWidth(10)

    def resetPaint(self):
        self.canvas.fill(QColor("white"))
        self.ui.lblPaper.setPixmap(self.canvas)

    def savePaint(self):
        dialog = QFileDialog()
        dialog.setNameFilter("*.jpg")
        dialog.setDefaultSuffix(".jpg")
        clickedOk = dialog.exec()
        if clickedOk:
            self.canvas.save(dialog.selectedFiles()[0])

    def changeColor(self):
        dialog = QColorDialog()
        clickedOk = dialog.exec()
        if clickedOk:
            self.pen.setColor(dialog.currentColor())
            self.ui.btnColor.setStyleSheet(u"#btnColor {\n"
                                        "	border-radius: 27px;\n"
                                        "	border : 2px solid #636363;\n"
                                        "	background-color: %s;\n"
                                        "}\n"
                                        "\n"
                                        "" % dialog.currentColor().name())


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
