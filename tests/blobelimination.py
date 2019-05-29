import cv2
import numpy as np

def BlobDetection (segImg, lowsize=100):
    for d in range(segImg.shape[-1]):
        nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(segImg[:,:,d], connectivity=8)
        sizes = stats[1:, -1]; nb_components = nb_components - 1
        min_size = lowsize
        img_out = np.zeros((segImg.shape[-3],segImg.shape[-2],segImg.shape[-1]))
        for i in range(0, nb_components):
            if sizes[i] >= min_size:
                img_out[output == i + 1,d] = 255
    return img_out

def applyMask (mask, img):
    # flatten to keep all the values
    out_sum = mask[:,:,0] + mask[:,:,1] + mask[:,:,2]
    # stack array again in 3-Dimensions to keep shape
    out_stack = np.stack((out_sum, out_sum, out_sum), axis= -1)
    # make 3-D mask
    sum_mask = np.ma.make_mask(out_stack, shrink = False)
    # make a masked array
    img_masked = np.ma.array(img, mask=sum_mask)
    # put inverse of mask to 0
    img_masked[~img_masked.mask] = 0
    return img_masked
