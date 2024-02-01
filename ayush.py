import pytesseract
import cv2
print("Hello")
img = cv2.imread('C:/Users/ADMIN\Desktop/download.png')

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

text = pytesseract.image_to_string(img)
print(text)