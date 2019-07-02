import pytest

import cv2
import numpy as np
import matplotlib

def open_image_cv2 (path):
	img = cv2.imread(path)
	return img

def numpy_array (R,G,B):
	BGR = np.array((B,G,R))
	return BGR

def matplotlib_test (colorname):
	return matplotlib.colors.cnames[name]

testpath = "/home/rio/Dokumente/Uni/project/bilder/DSC01496.JPG"

def test():
	assert open_image_cv2(testpath).shape[2] == 3
	assert numpy_array(255,133,0) == np.array(0,133,255)
	assert matplotlib_test('white') == '#FFFFFF'


