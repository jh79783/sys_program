import cv2
import numpy as np
import show_imgs as si
IMG_PATH = "../sample_imgs"


def blur():
    image = cv2.imread(IMG_PATH + "/jjang.jpg")
    kernel_sizes = [(1, 1), (3, 3), (5, 5), (7, 7), (7, 1), (1, 7)]
    filter_imgs = {}
    blur_imgs = {}
    for ksize in kernel_sizes:
        title = f"ksize: {ksize}"
        kernel = np.ones(ksize)
        kernel /= kernel.size
        filter_imgs[title] = cv2.filter2D(image, -1, kernel)
        blur_imgs[title] = cv2.blur(image, ksize)
    resimg = si.show_imgs(filter_imgs, "cv2.filter2D", 3)
    resimg = si.show_imgs(blur_imgs, "cv2.blur", 3)


def gaussian():
    image = cv2.imread(IMG_PATH + "/jjang.jpg")
    kernel_size = (5, 5)
    blur_imgs = {}
    blur_imgs["original"] = image
    blur_imgs["blur"] = cv2.blur(image, kernel_size)
    blur_imgs["GaussianBlur"] = cv2.GaussianBlur(image, kernel_size, 0)
    result_img = si.show_imgs(blur_imgs, "GaussianBlur", 3, 1000)

def bilateral():
    image = cv2.imread(IMG_PATH + "/jjang.jpg")
    kernel_size = (5, 5)
    blur_imgs = {}
    blur_imgs["original"] = image
    blur_imgs["gaussian"] = cv2.GaussianBlur(image, kernel_size, 0)
    blur_imgs["bilateral (5,50,50)"] = cv2.bilateralFilter(image, 5, 50, 50)
    blur_imgs["bilateral (5,150,150)"] = cv2.bilateralFilter(image, 5, 150, 150)
    result_img = si.show_imgs(blur_imgs, "Bilateral Filter", 2)



if __name__ == "__main__":
    # gaussian()
    bilateral()
