# edge detection example

from PIL import Image, ImageFilter
import cv2

image = Image.open(r"C:\\Users\\hsken\\projects_problems\\hackathons\\BoilermakeXII\\taco_truck\\bowlWithTray.png")

# converting image to grayscale
# requires input image to be of mode = Grayscale (L)

image = image.convert("L")

image = image.filter(ImageFilter.FIND_EDGES)

image.show()
cv2.waitKey(0)
cv2.destroyAllWindows()