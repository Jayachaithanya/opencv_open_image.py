import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\jayac\AppData\Local\Programs\Python\Python39\Scripts\pytesseract.exe"

# blur to reduce noise
gray1 = cv2.imread('4.jpg',image)
gray1 = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("Bilateral Filter", gray1)

c = cv2.write('6.jpg',image)

cv2.waitKey(0)
cv2.destroyAllWindows()
