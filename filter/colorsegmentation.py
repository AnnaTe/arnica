import cv2
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

scalarMap = cm.ScalarMappable(norm=mpl.colors.Normalize(vmin=1, vmax=20), cmap=plt.get_cmap("Wistia"))
wistia = scalarMap.to_rgba(range(20))

# eliminate alpha channel
Gelb = wistia[:,:3]*255

minBGR = np.array((np.min(Gelb[:,2]),np.min(Gelb[:,1]), np.min(Gelb[:,0])))
maxBGR = np.array((np.max(Gelb[:,2]),np.max(Gelb[:,1]), np.max(Gelb[:,0])))

def Yellow (image):
    minBGR = np.array((0, 133, 225))
    maxBGR = np.array((122, 255, 255))
    maskBGR = cv2.inRange(image,minBGR,maxBGR)
    segBGR = cv2.bitwise_and(image, image, mask = maskBGR)
    return segBGR



