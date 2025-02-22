# a basic example of how to use openCV to read an image (based on geeks for geeks)
# https://www.geeksforgeeks.org/reading-image-opencv-using-python/

import cv2

# read the image
img = cv2.imread("C:\\Users\\hsken\\projects_problems\\hackathons\\BoilermakeXII\\taco_truck\\catinaBowl.png", cv2.IMREAD_COLOR)

# display the image
cv2.imshow("image", img)

# event listener for key press
cv2.waitKey(0)

# close all windows
cv2.destroyAllWindows()