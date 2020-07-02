import cv2
import numpy as np
import show_imgs as si
IMG_PATH = "../sample_imgs"
SKY_LABEL = 1
GOOSE_LABEL = 2

def watershed():
    srcimg = cv2.imread(IMG_PATH + "/wildgoose.jpg", cv2.IMREAD_COLOR)
    images = {"original": srcimg}
    # find apprent background(sky) and wild goose region
    gray = cv2.cvtColor(srcimg, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    images["threshold"] = binary
    app_sky = cv2.erode(binary, kernel, iterations=3)
    images["apparent sky"] = app_sky
    app_goose = cv2.dilate(binary, kernel, iterations=1)
    images["apparent wildgoose"] = app_goose
    images["undetermined"] = cv2.subtract(app_goose, app_sky)
    # create markers and watershed
    markers = np.zeros(gray.shape, dtype=np.int32)
    markers[app_sky > 0] = SKY_LABEL
    markers[app_goose == 0] = GOOSE_LABEL
    markers = cv2.watershed(srcimg, markers)
    # show contours of wild gooses
    labelimg = np.zeros_like(srcimg)
    labelimg[markers == -1, :] = (0, 0, 255)      # draw contours
    labelimg[markers == SKY_LABEL, :] = (200, 150, 100)
    labelimg[markers == GOOSE_LABEL, :] = srcimg[markers == GOOSE_LABEL, :]
    images["label"] = labelimg
    result_img = si.show_imgs(images, "watershed", 3)
    print((markers == GOOSE_LABEL)[150:160, 120:130])

if __name__ == "__main__":
    watershed()

    #