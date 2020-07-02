import os
import cv2
import numpy as np

IMG_PATH = "../sample_imgs"
filename = os.path.join(IMG_PATH, "jjang.jpg")
image = cv2.imread(filename)
# 영상 속성 확인
print(f"image info: shape={image.shape}, dtype={image.dtype}, size={image.size}")
# => image info: shape=(300, 326, 3), dtype=uint8, size=293400
cv2.imshow("jjangzeolmi", image)
cv2.waitKey()

channels = {"blue": 0, "green": 1, "red": 2}
bgr_means = {}
for color, chn in channels.items():
    color_sum = 0
    for v in range(image.shape[0]):         # vertical axis
        for u in range(image.shape[1]):     # horizontal axis
            color_sum += image[v, u, chn]
    bgr_means[color] = color_sum / image[:, :, chn].size
print("BGR means:", bgr_means)

image[:10, :, :] = 255      # 위에 흰 줄
image[-10:, :, :] = 0       # 아래에 검은 줄
image[:, :10, 0] = 255      # 왼쪽에 파란 줄
image[:, :10, 1:] = 0
image[:, -10:, 2] = 255     # 오른쪽에 빨간 줄
image[:, -10:, :2] = 0
cv2.imshow("jjangzeolmi", image)
cv2.waitKey()

image[100:200, 100, :] = 0
image[100:200, 200, :] = 0
image[100:200, 100, :] = 0
image[100, 100:200, :] = 0
image[200, 100:200, :] = 0
cv2.imshow("jjangzeolmi", image)
cv2.waitKey()