import cv2
import numpy as np
import show_imgs as si
IMG_PATH = "../sample_imgs"
NO_REGION = 50
AREA_THR = 100
LABEL_BEGIN = 100

# def count_balls():
#     srcimg = cv2.imread(IMG_PATH + "/ballpool.jpg", cv2.IMREAD_COLOR)
#     images, mask = prepare_mask(srcimg)
#     result_img = si.show_imgs(images, "floodfill", 3)

def prepare_mask(srcimg):
    images = {"original": srcimg}
    hsvimg = cv2.cvtColor(srcimg, cv2.COLOR_BGR2HSV)
    images["hue"] = hsvimg[:, :, 0]
    images["value"] = hsvimg[:, :, 2]
    # canny edge와 value 값을 이용해서 no-region mask 만들기
    canny = cv2.Canny(images["value"], 80, 160)
    images["canny"] = canny
    mask = np.zeros(canny.shape, np.uint8)
    mask[canny > 10] = NO_REGION
    mask[images["value"] < 70] = NO_REGION
    images["mask mask"] = mask
    # 상하좌우에 1픽셀씩 추가 (H, W) -> (H+2, W+2)
    mask = np.pad(mask, ((1, 1), (1, 1)))
    return images, mask

# def count_balls():
#     srcimg = cv2.imread(IMG_PATH + "/ballpool.jpg", cv2.IMREAD_COLOR)
#     images, mask = prepare_mask(srcimg)
#     result_img = si.show_imgs(images, "floodfill", 3)
#     mask, label = find_balls(images, mask)
#     print("number of balls:", label - LABEL_BEGIN)

def find_balls(images, mask):
    label = LABEL_BEGIN
    ih, iw, ch = images["original"].shape
    hueimg = images["hue"].copy()
    for v in range(0, ih, 5):
        for u in range(0, iw, 5):
            if mask[v+1, u+1] > 0:
                continue
            flags = (4 | cv2.FLOODFILL_MASK_ONLY | (label << 8))
            area, hueimg, mask, rect = \
                cv2.floodFill(hueimg, mask, (u, v), None, 1, 1, flags)
            print(f"floodfill at {(u, v)}, pixels={area}, rect={rect}, label={label}")
            if area > AREA_THR:
                label += 1
                cv2.imshow("floodfill mask", mask)
                cv2.waitKey(100)
            else:   # 영역이 너무 작으면 mask를 다시 NO_REGION 으로 채우기
                mask[mask == label] = NO_REGION
    cv2.waitKey()
    return mask, label

def count_balls():
    srcimg = cv2.imread(IMG_PATH + "/ballpool.jpg", cv2.IMREAD_COLOR)
    images, mask = prepare_mask(srcimg)
    result_img = si.show_imgs(images, "floodfill", 3)
    mask, label = find_balls(images, mask)
    print("number of balls:", label - LABEL_BEGIN)
    images["labeled balls"] = colorize_regions(mask, label)
    result_img = si.show_imgs(images, "floodfill", 3)

def colorize_regions(mask, label_max):
    image = np.zeros((mask.shape[0], mask.shape[1], 3), np.uint8)
    for label in range(LABEL_BEGIN, label_max, 1):
        image[mask==label, :] = np.random.randint(50, 256, 3)
    return image[1:-1, 1:-1, :]


if __name__ == "__main__":
    count_balls()

