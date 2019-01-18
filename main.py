import cv2
import glob
import os, errno
import numpy as np

from filter.colorsegmentation import Yellow
#from Functions.imageplots import subplot12
from filter.openfiles import Crop
from filter.blobelimination import BlobDetection, applyMask

path = "/home/rio/Dokumente/Uni/Bachelorarbeit/arnika/Beispielbilder/Beispielordner/*.JPG"
fpaths = glob.glob(path)

#create output directory
try:
    os.makedirs("output")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# open every image individually in a loop
for fpath in fpaths:
     img = cv2.imread(fpath)
     img = Crop(img, 50)
     seg = yellow(img)
     out = BlobDetection(seg)
     img_masked = applyMask(out, img)
     out_path = "/home/rio/Dokumente/Uni/Bachelorarbeit/arnika/Project/output/" + fpath[-12:-4] + "seg" + ".PNG"
     cv2.imwrite(out_path, img_masked)

#subplot12 (testimg, seg, title1 = "BGR Image", title2 = "Yellow colow segmentation")
#singleplot(seg)




