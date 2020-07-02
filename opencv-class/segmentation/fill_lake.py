import cv2
import numpy as np
import show_imgs as si
IMG_PATH = "../sample_imgs"

def fill_lake():
    srcimg = cv2.imread(IMG_PATH + "/sinjeong-lake.jpg", cv2.IMREAD_COLOR)
    images = {"original": srcimg}
    seed = (int(srcimg.shape[1]/2), int(srcimg.shape[0]/2))
    # 아무 처리하지 않고 바로 호수에 flood fill 적용
    fill_direct = srcimg.copy()
    mask = np.zeros((srcimg.shape[0]+2, srcimg.shape[1]+2), dtype=np.uint8)
    retval, fill_direct, mask, rect = \
        cv2.floodFill(fill_direct, mask, seed, newVal=(0, 255, 255),
                      loDiff=(2, 2, 2), upDiff=(2, 2, 2), flags=8)
    print(f"pixel area of lake WITHOUT preprocess={retval}, rect={rect}")
    fill_direct = cv2.circle(fill_direct, seed, 1, (0,0,255), 2)
    images["direct_floodfill"] = fill_direct
    # flood fill이 잘 퍼지도록 블러링 후 적용
    fill_blur = srcimg.copy()
    fill_blur = cv2.GaussianBlur(fill_blur, (3,3), 0)
    fill_blur = cv2.medianBlur(fill_blur, 3)
    mask = np.zeros((srcimg.shape[0] + 2, srcimg.shape[1] + 2), dtype=np.uint8)
    retval, fill_blur, mask, rect = \
        cv2.floodFill(fill_blur, mask, seed, newVal=(0, 255, 255),
                      loDiff=(2, 2, 2), upDiff=(2, 2, 2), flags=8 | (255 << 8))
    print(f"pixel area of lake WITH preprocess=   {retval}, rect={rect}")
    fill_blur = cv2.circle(fill_blur, seed, 1, (0,0,255), 2)
    images["blur_n_floodfill"] = fill_blur
    # 결과 출력
    images["final mask"] = cv2.cvtColor(mask[1:-1, 1:-1], cv2.COLOR_GRAY2BGR)
    result_img = si.show_imgs(images, "fill the lake", 2)

if __name__ == "__main__":
    fill_lake()