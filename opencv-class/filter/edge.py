import cv2
import numpy as np
import show_imgs as si
IMG_PATH = "../sample_imgs"

def sobel():
    image = cv2.imread(IMG_PATH + "/yumi-cells.jpg", cv2.IMREAD_GRAYSCALE)
    sobel_imgs = {"original": image}
    sobel_imgs["Sobel dx"] = cv2.Sobel(image, ddepth=-1, dx=1, dy=0, ksize=3)
    sobel_imgs["Sobel dy"] = cv2.Sobel(image, ddepth=-1, dx=0, dy=1, ksize=3)
    sobel_imgs["Sobel dx+dy"] = cv2.add(sobel_imgs["Sobel dx"], sobel_imgs["Sobel dy"])
    sobel_imgs["Scharr dx"] = cv2.Scharr(image, ddepth=-1, dx=1, dy=0)
    sobel_imgs["Scharr dy"] = cv2.Scharr(image, ddepth=-1, dx=0, dy=1)
    result_img = si.show_imgs(sobel_imgs, "Sobel & Scharr", 3)

def laplacian():
    image = cv2.imread(IMG_PATH + "/yumi-cells.jpg", cv2.IMREAD_GRAYSCALE)
    lapla_imgs = {"original": image}
    sobel_dx = cv2.Sobel(image, ddepth=-1, dx=1, dy=0, ksize=3)
    sobel_dy = cv2.Sobel(image, ddepth=-1, dx=0, dy=1, ksize=3)
    lapla_imgs["Sobel dx+dy"] = cv2.add(sobel_dx, sobel_dy)
    lapla_imgs["Laplacian"] = cv2.Laplacian(image, -1)
    result_img = si.show_imgs(lapla_imgs, "Laplacian", 3)

def canny():
    image = cv2.imread(IMG_PATH + "/arya.jpg", cv2.IMREAD_GRAYSCALE)
    canny_imgs = {"original": image}
    canny_imgs["Laplacian"] = cv2.Laplacian(image, -1, scale=2)
    canny_imgs["Canny (100, 200)"] = cv2.Canny(image, 100, 200)
    canny_imgs["Canny (200, 255)"] = cv2.Canny(image, 150, 255)
    result_img = si.show_imgs(canny_imgs, "Canny", 2)

def erode_and_dilate():
    srcimg = cv2.imread(IMG_PATH + "/marvel.jpg", cv2.IMREAD_GRAYSCALE)
    srcimg = salt_and_pepper_noise(srcimg)
    # erode and dilate, and then show them
    images = {"original": srcimg}
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    images["erode"] = cv2.erode(srcimg, kernel)
    images["dilate"] = cv2.dilate(srcimg, kernel)
    result_img = si.show_imgs(images, "Erode and Dilate", 1)

def salt_and_pepper_noise(image):
    towhite = np.unravel_index(np.random.randint(0, image.size, 100), image.shape)
    toblack = np.unravel_index(np.random.randint(0, image.size, 100), image.shape)
    image[towhite] = 255
    image[toblack] = 0
    return image

def morphologies():
    srcimg = cv2.imread(IMG_PATH + "/marvel.jpg", cv2.IMREAD_GRAYSCALE)
    srcimg = salt_and_pepper_noise(srcimg)
    # erode and dilate, and then show them
    images = {"original": srcimg}
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    images["opening"] = cv2.morphologyEx(srcimg, cv2.MORPH_OPEN, kernel)
    images["closing"] = cv2.morphologyEx(srcimg, cv2.MORPH_CLOSE, kernel)
    images["gradient"] = cv2.morphologyEx(srcimg, cv2.MORPH_GRADIENT, kernel)
    images["tophat"] = cv2.morphologyEx(srcimg, cv2.MORPH_TOPHAT, kernel)
    images["blackhat"] = cv2.morphologyEx(srcimg, cv2.MORPH_BLACKHAT, kernel)
    result_img = si.show_imgs(images, "Morphology Ops", 2)

if __name__ == "__main__":
    # sobel()
    # laplacian()
    # canny()
    # erode_and_dilate()
    morphologies()

