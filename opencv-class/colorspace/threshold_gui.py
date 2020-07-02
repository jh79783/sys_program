import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5 import uic
# import matplotlib.pylab as plt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("thresholding.ui", self)
        self.src_img = None             # 원본 영상
        self.res_img = None             # threshold 결과 영상
        self.rb_dict = {self.radioButton_binary: cv2.THRESH_BINARY,
                        self.radioButton_binary_inv: cv2.THRESH_BINARY_INV,
                        self.radioButton_trunc: cv2.THRESH_TRUNC,
                        self.radioButton_tozero: cv2.THRESH_TOZERO,
                        self.radioButton_tozero_inv: cv2.THRESH_TOZERO_INV,
                        }
        self.rb_adap_list = [self.radioButton_none, self.radioButton_otsu,
                             self.radioButton_adap_mean, self.radioButton_adap_gauss]
        self.setup_ui()

    def setup_ui(self):
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.radioButton_binary.setChecked(True)
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setValue(100)
        for rbutton in self.rb_dict.keys():
            rbutton.clicked.connect(self.threshold_image)
        self.verticalSlider.valueChanged.connect(self.threshold_image)
        for rbutton in self.rb_adap_list:
            rbutton.clicked.connect(self.threshold_image)

    def threshold_image(self):
        if self.src_img is None:
            return
        thr_type, threshold, adaptive = self.get_params()
        if adaptive is None:
            ret, self.res_img = cv2.threshold(self.src_img, threshold, 255, thr_type)
            print("threshold", ret)
        else:
            self.res_img = cv2.adaptiveThreshold(self.src_img, 255, adaptive, thr_type, 9, 5)
        cv2.imshow("result image", self.res_img)
        cv2.waitKey(1)

    def get_params(self):
        thr_type = cv2.THRESH_BINARY
        for rbutton, button_type in self.rb_dict.items():
            if rbutton.isChecked():
                thr_type = button_type

        if self.radioButton_otsu.isChecked():
            thr_type |= cv2.THRESH_OTSU

        adaptive = None
        if self.radioButton_adap_mean.isChecked():
            adaptive = cv2.ADAPTIVE_THRESH_MEAN_C
        elif self.radioButton_adap_gauss.isChecked():
            adaptive = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
        threshold = self.verticalSlider.value()
        self.label_threshold.setText(f"Threshold: {threshold}")
        return thr_type, threshold, adaptive

    def open_file(self):
        filename = QFileDialog.getOpenFileName(filter="JPG files (*.jpg)")
        filename = filename[0]
        print("open file:", filename)
        if not filename:
            return
        self.src_img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        cv2.imshow("original", self.src_img)
        cv2.waitKey(1)

    def save_file(self):
        filename = QFileDialog.getOpenFileName(filter="JPG files (*.jpg)", directory="../sample_imgs")
        filename = filename[0]
        print("save file:", filename)
        if not filename or self.res_img is None:
            return
        cv2.imwrite(filename, self.res_img)


def main():
    app = QApplication(sys.argv)
    editor = MyWindow()
    editor.show()
    app.exec_()


if __name__ == "__main__":
    main()

