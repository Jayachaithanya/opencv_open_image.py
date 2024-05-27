import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\jayac\AppData\Local\Programs\Python\Python39\Scripts\pytesseract.exe"

# perform edge detection
edged = cv2.imread('4.jpg', image)
edged = cv2.Canny(gray, 170, 200)
cv2.imshow("Canny Edges", edged)

d = cv2.write('7.jpg', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
