import cv2
from PySide2.QtWidgets import QFileDialog

from main import MainWindow


class CartoonVideoFunc(MainWindow):

    def convertVidtoCartoon(self):
        print(self.video_name)
        video_capture  = cv2.VideoCapture(self.video_name)
        width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video_capture.get(cv2.CAP_PROP_FPS)
        video_writer = CartoonVideoFunc.saveVideo(self, fps, width, height)

        while video_capture.isOpened():
            ret, frame = video_capture.read()
            if ret:
                frame = CartoonVideoFunc.cartoonize(frame)
                video_writer.write(frame)
                #cv2.imshow('Video', frame)
            else:
                break

        # Release the video capture and writer, and close the OpenCV window
        video_capture.release()
        video_writer.release()



    def cartoonize(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)  # applying median blur with kernel size of 5
        edges2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)
        dst = cv2.edgePreservingFilter(img, flags=2, sigma_s=64,
                                       sigma_r=0.25)
        cartoon = cv2.bitwise_and(dst, dst, mask=edges2)

        return cartoon

    def saveVideo(self, fps, width, height):
        dialog = QFileDialog()
        dialog.setNameFilter("*.mp4")
        dialog.setDefaultSuffix(".mp4")
        clickedOk = dialog.exec()
        if clickedOk:
            output_file = str(dialog.selectedFiles()[0]) # Specify the output file name and format
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the desired codec (e.g., 'XVID', 'MJPG', 'mp4v', etc.)
            video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
        return video_writer
