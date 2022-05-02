from PIL import Image
import pytesseract

# import cv2 as cv

code = 'assets/onlyCode.png'
full = 'assets/full.png'
full2 = 'assets/full2.png'
grid = 'assets/grid.png'

# add tesseract to the path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


text1 = pytesseract.image_to_string(Image.open(grid), lang="eng")
print('-----------grid---------------')
print(text1)

text1 = pytesseract.image_to_string(Image.open(code), lang="eng")
print('-----------code---------------')
print(text1)

text1 = pytesseract.image_to_string(Image.open(full), lang="eng")
print('-----------full---------------')
print(text1)

text1 = pytesseract.image_to_string(Image.open(full2), lang="eng")
print('-----------full2---------------')
print(text1)
