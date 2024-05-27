import cv2
import imutils
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\jayac\AppData\Local\Programs\Python\Python39\Scripts\pytesseract.exe"

# read and resize image to the required size
image = cv2.imread('image.jpg')
image = imutils.resize(image, width=500)
cv2.imshow("Original Image", image)

a = cv2.imwrite('4.jpg', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
