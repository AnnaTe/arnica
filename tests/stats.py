import cv2
import numpy as np
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


class Data:
    def __init__(self, path):
        self.img = self._open(path)
        self.cropped = np.copy(self.img)
        self.seg = np.copy(self.cropped)
        self.blob = np.copy(self.cropped)
        self.path = path
        self.name = self.path.split('/')[-1].split('.')[0]

    @staticmethod
    def _open(path):
        img = cv2.imread(path)
        return img

    def crop(self, percent=50):
        if percent == 100:
            pass
        # if percent == 0:
        lower = (50 - (percent / 2)) / 100
        upper = (50 + (percent / 2)) / 100
        self.cropped = self.img[int(self.img.shape[0] * lower):int(self.img.shape[0] * upper) + 1,
                       int(self.img.shape[1] * lower):int(self.img.shape[1] * upper) + 1, :]

    def yellow(self, image, lowsize=100):
        minBGR = np.array((0, 133, 200))
        maxBGR = np.array((122, 255, 255))
        maskBGR = cv2.inRange(image, minBGR, maxBGR)
        self.seg = cv2.bitwise_and(image, image, mask=maskBGR)

        if lowsize == 0:
            self.blob = self.seg

        else:
            # blob dectection including sizes
            nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(maskBGR, connectivity=8)
            sizes = stats[1:, -1]
            nb_components = nb_components - 1
            mask = np.zeros(maskBGR.shape, dtype='uint8')
            for i in range(0, nb_components):
                if sizes[i] >= lowsize:
                    mask[output == i + 1] = 255
            self.blob = cv2.bitwise_and(image, image, mask=mask)
            return self.blob

    def filter(self, percent=50, lowsize=100):
        self.crop(percent)
        self.yellow(self.cropped, lowsize)
        # self.blobelimination(lowsize)

    def circleplot(self):
        from matplotlib.patches import Circle
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(1, figsize=(15, 10))
        ax.set_aspect('equal')
        number, output, stats, centroids = cv2.connectedComponentsWithStats(self.blob[:, :, 0], connectivity=8)
        center = list(zip(centroids[1:, 0].astype(int), centroids[1:, 1].astype(int)))
        radius = stats[1:, 3]

        ax.imshow(cv2.cvtColor(self.cropped, cv2.COLOR_BGR2RGB))
        ax.axis("off")

        for i in range(centroids[1:, 1].shape[0]):
            circ = Circle(center[i], radius[i], color="r", linewidth=1, fill=False)
            ax.add_patch(circ)

        # name = self.path[:-12] + self.path[-19:-13] + "circ/" + self.name + "circ" + ".png"
        # plt.savefig(name, dpi=300)

        # Show the image
        return plt.show()


img1 = "/home/rio/Dokumente/Uni/beispiel/testbilder/flug15/DSC01412.JPG"
img2 = "/home/rio/Dokumente/Uni/beispiel/testbilder/flug30/DSC01743.JPG"

import matplotlib.pyplot as plt

test = Data(img1)
test.crop(50)

minBGR = np.array((0, 133, 200))
maxBGR = np.array((122, 255, 255))
maskBGR = cv2.inRange(test.cropped, minBGR, maxBGR)
test.seg = cv2.bitwise_and(test.cropped, test.cropped, mask=maskBGR)
nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(maskBGR, connectivity=8)
sizes = stats[1:, -1]
nb_components = nb_components - 1
height = stats[1:,3]

width = stats[1:,2]

# figure = plt.figure(dpi = 300)
#
# n, bins, patches = plt.hist(sizes,
#                             bins=int(sizes.shape[0]/10),
#                             density=True,
#                             edgecolor="#6A9662",
#                             color="#DDFFDD",
#                             log = True)
# n, bins, patches = plt.hist(height,
#                             bins=int(height.shape[0]/100),
#                             density=True,
#                             edgecolor="#d1771d",
#                             color="#efbc88",
#                             log = True,
#                             alpha = 0.5)
# n, bins, patches = plt.hist(width,
#                             bins=int(height.shape[0]/100),
#                             density=True,
#                             edgecolor="#a488ef",
#                             color="#d7c9ff",
#                             log = True,
#                             alpha = 0.5)
# plt.show()

meanpx = np.mean(sizes)
meanbox = np.mean(width)*np.mean(height)
if meanpx > meanbox:
    lowsize = int(meanpx/3)
    maxsize = int(meanpx)
else:
    lowsize = int(meanbox/3)
    maxsize = int(meanbox*6)
mask = np.zeros(maskBGR.shape, dtype='uint8')
for i in range(0, nb_components):
    if sizes[i] >= lowsize and sizes[i]<= maxsize:
        mask[output == i + 1] = 255
test.blob = cv2.bitwise_and(test.seg, test.seg, mask=mask)


test.circleplot()