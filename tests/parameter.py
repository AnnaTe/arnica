import cv2
import numpy as np
#from matplotlib import pyplot as plt


file0 = '/home/rio/Dokumente/Uni/project/beispiel/testbilder/flug15/DSC01401.JPG'
img = cv2.imread(file0)


histo = np.zeros([256,1, 3])

for i in range(3):
    histo[:,:,i] = cv2.calcHist([img],[i],None,[256],[0,256])


summe = img.shape[0]* img.shape[1]

histo_rel = histo / summe

cum_b = np.cumsum(histo_rel[:,:,0]*100)
cum_g = np.cumsum(histo_rel[:,:,1]*100)
cum_r = np.cumsum(histo_rel[:,:,2]*100)

mb = np.mean(cum_b)
mg = np.mean(cum_g)
mr = np.mean(cum_r)

#mbgr = np.mean(cum_b + cum_g + cum_r)

mib = np.min(np.where(cum_b > 50))
mig = np.min(np.where(cum_g > 50))
mir = np.min(np.where(cum_r > 50))

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hell = np.mean(img_hsv[:,:,0])

file1= "/home/rio/Dokumente/Uni/project/beispiel/testbilder/flug30/DSC01743.JPG"

img1 = cv2.imread(file1)

img1_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

hell2 = np.mean(img1_hsv[:,:,0])

imgg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

histo = np.zeros([256,1, 3])

for i in range(3):
    histo[:,:,i] = cv2.calcHist([img1],[i],None,[256],[0,256])

#############################################################
import cv2
import numpy as np
#from datatest import Data
from matplotlib.patches import Circle
import matplotlib.pyplot as plt

img = "/home/rio/Dokumente/Uni/beispiel/testbilder/flug15/DSC01412.JPG"
img3 = "/home/rio/Dokumente/Uni/project/src/abb/ergebnisse/probleme/image.png"
#img2 = "/home/rio/Dokumente/Uni/beispiel/testbilder/flug30/DSC01743.JPG"

import matplotlib.pyplot as plt

test = Data(img3)
#test.crop(50)

# minBGR = np.array((0, 133, 200))
# maxBGR = np.array((122, 255, 255))
# maskBGR = cv2.inRange(test.cropped, minBGR, maxBGR)
# test.seg = cv2.bitwise_and(test.cropped, test.cropped, mask=maskBGR)
# nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(maskBGR, connectivity=8)
# sizes = stats[1:, -1]
# nb_components = nb_components - 1

# test2 = Data(img2)
# test2.crop(50)
#
# minBGR = np.array((0, 133, 200))
# maxBGR = np.array((122, 255, 255))
# maskBGR2 = cv2.inRange(test2.cropped, minBGR, maxBGR)
# test2.seg = cv2.bitwise_and(test2.cropped, test2.cropped, mask=maskBGR2)
#
# nb_components2, output2, stats2, centroids2 = cv2.connectedComponentsWithStats(maskBGR2, connectivity=8)
# sizes2 = stats2[1:, -1]
# nb_components2 = nb_components2 - 1

test.filter(100,30)

fig, ax = plt.subplots(1, figsize=(15, 10))
ax.set_aspect('equal')
number, output, stats, centroids = cv2.connectedComponentsWithStats(test.blob[:, :, 0], connectivity=8)

nb_components = number - 1
left = stats[1:,0]
top = stats[1:,1]
width = stats[1:,2]
height = stats[1:,3]
sizes = stats[1:,4]

center = np.array((centroids[1:, 0].astype(int), centroids[1:, 1].astype(int))).transpose()

lowsize = np.mean(sizes)*2

