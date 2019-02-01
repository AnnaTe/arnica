import cv2
import numpy as np


class Data:
    def __init__(self, path):
        self.img = self.open(path)
        self.cropped = self.img
        self.seg = self.img
        self.blob = self.img

    @staticmethod
    def open(path):
        img = cv2.imread(path)
        return img

    def crop(self, percent=50):
        lower = (50 - (percent / 2)) / 100
        upper = (50 + (percent / 2)) / 100
        self.cropped = self.img[int(self.img.shape[0] * lower):int(self.img.shape[0] * upper) + 1,
          int(self.img.shape[1] * lower):int(self.img.shape[1] * upper) + 1, :]
        return self.cropped

    def yellow(self, image):
        minBGR = np.array((0, 133, 225))
        maxBGR = np.array((122, 255, 255))
        maskBGR = cv2.inRange(image, minBGR, maxBGR)
        self.seg = cv2.bitwise_and(image, image, mask=maskBGR)
        return self.seg

    def blobelimination(self, lowsize=100):
        'blob detection with variing size'
        for d in range(self.seg.shape[-1]):
            nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(self.seg[:, :, d], connectivity=8)
            sizes = stats[1:, -1]
            nb_components = nb_components - 1
            min_size = lowsize
            mask = np.zeros((self.seg.shape[-3], self.seg.shape[-2], self.seg.shape[-1]))
            for i in range(0, nb_components):
                if sizes[i] >= min_size:
                    mask[output == i + 1, d] = 255

        # flatten to keep all the values
        out_sum = mask[:, :, 0] + mask[:, :, 1] + mask[:, :, 2]
        # stack array again in 3-Dimensions to keep shape
        out_stack = np.stack((out_sum, out_sum, out_sum), axis=-1)
        # make 3-D mask
        sum_mask = np.ma.make_mask(out_stack, shrink=False)
        # make a masked array
        self.blob = np.ma.array(self.cropped, mask=sum_mask)
        # put inverse of mask to 0
        self.blob[~self.blob.mask] = 0
        return self.blob


    # def __repr__(self):
    #     #print ("Data.open(path)")
    #     pass
    #
    # def __str__(self):
    #     pass


path = "/home/rio/Dokumente/Uni/project/DSC01506.JPG"
test = Data(path)

