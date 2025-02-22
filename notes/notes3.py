# color spaces in openCV

import cv2

img = cv2.imread("C:\\Users\\hsken\\projects_problems\\hackathons\\BoilermakeXII\\taco_truck\\catinaBowl.png")
B, G, R = cv2.split(img)

cv2.imshow("original", img)
cv2.waitKey(0)

cv2.imshow("blue", B)
cv2.waitKey(0)

cv2.imshow("green", G)
cv2.waitKey(0)

cv2.imshow("red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()