centers = []
radius = []
for i in range(0, nb_components):
    if sizes[i] >= lowsize:
        if width[i]/height[i] >= 0.75 and width[i]/height[i] < 1.5:
            pass
        elif width[i]/height[i] < 0.75 and width[i]/height[i] >= 0.415:
            center[i] = np.array([(width[i]/2) + left[i], (height[i]/4) + top[i]])
            centers.append([(width[i]/2) + left[i], (height[i]/4) * 3 + top[i]])
            radius.append(np.min((width[i],height[i])))
        elif width[i]/height[i] < 2.5 and width[i]/height[i] >= 1.5:
            center[i] = np.array([(width[i] /4) + left[i], (height[i] / 2) + top[i]])
            centers.append([(width[i] / 4) * 3 + left[i], (height[i] / 2) + top[i]])
            radius.append(np.min((width[i],height[i])))
        elif width[i]/height[i] >= 2.5 and width[i]/height[i] < 3.5:
            centers.append([(width[i]/4)+left[i],(height[i]/2)+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/4)*3+left[i],(height[i]/2)+top[i]])
            radius.append(np.min((width[i],height[i])))
        elif width[i]/height[i] < 0.415 and width[i]/height[i] >= 0.29:
            centers.append([(width[i]/2)+left[i],(height[i]/4)+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/2)+left[i],(height[i]/4)*3+top[i]])
            radius.append(np.min((width[i],height[i])))
        elif width[i]/height[i] < 0.29 and width[i]/height[i] >= 0.225:
            center[i] = np.array([(width[i] / 2) + left[i], (height[i] / 5) + top[i]])
            centers.append([(width[i]/2)+left[i],(height[i]/5)*2+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/2)+left[i],(height[i]/5)*3+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/2)+left[i],(height[i]/5)*4+top[i]])
            radius.append(np.min((width[i],height[i])))
        elif width[i]/height[i] >= 3.5 and width[i]/height[i] < 4.5:
            center[i] = np.array([(width[i] / 5) + left[i], (height[i] / 2) + top[i]])
            centers.append([(width[i]/5)*2+left[i],(height[i]/2)+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/5)*3+left[i],(height[i]/2)+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/5)*4+left[i],(height[i]/2)+top[i]])
            radius.append(np.min((width[i],height[i])))
        elif width[i]/height[i] < 0.225:
            centers.append([(width[i]/2)+left[i],(height[i]/6)+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/2)+left[i],(height[i]/6)*2+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/2)+left[i],(height[i]/6)*4+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/2)+left[i],(height[i]/6)*5+top[i]])
            radius.append(np.min((width[i],height[i])))
        elif width[i]/height[i] >= 4.5:
            centers.append([(width[i]/6)+left[i],(height[i]/2)+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/6)*2+left[i],(height[i]/2)+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/6)*5+left[i],(height[i]/2)+top[i]])
            radius.append(np.min((width[i],height[i])))
            centers.append([(width[i]/6)*4+left[i],(height[i]/2)+top[i]])
            radius.append(np.min((width[i],height[i])))

ax.imshow(cv2.cvtColor(test.cropped, cv2.COLOR_BGR2RGB))
ax.axis("off")
count = 0
for i in range(centroids[1:, 1].shape[0]):
    circ = Circle(tuple(center[i]),np.min(stats[i + 1, 2:4]), color="r", linewidth=1, fill=False)
    ax.add_patch(circ)
    count += 1
for a in range(len(centers)):
    circ2 = Circle(tuple(centers[a]), int(radius[a]), color="b", linewidth=1, fill=False)
    ax.add_patch(circ2)
    count += 1

#name = self.path[:-12] + self.path[-19:-13] + "circ/" + self.name + "circ" + ".png"

#plt.savefig("/home/rio/Dokumente/Uni/project/src/abb/ergebnisse/probleme/circles-adjust.png", dpi=300)
#plt.title("{} flowers counted.".format(count))
plt.show()

#normalize data
# normsizes = sizes / np.sqrt(np.sum(sizes**2))
#
#
# # relative to number of blobs
# sizes_rel = np.zeros(sizes.shape[0])
# for i in range(sizes.shape[0]):
#   sizes_rel [i] = sizes[i] / np.mean(sizes)
