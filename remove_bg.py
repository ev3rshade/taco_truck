import cv2
import numpy as np

def remove_background(input_image_path, output_image_path, threshold=0.9):

    image = cv2.imread(input_image_path)
    if image is None:
        print("Error: Image not found.")
        return
    
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    ret, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) 
    cv2.imshow('Binary Threshold', thresh1) 
    cv2.waitKey(0)

    thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_GRAY2RGB)


    mask = np.zeros(thresh1.shape[:2], np.uint8)

    
    rectangle = (10, 10, thresh1.shape[1] - 10, thresh1.shape[0] - 10)

  
    bgd_model = np.zeros((1, 65), np.float64)
    fg_model = np.zeros((1, 65), np.float64)

    cv2.grabCut(thresh1, mask, rectangle, bgd_model, fg_model, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    
    result = thresh1 * mask2[:, :, np.newaxis]

    result_with_alpha = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA) 
    result_with_alpha[:, :, 3] = mask2 * 255 

    cv2.imwrite(output_image_path, result_with_alpha)
    

    cv2.imshow('Foreground with Removed Background', result_with_alpha)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image = "C:\\Users\\hsken\\projects_problems\\hackathons\\BoilermakeXII\\taco_truck\\catinaBowl.png"  # Replace with your input image file path
output_image = "C:\\Users\\hsken\\projects_problems\\hackathons\\BoilermakeXII\\taco_truck\\image.png"  # Path to save the output image (preferably .png to support transparency)
remove_background(input_image, output_image)
