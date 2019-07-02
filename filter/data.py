import cv2
import numpy as np


class Data:
    """This is the Data class that stores the images and the altered copies for fast accessibility."""

    def __init__(self, path):
        self.img = self._open(path)
        self.cropped = np.copy(self.img)
        self.seg = np.copy(self.cropped)
        self.blob = np.copy(self.cropped)
        self.circle = np.copy(self.cropped)
        self.path = path
        self.name = self.path.split('/')[-1].split('.')[0]
        self.count = 0
        self.groupsize = 0

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
        # morphological filtering
        holefill = cv2.morphologyEx(maskBGR, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
        self.seg = cv2.bitwise_and(image, image, mask=holefill)

        # blob dectection including sizes
        nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(holefill, connectivity=8)
        sizes = stats[1:, -1]
        self.groupsize = np.mean(sizes) * 2
        number = nb_components - 1
        mask = np.zeros(maskBGR.shape, dtype='uint8')
        height = stats[1:, 3]
        width = stats[1:, 2]
        self.count = nb_components - 1
        korr = 0
        for i in range(0, number):
            if sizes[i] >= lowsize:
                mask[output == i + 1] = 255
            else:
                self.count -= 1
            if sizes[i] >= self.groupsize:
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
        self.count += korr
        self.blob = cv2.bitwise_and(image, image, mask=mask)

    def filter(self, percent=20, lowsize=50):
        """calls the crop and segmentation methods together"""
        self.crop(percent)
        self.yellow(self.cropped, lowsize)

    def circleplot(self):
        """adds red circles around the flowers."""
        number, output, stats, centroids = cv2.connectedComponentsWithStats(
            cv2.cvtColor(self.blob, cv2.COLOR_BGR2GRAY), connectivity=8)
        # center = list(zip(centroids[1:, 0].astype(int), centroids[1:, 1].astype(int)))
        center = np.array([centroids[1:, 0].astype(int), centroids[1:, 1].astype(int)]).transpose()
        self.circle = np.copy(self.cropped)
        left = stats[1:, 0]
        top = stats[1:, 1]
        width = stats[1:, 2]
        height = stats[1:, 3]
        sizes = stats[1:, 4]
        centers = []
        radius = []
        for i in range(0, (number - 1)):
            if sizes[i] >= self.groupsize:
                if width[i] / height[i] >= 0.75 and width[i] / height[i] < 1.5:
                    pass
                elif width[i] / height[i] < 0.75 and width[i] / height[i] >= 0.415:
                    center[i] = np.array([int((width[i] / 2) + left[i]), int((height[i] / 4) + top[i])])
                    centers.append([int((width[i] / 2) + left[i]), int((height[i] / 4) * 3 + top[i])])
                    radius.append(np.min((width[i], height[i])))
                elif width[i] / height[i] < 2.5 and width[i] / height[i] >= 1.5:
                    center[i] = np.array([int((width[i] / 4) + left[i]), int((height[i] / 2) + top[i])])
                    centers.append([int((width[i] / 4) * 3 + left[i]), int((height[i] / 2) + top[i])])
                    radius.append(np.min((width[i], height[i])))
                elif width[i] / height[i] >= 2.5 and width[i] / height[i] < 3.5:
                    centers.append([int((width[i] / 4) + left[i]), int((height[i] / 2) + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 4) * 3 + left[i]), int((height[i] / 2) + top[i])])
                    radius.append(np.min((width[i], height[i])))
                elif width[i] / height[i] < 0.415 and width[i] / height[i] >= 0.29:
                    centers.append([int((width[i] / 2) + left[i]), int((height[i] / 4) + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 2) + left[i]), int((height[i] / 4) * 3 + top[i])])
                    radius.append(np.min((width[i], height[i])))
                elif width[i] / height[i] < 0.29 and width[i] / height[i] >= 0.225:
                    center[i] = np.array([int((width[i] / 2) + left[i]), int((height[i] / 5) + top[i])])
                    centers.append([int((width[i] / 2) + left[i]), int((height[i] / 5) * 2 + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 2) + left[i]), int((height[i] / 5) * 3 + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 2) + left[i]), int((height[i] / 5) * 4 + top[i])])
                    radius.append(np.min((width[i], height[i])))
                elif width[i] / height[i] >= 3.5 and width[i] / height[i] < 4.5:
                    center[i] = np.array([int((width[i] / 5) + left[i]), int((height[i] / 2) + top[i])])
                    centers.append([int((width[i] / 5) * 2 + left[i]), int((height[i] / 2) + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 5) * 3 + left[i]), int((height[i] / 2) + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 5) * 4 + left[i]), int((height[i] / 2) + top[i])])
                    radius.append(np.min((width[i], height[i])))
                elif width[i] / height[i] < 0.225:
                    centers.append([int((width[i] / 2) + left[i]), int((height[i] / 6) + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 2) + left[i]), int((height[i] / 6) * 2 + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 2) + left[i]), int((height[i] / 6) * 4 + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 2) + left[i]), int((height[i] / 6) * 5 + top[i])])
                    radius.append(np.min((width[i], height[i])))
                elif width[i] / height[i] >= 4.5:
                    centers.append([int((width[i] / 6) + left[i]), int((height[i] / 2) + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 6) * 2 + left[i]), int((height[i] / 2) + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 6) * 5 + left[i]), int((height[i] / 2) + top[i])])
                    radius.append(np.min((width[i], height[i])))
                    centers.append([int((width[i] / 6) * 4 + left[i]), int((height[i] / 2) + top[i])])
                    radius.append(np.min((width[i], height[i])))

        self.count = 0
        for i in range(centroids[1:, 1].shape[0]):
            cv2.circle(self.circle, tuple(center[i]), int(np.min(stats[i + 1, 2:4])), color=(0, 0, 255), thickness=2)
            self.count += 1
        for a in range(len(centers)):
            cv2.circle(self.circle, tuple(centers[a]), int(radius[a]), color=(0, 0, 255), thickness=2)
            self.count += 1

        return self.circle




