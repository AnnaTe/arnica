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

img = "/home/rio/Dokumente/Uni/project/beispiel/testbilder/flug15/DSC01412.JPG"
img2 = "/home/rio/Dokumente/Uni/project/beispiel/testbilder/flug30/DSC01743.JPG"

import matplotlib.pyplot as plt

test = Data(img)
test.crop(50)

minBGR = np.array((0, 133, 200))
maxBGR = np.array((122, 255, 255))
maskBGR = cv2.inRange(test.cropped, minBGR, maxBGR)
test.seg = cv2.bitwise_and(test.cropped, test.cropped, mask=maskBGR)
nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(maskBGR, connectivity=8)
sizes = stats[1:, -1]
nb_components = nb_components - 1

test2 = Data(img2)
test2.crop(50)
minBGR = np.array((0, 133, 200))
maxBGR = np.array((122, 255, 255))
maskBGR2 = cv2.inRange(test2.cropped, minBGR, maxBGR)
test2.seg = cv2.bitwise_and(test2.cropped, test2.cropped, mask=maskBGR2)

nb_components2, output2, stats2, centroids2 = cv2.connectedComponentsWithStats(maskBGR2, connectivity=8)
sizes2 = stats2[1:, -1]
nb_components2 = nb_components2 - 1

fig = plt.figure()
ax = plt.gca()

n, bins, patches = ax.hist(sizes, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
ax.set_yscale('log')
plt.show()

#normalize data
normsizes = sizes / np.sqrt(np.sum(sizes**2))


# relative to number of blobs
sizes_rel = np.zeros(sizes.shape[0])
  ...: for i in range(sizes.shape[0]):
  ...:     sizes_rel [i] = sizes[i] / np.mean(sizes)