import random
import cv2
import matplotlib.pyplot as plt
import numpy as np


#sp15 = random.sample(range(1339,1562), k=10)
#sp20 = random.sample(range(1121,1322), k=10)
sp30 = random.sample(range(1573,1798), k=10)

path30 = []
for i in sp30:
    path30.append("/media/rio/INTENSO/Arnika/2018-06-14_A1_JF_flight_arnika/flight30/DSC0{}.JPG".format(i))


data = np.empty((len(path30), 984, 1473, 3), dtype=np.uint8)
for i, fpath in enumerate(path30):
        img = cv2.imread(fpath)
        percent = 20
        lower = (50 - (percent / 2)) / 100
        upper = (50 + (percent / 2)) / 100
        img = img[int(img.shape[0] * lower):int(img.shape[0] * upper) + 1,
                       int(img.shape[1] * lower):int(img.shape[1] * upper) + 1, :]
        data[i, ...] = img


plt.figure(figsize=(10, 20))

for i in range(10):
    plt.subplot(5,2,i+1)
    plt.imshow(cv2.cvtColor(data[i], cv2.COLOR_BGR2RGB))
    plt.title(sp30[i])
    plt.xticks([])
    plt.yticks([])

plt.tight_layout()
plt.show()

