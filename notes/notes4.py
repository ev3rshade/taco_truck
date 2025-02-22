# image resizing using OpenCV

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\hsken\\projects_problems\\hackathons\\BoilermakeXII\\taco_truck\\catinaBowl.png", 1)

half = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)

(h, w) = img.shape[:2]
aspect_ratio = w/h
new_height = int(1050 / aspect_ratio)

bigger = cv2.resize(img, (1050, new_height))

stretch_near = cv2.resize(img, (780, 540), interpolation=cv2.INTER_NEAREST)

Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [img, half, bigger, stretch_near]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()

plt.waitforbuttonpress()
plt.close('all')