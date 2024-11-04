import numpy as np
import cv2
from application.tools.transforms import get_affine_transform

def img_resize(img, cfg):

    img_xsize = img.shape[1]
    img_ysize = img.shape[0]
    c = np.array([float(img_xsize/2), float(img_ysize/2)], dtype=np.float32)
    s = np.array([float(img_xsize/200), float(img_ysize/200)], dtype=np.float32)
    # 仿射變換將原圖像素精確映射到縮小圖。通過三個基準點，我們生成變換矩陣，再利用這個矩陣來映射每個像素
    # 獲得旋轉矩陣
    trans = get_affine_transform(c, s, 0, cfg['MODEL']['IMAGE_SIZE'])

    # 根據旋轉矩陣進行反射變換
    input = cv2.warpAffine(
        img,
        trans,
        (int(cfg['MODEL']['IMAGE_SIZE'][0]), int(cfg['MODEL']['IMAGE_SIZE'][1])),
        flags=cv2.INTER_LINEAR)
    return input, c, s