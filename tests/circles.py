
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
import cv2

# Get an example image
#import matplotlib.cbook as cbook
#image_file = cbook.get_sample_data('grace_hopper.png')
#path = "/home/rio/Dokumente/Uni/Bachelorarbeit/arnika/Beispielbilder/output/DSC01341seg0.png"
#path = "/home/rio/Dokumente/Uni/project/DSC01506seg.png"
path = "/home/rio/Dokumente/Uni/project/beispiel/testbilder/flug30/flug30seg/DSC01573seg100.png"
img = cv2.imread(path)

path2 = "/home/rio/Dokumente/Uni/project/beispiel/testbilder/flug30/DSC01573.JPG"

org = cv2.imread(path2)
org = org[int(org.shape[0] * 0.05):int(org.shape[0] * 0.95) + 1, int(org.shape[1] * 0.05):int(org.shape[1] * 0.95) + 1, :]


def circleplot(img, orginal = True):


    fig,ax = plt.subplots(1)
    ax.set_aspect('equal')
    number, output, stats, centroids = cv2.connectedComponentsWithStats(img[:,:,0], connectivity=8)
    center = list(zip(centroids[1:,0].astype(int),centroids[1:,1].astype(int)))

    radius = stats[1:,3]

    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    ax.axis("off")

    # Now, loop through coord arrays, and create a circle at each x,y pair
    for i in range(centroids[1:, 1].shape[0]):
        circ = Circle(center[i], radius[i], color="#ee0000", linewidth=1, fill=False)
        ax.add_patch(circ)

    # Show the image
    return plt.show()


# Create a figure. Equal aspect so circles look circular
fig,ax = plt.subplots(1)
ax.set_aspect('equal')

number, output, stats, centroids = cv2.connectedComponentsWithStats(img[:,:,0], connectivity=8)


center = list(zip(centroids[1:,0].astype(int),centroids[1:,1].astype(int)))

radius = stats[1:,3]
# Show the orginial image
#path2 = "/home/rio/Dokumente/Uni/Bachelorarbeit/arnika/Beispielbilder/Beispielordner/DSC01341.JPG"
#path2 = "/home/rio/Dokumente/Uni/project/DSC01506crop.JPG"


#ax.imshow(cv2.cvtColor(org, cv2.COLOR_BGR2RGB))
ax.imshow(cv2.cvtColor(org, cv2.COLOR_BGR2RGB))

ax.axis("off")

# Now, loop through coord arrays, and create a circle at each x,y pair
for i in range(centroids[1:,1].shape[0]):
    circ = Circle(center[i],radius[i], color = "#ee0000",linewidth=1, fill=False)
    ax.add_patch(circ)

# Show the image
plt.show()
