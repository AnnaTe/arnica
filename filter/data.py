import cv2

class Data:
    def __init__(self, path):
        self.img = cv2.imread(path)
        self.imgcrop = self.crop(self.img)


    #methods
    def crop (self, img, percent=50):
        lower = percent/100/2
        upper = percent/100+lower
        img = img[int(img.shape[0] * lower):int(img.shape[0] * upper) + 1,
          int(img.shape[1] * lower):int(img.shape[1] * upper) + 1, :]
        return img


testpath = "/home/rio/Dokumente/Uni/project/DSC01506.JPG"

test = Data(testpath)