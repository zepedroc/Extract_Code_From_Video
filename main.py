import os
from PIL import Image
import pytesseract
import cv2 as cv

code = 'assets/onlyCode.png'
full = 'assets/full.png'
full2 = 'assets/full2.png'
grid = 'assets/grid.png'

if not os.path.exists('frames'):
    os.makedirs('frames')


vid = cv.VideoCapture('assets/videoSample.mp4')

totalFrames = 0
savingFrames = 1

while True:
    success, frame = vid.read()

    if not success:
        break

    # register one in every 200 frames
    if totalFrames % 200 == 0:
        cv.imwrite(f'frames/{savingFrames}.jpg', frame)
        savingFrames += 1

    totalFrames += 1

# cv.waitKey(0)
# When everything done, release the capture
vid.release()
cv.destroyAllWindows()


# add tesseract to the path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# text1 = pytesseract.image_to_string(Image.open(grid), lang="eng")
# print('-----------grid---------------')
# print(text1)

# text1 = pytesseract.image_to_string(Image.open(code), lang="eng")
# print('-----------code---------------')
# print(text1)

# text1 = pytesseract.image_to_string(Image.open(full), lang="eng")
# print('-----------full---------------')
# print(text1)

# text1 = pytesseract.image_to_string(Image.open(full2), lang="eng")
# print('-----------full2---------------')
# print(text1)
