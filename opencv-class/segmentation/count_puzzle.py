import cv2
import numpy as np
import show_imgs as si
IMG_PATH = "../sample_imgs"

def count_puzzle():
    img = cv2.imread(IMG_PATH + "/puzzle.jpg")
    ih, iw, ch = img.shape
    mask = np.zeros((ih+2, iw+2), dtype=np.uint8)
    images = {"original": img.copy()}
    cv2.imshow("image", img)
    cv2.waitKey()
    count = 0
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if mask[y+1, x+1] == 0:
                # flood fill로 채울 랜덤 색상 생성
                color = np.random.randint(20, 256, 3).tolist()
                ret, img, mask, rect = cv2.floodFill(img, mask, (x,y), color,
                                loDiff=(10,10,10), upDiff=(10,10,10), flags=8)
                mask_show = mask*255
                print(f"area={ret}, rect={rect}, mask value={mask[y+1, x+1]}")
                if ret > 500:   # 영역이 넓은 것만 퍼즐 조각으로 인정
                    cv2.imshow("image", img)
                    cv2.imshow("mask", mask_show)
                    cv2.waitKey(100)
                    count += 1
    print("total puzzle count:", count)
    cv2.destroyAllWindows()
    images["filled"] = img
    result_img = si.show_imgs(images, "floodfill", 2)
    cv2.imwrite(IMG_PATH + "/floodfill_puzzle.jpg", result_img)

if __name__ == "__main__":
    count_puzzle()