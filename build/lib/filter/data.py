import cv2
import numpy as np


class Data:
    """This is the Data class that stores the images and the altered copies for fast accessibility."""

    def __init__(self, path):
        self.img = self._open(path)
        self.cropped = np.copy(self.img)
        self.seg = np.copy(self.cropped)
        self.blob = np.copy(self.cropped)
        self.path = path
        self.name = self.path.split('/')[-1].split('.')[0]
        self.count = 0

    @staticmethod
    def _open(path):
        img = cv2.imread(path)
        return img

    def crop(self, percent=20):
        """crop of image from the center in percent"""
        if percent == 100:
            pass
        # borders from center
        lower = (50 - (percent / 2)) / 100
        upper = (50 + (percent / 2)) / 100
        self.cropped = self.img[int(self.img.shape[0] * lower):int(self.img.shape[0] * upper) + 1,
                       int(self.img.shape[1] * lower):int(self.img.shape[1] * upper) + 1, :]

    def yellow(self, image, lowsize=50):
        """segmentation of yellow area in the image with minimum size of segmented Components"""
        minBGR = np.array((0, 133, 200))
        maxBGR = np.array((122, 255, 255))
        maskBGR = cv2.inRange(image, minBGR, maxBGR)
        holefill = cv2.morphologyEx(maskBGR, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
        self.seg = cv2.bitwise_and(image, image, mask=holefill)

        # blob dectection including sizes
        nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(holefill, connectivity=8)
        sizes = stats[1:, -1]
        groupsize = np.mean(sizes) * 2
        number = nb_components - 1
        mask = np.zeros(maskBGR.shape, dtype='uint8')
        height = stats[1:, 2]
        width = stats[1:, 3]
        self.count = nb_components - 1
        korr = 0
        for i in range(0, number):
            if sizes[i] >= lowsize:
                mask[output == i + 1] = 255
                if sizes[i] >= groupsize:
                    if width[i] / height[i] >= 0.75 and width[i] / height[i] < 1.5:
                        pass
                    elif width[i] / height[i] < 0.75 and width[i] / height[i] >= 0.415:
                        korr += 1
                    elif width[i] / height[i] < 2.5 and width[i] / height[i] >= 1.5:
                        korr += 1
                    elif width[i] / height[i] >= 2.5 and width[i] / height[i] < 3.5:
                        korr += 2
                    elif width[i] / height[i] < 0.415 and width[i] / height[i] >= 0.29:
                        korr += 2
                    elif width[i] / height[i] < 0.29 and width[i] / height[i] >= 0.225:
                        korr += 3
                    elif width[i] / height[i] >= 3.5 and width[i] / height[i] < 4.5:
                        korr += 3
                    elif width[i] / height[i] < 0.225:
                        korr += 4
                    elif width[i] / height[i] >= 4.5:
                        korr += 4
            else:
                self.count -= 1
        self.count += korr
        self.blob = cv2.bitwise_and(image, image, mask=mask)

    def filter(self, percent=50, lowsize=100):
        """calls the crop and segmentation methods together"""
        self.crop(percent)
        self.yellow(self.cropped, lowsize)

    def circleplot(self):
        """plots red circles around the flowers. This function not called from application."""
        from matplotlib.patches import Circle
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(1, figsize=(15, 10))
        ax.set_aspect('equal')
        number, output, stats, centroids = cv2.connectedComponentsWithStats(self.blob[:, :, 2], connectivity=8)
        center = list(zip(centroids[1:, 0].astype(int), centroids[1:, 1].astype(int)))
        radius = stats[1:, 3]

        ax.imshow(cv2.cvtColor(self.cropped, cv2.COLOR_BGR2RGB))
        ax.axis("off")

        for i in range(centroids[1:, 1].shape[0]):
            circ = Circle(center[i], radius[i], color="r", linewidth=0.5, fill=False)
            ax.add_patch(circ)

        # Show the image
        return plt.show()


