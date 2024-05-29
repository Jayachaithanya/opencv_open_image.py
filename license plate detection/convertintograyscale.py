import cv2
import imutils
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\jayac\AppData\Local\Programs\Python\Python39\Scripts\pytesseract.exe"

# convert to gray scale
gray = cv2.imread('4.jpg', image)
image = cv2.imread('image.jpg')
image = imutils.resize(image, width=500)
cv2.imshow("Original Image", image)

b = cv2.write('4.jpg', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#  converts the image into black/white image.
#  try using in idle

