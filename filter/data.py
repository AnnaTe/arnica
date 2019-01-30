import cv2
import numpy as np


class Data:
    def __init__(self, path):
        #self.img = self.open(path)
        self.path = path


    #methods
    def open(self):
        img = cv2.imread(self.path)
        return img

    def crop (self, percent=50):
        lower = 100 - percent / 2 / 100
        upper = 100 + percent / 2 / 100
        img = self.img[int(self.img.shape[0] * lower):int(self.img.shape[0] * upper) + 1,
          int(self.img.shape[1] * lower):int(self.img.shape[1] * upper) + 1, :]
        return img

    def yellow(self, img):
        minBGR = np.array((0, 133, 225))
        maxBGR = np.array((122, 255, 255))
        maskBGR = cv2.inRange(img, minBGR, maxBGR)
        segBGR = cv2.bitwise_and(img, img, mask=maskBGR)
        return segBGR

    def __blobs(self, segImg, lowsize=100):
        'blob detection with variing size'
        for d in range(segImg.shape[-1]):
            nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(segImg[:, :, d], connectivity=8)
            sizes = stats[1:, -1]
            nb_components = nb_components - 1
            min_size = lowsize
            img_out = np.zeros((segImg.shape[-3], segImg.shape[-2], segImg.shape[-1]))
            for i in range(0, nb_components):
                if sizes[i] >= min_size:
                    img_out[output == i + 1, d] = 255
        return img_out

    def __applyMask(self, mask, img):
        # flatten to keep all the values
        out_sum = mask[:, :, 0] + mask[:, :, 1] + mask[:, :, 2]
        # stack array again in 3-Dimensions to keep shape
        out_stack = np.stack((out_sum, out_sum, out_sum), axis=-1)
        # make 3-D mask
        sum_mask = np.ma.make_mask(out_stack, shrink=False)
        # make a masked array
        img_masked = np.ma.array(img, mask=sum_mask)
        # put inverse of mask to 0
        img_masked[~img_masked.mask] = 0
        return img_masked

    def blobelimination (self, segimg, original, lowsize = 100):
        blobs = self.__blobs(segimg, lowsize)
        out = self.__applyMask(blobs, original)
        return out

    def __repr__(self):
        pass

    def __str__(self):
        pass






testpath = "/home/rio/Dokumente/Uni/project/DSC01506.JPG"

test = Data(testpath)