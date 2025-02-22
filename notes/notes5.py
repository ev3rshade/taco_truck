# blurring with cv2

import cv2

img = cv2.imread("C:\\Users\\hsken\\projects_problems\\hackathons\\BoilermakeXII\\taco_truck\\catinaBowl.png")

cv2.imshow("original", img)
cv2.waitKey(0)

Gassian = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow("Gassian", Gassian)
cv2.waitKey(0)

Median = cv2.medianBlur(img, 5)
cv2.imshow("Median", Median)
cv2.waitKey(0)

Bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("Bilateral", Bilateral)
cv2.waitKey(0)
cv2.destoryAllWindows()