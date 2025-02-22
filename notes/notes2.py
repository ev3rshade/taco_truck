# open image using matplotlib

import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\hsken\\projects_problems\\hackathons\\BoilermakeXII\\taco_truck\\catinaBowl.png")
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# display image with plt.imshow()
plt.imshow(RGB_img)

plt.waitforbuttonpress()
plt.close('all')