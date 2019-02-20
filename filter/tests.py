import cv2
import numpy as np

class Data:
    def __init__(self, path):
        self.img = self.open(path)
        self.cropped = np.copy(self.img)
        self.seg = np.copy(self.cropped)
        self.blob = np.copy(self.cropped)

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

    def crop2(self, percent=50):
        lower = (int(((50 - (percent / 2)) / 100) * self.img.shape[0]),
                 int(((50 - (percent / 2)) / 100) * self.img.shape[1]))
        upper = (int(((50 + (percent / 2)) / 100) * self.img.shape[0]),
                 int(((50 + (percent / 2)) / 100) * self.img.shape[1]))
        self.cropped = self.img[lower[0]:upper[0] + 1, lower[1]:upper[1] + 1, :]

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
        self.blob = np.copy(self.cropped)
        self.blob = np.ma.array(self.blob, mask=sum_mask)
        # put inverse of mask to 0
        self.blob[~self.blob.mask] = 0
        return self.blob

    def filter(self, percent, lowsize):
        self.crop(percent)
        self.yellow(self.cropped)
        self.blobelimination(lowsize)


    # def __repr__(self):
    #     #print ("Data.open(path)")
    #     pass
    #
    # def __str__(self):
    #     pass






if __name__ == "__main__":
    path = "/home/rio/Dokumente/Uni/project/DSC01506.JPG"
    test = Data(path)
    #import timeit

    #%timeit test.filter(percent=40, lowsize=140)

    import matplotlib.pyplot as plt

    plt.figure(1)

    plt.subplot(221)
    plt.imshow(cv2.cvtColor(test.img, cv2.COLOR_BGR2RGB))
    plt.title('original Image')

    plt.subplot(222)
    plt.imshow(cv2.cvtColor(test.cropped, cv2.COLOR_BGR2RGB))
    plt.title('cropped Image')

    plt.subplot(223)
    plt.imshow(cv2.cvtColor(test.seg, cv2.COLOR_BGR2RGB))
    plt.title('yellow segmentation')

    plt.subplot(224)
    plt.imshow(cv2.cvtColor(test.blob, cv2.COLOR_BGR2RGB))
    plt.title('blob reduction')

    plt.show()
