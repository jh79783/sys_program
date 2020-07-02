import cv2
import numpy as np
import show_imgs as si
IMG_PATH = "../sample_imgs"

def hough_circles():
    img_names = [IMG_PATH + f"/mole{i+1}.jpg" for i in range(3)]
    images = {}
    for i, name in enumerate(img_names):
        srcimg = cv2.imread(name, cv2.IMREAD_COLOR)
        images[f"srcimg{i + 1}"] = srcimg
        gray = cv2.cvtColor(srcimg, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        # 알고리즘에 들어가진 않지만 중간과정을 이해하기 위한 엣지 영상
        cannyimg = cv2.Canny(gray, 100, 200)
        images[f"canny{i+1}"] = cannyimg
        # hough circle transform
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 30, None,
                                   param1=200, param2=50, maxRadius=60)
        # result: 1xNx3 float -> Nx3 uint16
        circles = np.around(circles).astype(np.uint16)
        circles = circles[0]
        print("circles\n", circles)
        result = srcimg.copy()
        for circle in circles:  # circle: (x, y, r)
            result = cv2.circle(result, (circle[0], circle[1]), circle[2], (0,0,255), 2)
        images[f"houghcircle{i+1}"] = result

    result_img = si.show_imgs(images, "hough circles", 3, 1200)

if __name__ == "__main__":
    hough_circles()