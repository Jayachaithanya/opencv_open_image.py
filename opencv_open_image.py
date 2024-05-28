#  used to open the file manager using openCV.

import cv2
# path 
path = r'4.jpg'

# Using cv2.imread() method 
# Using 0 to read image in grayscale mode 
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 

# Displaying the image 
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
