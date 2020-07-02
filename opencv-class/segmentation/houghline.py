import cv2
import numpy as np
import show_imgs as si
IMG_PATH = "../sample_imgs"

def hough_lines():
    img_names = [IMG_PATH + f"/bookshelf{i+1}.jpg" for i in range(3)]
    images = {}
    for i, name in enumerate(img_names):
        srcimg = cv2.imread(name, cv2.IMREAD_COLOR)
        images[f"srcimg{i+1}"] = srcimg
        # 이미지 전처리
        grayimg = cv2.cvtColor(srcimg, cv2.COLOR_BGR2GRAY)
        blurimg = cv2.GaussianBlur(grayimg, (3, 3), 0)
        cannyimg = cv2.Canny(blurimg, 100, 200)
        images[f"canny{i+1}"] = cannyimg
        # hough transform
        lines = cv2.HoughLinesP(cannyimg, 1, np.pi/180, 50, None, 50, 10)
        print("lines", lines)
        result = images[f"srcimg{i+1}"].copy()
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(result, (x1,y1), (x2,y2), (0,0,255), 1)
        images[f"houghline{i+1}"] = result

    result_img = si.show_imgs(images, "hough lines", 3, 1200)

if __name__ == "__main__":
    hough_lines()