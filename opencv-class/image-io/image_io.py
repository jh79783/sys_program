import os
import numpy as np
import cv2

# 파일명 만들기
IMG_PATH = "../sample_imgs"
filename = os.path.join(IMG_PATH, "superson.jpg")
print("filename:", filename)
# 네 가지 형식으로 영상 불러오기
img_color = cv2.imread(filename, cv2.IMREAD_COLOR)
img_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
img_unchange = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
# 영상 보여주기
cv2.imshow("superson-color", img_color)
cv2.imshow("superson-gray", img_gray)
cv2.imshow("superson-unchange", img_unchange)
key = cv2.waitKey()
print("key in:", key, "==", chr(key))
if key == ord('s'):
    filename = os.path.join(IMG_PATH, "superson-save.jpg")
    cv2.imwrite(filename, img_color)
cv2.destroyAllWindows()

