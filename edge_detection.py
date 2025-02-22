# canny edge detection using openCV

import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

   
frame = cv2.imread("C:\\Users\\hsken\\projects_problems\\hackathons\\BoilermakeXII\\taco_truck\\catinaBowl.png") 
blurred = cv2.GaussianBlur(frame, (31, 31), 0)

# calling the designed function for 
# finding edges 
canny_img = cv2.Canny(blurred, 50, 150) 

complete_ellipse.complete_curve_to_ellipse(canny_img)


contours, _ = cv2.findContours(canny_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = max(contours, key=cv2.contourArea)
    
# Fit an ellipse to the largest contour if it has enough points
if len(largest_contour) >= 5:
    ellipse = cv2.fitEllipse(largest_contour)
    
    # Draw the ellipse on the original image
    cv2.ellipse(frame, ellipse, (0, 255, 0), 2) # green for lettuce

# Displaying the input and output image   
plt.figure() 
f, plots = plt.subplots(2, 1)  
plots[0].imshow(frame) 
plots[1].imshow(canny_img) 

cv2.imshow('canny', canny_img)
cv2.imshow('og', frame)
cv2.waitKey(0)
