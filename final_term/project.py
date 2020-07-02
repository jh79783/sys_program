import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import cv2
import numpy as np
import os


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("project.ui", self)
        self.rb_dict = {self.radioButton_hsv: cv2.COLOR_BGR2HSV,
                        self.radioButton_bgr: "bgr"}
        self.setup_ui()
        self.frame = None
        self.bgr_param = None
        self.hsv_param = None
        self.cam = None
        self.end = True

    def setup_ui(self):
        self.verticalSlider_lower_BH.setRange(0, 255)
        self.verticalSlider_lower_BH.setValue(100)
        self.verticalSlider_lower_GS.setRange(0, 255)
        self.verticalSlider_lower_GS.setValue(100)
        self.verticalSlider_lower_RV.setRange(0, 255)
        self.verticalSlider_lower_RV.setValue(100)
        self.verticalSlider_upper_BH.setRange(0, 255)
        self.verticalSlider_upper_BH.setValue(100)
        self.verticalSlider_upper_GS.setRange(0, 255)
        self.verticalSlider_upper_GS.setValue(255)
        self.verticalSlider_upper_RV.setRange(0, 255)
        self.verticalSlider_upper_RV.setValue(255)
        for rbutton in self.rb_dict.keys():
            rbutton.clicked.connect(self.change_types)
        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_set_params.clicked.connect(self.set_color_channel)
        self.pushButton_merge.clicked.connect(self.merge_img)
        self.pushButton_draw_line.clicked.connect(self.draw_img)
        self.actionOpen.triggered.connect(self.open_files)
        self.pushButton_end.clicked.connect(self.end)

    def open_files(self):
        self.end = True
        filename = QFileDialog.getOpenFileName(filter="mp4 files (*.mp4)", directory="../sample_video")
        filename = filename[0]
        video_name = os.path.basename(filename)
        print("open file:", video_name)
        if not video_name:
            return
        else:
            self.cam = cv2.VideoCapture(filename)

    def read_video(self):
        if self.cam is not None:
            ret, self.frame = self.cam.read()
            if ret:
                self.frame = cv2.resize(self.frame, (640, 360),
                                        interpolation=cv2.INTER_AREA)
            return ret
        else:
            print("open video")
            return

    def start(self):
        cv2.destroyAllWindows()
        while True:
            if self.end:
                ret = self.read_video()
                if not ret:
                    return
                else:
                    cv2.imshow("ori", self.frame)
                    k = cv2.waitKey(33)
                    if k == ord('q'):
                        break
            else:
                self.end = True
                break
        self.clear_cam()

    def set_color_channel(self):
        cv2.destroyAllWindows()
        while True:
            if self.end:
                ret = self.read_video()
                if not ret:
                    return
                check, line_frame = self.detect_line()
                if check:
                    cv2.imshow("ori", self.frame)
                    cv2.imshow("frame", line_frame)
                    k = cv2.waitKey(33)
                    if k == ord('q'):
                        break
                else:
                    print("set color channel")
                    return
            else:
                self.end = True
                break
        self.clear_cam()

    def detect_line(self):
        frame_img = self.frame.copy()
        color_type, lower_scale, upper_scale = self.change_types()
        if color_type is "bgr":
            b_mask = cv2.inRange(frame_img, lower_scale, upper_scale)
            frame_img = cv2.bitwise_and(frame_img, frame_img, mask=b_mask)
            self.bgr_param = lower_scale, upper_scale
            return True, frame_img
        elif color_type is cv2.COLOR_BGR2HSV:
            frame_img = cv2.cvtColor(frame_img, color_type)
            h_mask = cv2.inRange(frame_img, lower_scale, upper_scale)
            frame_img = cv2.bitwise_and(frame_img, frame_img, mask=h_mask)
            self.hsv_param = lower_scale, upper_scale
            return True, frame_img
        else:
            return False, frame_img

    def change_types(self):
        color_type = None
        for rbutton, button_type in self.rb_dict.items():
            if rbutton.isChecked():
                color_type = button_type
        if color_type is not None:
            lower_BH, lower_GS, lower_RV, upper_BH, upper_GS, upper_RV = self.set_scale()
            self.label_lower_BH.setText(f"{lower_BH}")
            self.label_lower_GS.setText(f"{lower_GS}")
            self.label_lower_RV.setText(f"{lower_RV}")
            self.label_upper_BH.setText(f"{upper_BH}")
            self.label_upper_GS.setText(f"{upper_GS}")
            self.label_upper_RV.setText(f"{upper_RV}")
            lower_scale = np.array([lower_BH, lower_GS, lower_RV])
            upper_scale = np.array([upper_BH, upper_GS, upper_RV])
            return color_type, lower_scale, upper_scale
        else:
            lower_scale = None
            upper_scale = None
            return color_type, lower_scale, upper_scale

    def set_scale(self):
        lower_BH = self.verticalSlider_lower_BH.value()
        lower_GS = self.verticalSlider_lower_GS.value()
        lower_RV = self.verticalSlider_lower_RV.value()
        upper_BH = self.verticalSlider_upper_BH.value()
        upper_GS = self.verticalSlider_upper_GS.value()
        upper_RV = self.verticalSlider_upper_RV.value()
        return lower_BH, lower_GS, lower_RV, upper_BH, upper_GS, upper_RV

    def merge_img(self):
        cv2.destroyAllWindows()
        while True:
            if self.end:
                ret = self.read_video()
                if not ret:
                    return
                img = self.mask_draw()
                if img is not None:
                    cv2.imshow("img", img)
                    k = cv2.waitKey(33)
                    if k == ord('q'):
                        break
                else:
                    print("set values")
                    return
            else:
                self.end = True
                break
        self.clear_cam()

    def mask_draw(self):
        img = self.frame.copy()
        if self.bgr_param is not None:
            bgr_mask = cv2.inRange(img, self.bgr_param[0], self.bgr_param[1])
            hvs_mask = cv2.inRange(img, self.hsv_param[0], self.hsv_param[1])
            bgr_img = cv2.bitwise_and(img, img, mask=bgr_mask)
            hsv_img = cv2.bitwise_and(img, img, mask=hvs_mask)
            img = cv2.addWeighted(bgr_img, 1., hsv_img, 1., 0.)
            return img
        else:
            return

    def draw_img(self):
        cv2.destroyAllWindows()
        while True:
            ret = self.read_video()
            if self.end:
                if not ret:
                    return
                else:
                    mask_img = self.mask_draw()
                    if mask_img is not None:
                        gray_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)
                        gray_img = cv2.GaussianBlur(gray_img, (3, 3), 0)
                        edged = cv2.Canny(gray_img, 15, 150)
                        roi_mask = self.set_roi(edged)
                        lines = cv2.HoughLinesP(roi_mask, 2, np.pi / 180, 15, 10, 18)
                        line_img = np.zeros((*roi_mask.shape, 3), dtype=np.uint8)
                        if lines is None or len(lines) == 0:
                            print("Not detect lines")
                            pass
                        else:
                            slopes, new_lines = self.set_slope(lines)
                            lines = new_lines
                            right_lines, left_lines = self.judge_direct(lines, slopes, line_img)
                            right_m, right = self.right_lines(right_lines)
                            left_m, left = self.left_lines(left_lines)
                            y1, y2, right_x1, right_x2, left_x1, left_x2 = self.find_end_lines(right_m, left_m,
                                                                                               line_img)
                            draw_img = self.draw_lines(right, left, y1, y2, right_x1, right_x2, left_x1, left_x2,
                                                       line_img)
                            cv2.imshow("draw_frame", draw_img)
                        cv2.imshow("ori", self.frame)
                        k = cv2.waitKey(50)
                        if k == ord('q'):
                            break
                    else:
                        print("set values")
                        return
            else:
                self.end = True
                break
        self.clear_cam()

    def set_roi(self, edged):
        fshape = self.frame.shape
        roi = np.array([[((fshape[1] * (1 - 0.85)) // 2, fshape[0]),
                         ((fshape[1] * (1 - 0.07)) // 2, fshape[0] - fshape[0] * 0.4),
                         (fshape[1] - (fshape[1] * (1 - 0.07)) // 2, fshape[0] - fshape[0] * 0.4),
                         (fshape[1] - (fshape[1] * (1 - 0.85)) // 2, fshape[0])]], dtype=np.int32)
        mask = np.zeros_like(edged)
        if len(edged.shape) > 2:
            count = edged.shape[2]
            mask_color = (255, 255, 255) * count
            print(mask_color)
        else:
            mask_color = 255
        cv2.fillPoly(mask, roi, mask_color)
        roi_mask = cv2.bitwise_and(edged, mask)
        return roi_mask

    def set_slope(self, lines):
        slopes = []
        new_lines = []
        slope_thred = 0.5
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if x2 - x1 == 0.:  # 0으로 나눠지는 것 방지
                slope = 999.  # 경사의 각 설정

            else:
                slope = (y2 - y1) / (x2 - x1)

            if abs(slope) > slope_thred:
                slopes.append(slope)
                new_lines.append(line)

        return slopes, new_lines

    def judge_direct(self, lines, slopes, line_img):
        right_lines = []
        left_lines = []
        for i, line in enumerate(lines):
            x1, y1, x2, y2 = line[0]
            img_x_center = line_img.shape[1] / 2  # 가로축의 중앙점
            if slopes[i] > 0 and x1 > img_x_center and x2 > img_x_center:
                right_lines.append(line)
            elif slopes[i] < 0 and x1 < img_x_center and x2 < img_x_center:
                left_lines.append(line)
        return right_lines, left_lines

    def right_lines(self, right_lines):
        right = True
        right_lines_x = []
        right_lines_y = []
        for line in right_lines:
            x1, y1, x2, y2 = line[0]
            right_lines_x.append(x1)
            right_lines_x.append(x2)
            right_lines_y.append(y1)
            right_lines_y.append(y2)
        if len(right_lines_x) > 1:
            right_m = np.polyfit(right_lines_x, right_lines_y, 1)  # 다항식 계수 찾기 y=m*x+b
        else:
            right_m = 1, 1
            right = False
        return right_m, right

    def left_lines(self, left_lines):
        left = True
        left_lines_x = []
        left_lines_y = []
        for line in left_lines:
            x1, y1, x2, y2 = line[0]
            left_lines_x.append(x1)
            left_lines_x.append(x2)
            left_lines_y.append(y1)
            left_lines_y.append(y2)
        if len(left_lines_x) > 1:
            left_m = np.polyfit(left_lines_x, left_lines_y, 1)  # 다항식 계수 찾기
        else:
            left_m = 1, 1
            left = False
        return left_m, left

    def find_end_lines(self, right_m, left_m, line_img):
        y1 = line_img.shape[0]
        y2 = line_img.shape[0] * (1 - 0.4)
        right_x1 = (y1 - right_m[1]) / right_m[0]
        right_x2 = (y2 - right_m[1]) / right_m[0]
        left_x1 = (y1 - left_m[1]) / left_m[0]
        left_x2 = (y2 - left_m[1]) / left_m[0]
        y1 = int(y1)
        y2 = int(y2)
        right_x1 = int(right_x1)
        right_x2 = int(right_x2)
        left_x1 = int(left_x1)
        left_x2 = int(left_x2)
        return y1, y2, right_x1, right_x2, left_x1, left_x2

    def draw_lines(self, right, left, y1, y2, right_x1, right_x2, left_x1, left_x2, line_img):
        if right:
            cv2.line(line_img, (right_x1, y1), (right_x2, y2), (0, 255, 255), 10)
        if left:
            cv2.line(line_img, (left_x1, y1), (left_x2, y2), (0, 255, 255), 10)

        draw_img = cv2.addWeighted(line_img, 0.9, self.frame, 1., 0.)
        return draw_img

    def end(self):
        if self.cam is not None:
            print("exit video!!!")
            cv2.destroyAllWindows()
            self.end = False
        else:
            return

    def clear_cam(self):
        self.cam.release()
        self.cam = None
        cv2.destroyAllWindows()


def main():
    app = QApplication(sys.argv)
    editor = MyWindow()
    editor.show()
    app.exec_()


if __name__ == "__main__":
    main()


