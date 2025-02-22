# denoising colored images

import numpy as np
import cv2
from matplotlib import pyplot as plt

# reading image from folder where it is stored
img = cv2.imread("C:\\Users\\hsken\\projects_problems\\hackathons\\BoilermakeXII\\taco_truck\\catinaBowl.png")
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

dst = cv2.fastNlMeansDenoisingColored(RGB_img, None, 10, 10, 7, 15)

plt.subplot(121), plt.imshow(RGB_img)
plt.subplot(122), plt.imshow(dst)

plt.show()
plt.waitforbuttonpress()
plt.close('all')