import glob
import cv2
import numpy as np


def OpenAllfromFolder (path):
    fpaths = glob.glob(path)

    data = np.empty((len(fpaths), 2457, 3681, 3), dtype=np.uint8)
    for i, fpath in enumerate(fpaths):
        img = cv2.imread(fpath)
        img = img[int(img.shape[0] * 0.25):int(img.shape[0] * 0.75) + 1,
          int(img.shape[1] * 0.25):int(img.shape[1] * 0.75) + 1, :]
        data[i, ...] = img
    return data

def Crop (img, percent):
    lower = percent/100/2
    upper = percent/100+lower
    img = img[int(img.shape[0] * lower):int(img.shape[0] * upper) + 1,
          int(img.shape[1] * lower):int(img.shape[1] * upper) + 1, :]
    return img


