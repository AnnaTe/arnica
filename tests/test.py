import cv2
import glob
import os, errno
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from filter.colorsegmentation import yellow
from filter.imageplots import subplot12
from filter.openfiles import crop
from filter.blobelimination import BlobDetection, applyMask

path = "/home/rio/Dokumente/Uni/Bachelorarbeit/arnika/Beispielbilder/Beispielordner/DSC01506.JPG"


fig = plt.figure(figsize=(20,6))

# open every image individually in a loop
img = cv2.imread(path)
img = crop(img,50)
seg = yellow(img)
org = img.copy()
ims = []
for i in range(10,100,10):
    out = BlobDetection(seg, lowsize= i)
    img_masked = applyMask(out, img)
    #out_path = "/home/rio/Dokumente/Uni/Bachelorarbeit/arnika/Project/" + path[-12:-4] + "seg" + str(i) + ".PNG"
    #cv2.imwrite(out_path, img_masked)
    index = 250 + (i//10)
    plt.subplot(index)
    plt.imshow(cv2.cvtColor(img_masked, cv2.COLOR_BGR2RGB))
    plt.title("low_size" + str(i))


#ani = animation.ArtistAnimation(fig, ims, interval=10, blit = True, repeat_delay=100)

plt.show()
#subplot12 (org, img, title1 = "BGR Image", title2 = "Yellow colow segmentation")
#singleplot(seg)

#versuch nur die dunklen Blüten darzustellen
newBGR = np.array([100,230,230])
dark = cv2.inRange(seg,nonzero,newBGR)
lowseg = cv2.bitwise_and(seg, seg, mask = dark)
plt.imshow(cv2.cvtColor(lowseg, cv2.COLOR_BGR2RGB))
plt.show()


