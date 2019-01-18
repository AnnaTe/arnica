import matplotlib.pyplot as plt
import cv2

def subplot12 (image1, image2, title1 = "Image 1", title2 = "Image 2", figsize = [20, 10]):
    plt.rcParams['figure.figsize'] = figsize

    plt.subplot(1,2,1)
    plt.title(title1)
    plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
    plt.subplot(1,2,2)
    plt.title(title2)
    plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

    return plt.show()


def singleplot (image1, title1="Image 1", figsize=[20, 10]):
    plt.rcParams['figure.figsize'] = figsize

    plt.title(title1)
    plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

    return plt.show()
