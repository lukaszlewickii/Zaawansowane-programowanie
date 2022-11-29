import cv2
import pytesseract

from PIL import Image
from pytesseract import pytesseract

"""
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread("d:/Desktop/Zaawansowane programowanie/Laborki 9 - 22.11.22/newyork.jpg")

print(type(img))
print(img.shape)

cv2.imshow('image', img)
cv2.waitKey(0)
#cv2.destroyAllWindows()
"""

tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = r"D:\Desktop\Python\Visual Studio Code\Zaawansowane programowanie\Laborki 22.11 - opencv\image_1.jpg"

def readTextFromImage():
    img = Image.open(image)
    pytesseract.tesseract_cmd = tesseract_path
    text = pytesseract.image_to_string(img)
    print("Tekst:", text[:-1])

readTextFromImage()
