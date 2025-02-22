# trying circle detection

import numpy as np
import cv2 as cv

img = cv.imread("C:\\Users\\hsken\\projects_problems\\hackathons\\BoilermakeXII\\taco_truck\\catinaBowl.png")
output = cv.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (101,101), 0)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20,
                          param1=50, param2=30, minRadius=0, maxRadius=0)

detected_circles = np.uint16(np.around(circles))

for (x, y, r) in detected_circles[0, :]:
    cv.circle(output, (x,y), r, (0, 255, 0), 3)

cv.imshow('output', output)
cv.imshow('gray', gray)
cv.waitKey(0)
cv.destroyAllWindows()