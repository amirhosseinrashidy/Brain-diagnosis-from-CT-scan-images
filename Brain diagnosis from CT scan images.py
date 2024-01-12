#ARAH 

import cv2
import numpy as np

def detect_brain_bleeding(image_path):
    
    image = cv2.imread(image_path)

    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    
    edges = cv2.Canny(blurred_image, 50, 150)

    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    centers = []

    
    for contour in contours:
        
        area = cv2.contourArea(contour)

    
        if area > 100:
            
            M = cv2.moments(contour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            centers.append((cX, cY))

           
            cv2.circle(image, (cX, cY), 5, (0, 255, 0), -1)

    
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_brain_bleeding("path/to/your/ct_scan_image.jpg")

# Amir Hossein