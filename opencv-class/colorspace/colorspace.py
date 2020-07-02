import os
import cv2
import numpy as np

IMG_PATH = "../sample_imgs"
filename = os.path.join(IMG_PATH, "spiderman.jpg")
bgrimg = cv2.imread(filename)
# color space 변환
grayimg = cv2.cvtColor(bgrimg, cv2.COLOR_BGR2GRAY)
# binary image 만들기
binaryimg = grayimg.copy()
binaryimg[grayimg < 120] = 0
binaryimg[grayimg >= 120] = 255
grayimg = cv2.cvtColor(grayimg, cv2.COLOR_GRAY2BGR)
binaryimg = cv2.cvtColor(binaryimg, cv2.COLOR_GRAY2BGR)

concatimg = np.concatenate([binaryimg, grayimg, bgrimg], axis=1)
cv2.imshow("binary gray BGR", concatimg)
cv2.waitKey()

channels = np.concatenate([bgrimg[:,:,0], bgrimg[:,:,1], bgrimg[:,:,2]], axis=1)
cv2.imshow("BGR channels", channels)
cv2.waitKey()
hsvimg = cv2.cvtColor(bgrimg, cv2.COLOR_BGR2HSV)
hueimg = hsvimg[:,:,0]
valueimg = hsvimg[:,:,2]
faceimg = np.zeros(bgrimg.shape, dtype=np.uint8)
# hue 값이 낮은 얼굴 영역 추출
faceimg[hueimg<13, :] = bgrimg[hueimg<13, :]
bodyimg = np.zeros(bgrimg.shape, dtype=np.uint8)
# hue 값이 높은 슈트의 빨간 영역 추출
bodyimg[hueimg>170, :] = bgrimg[hueimg>170, :]
# hue 값이 100~130인 슈트의 파란 영역 추출
bodyimg[(hueimg>100) & (hueimg<130), :] = bgrimg[(hueimg>100) & (hueimg<130), :]
bodyimg[valueimg>220] = 0
segment = np.concatenate([faceimg, bodyimg], axis=1)
cv2.imshow("segmented image", segment)
cv2.waitKey()
