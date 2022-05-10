import pytesseract
import cv2 as cv
from languages import chooseLang, handle_lang

# add tesseract to the path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def convert_image_to_text(img, lang):
    print('\nProcessing...')

    # turning the image black and white
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray) # we can pass a lang here as the 2nd param

    # update text based on the chosen language
    updated_text = handle_lang(text, lang)

    with open('assets/textFromImage2.txt', 'w+') as file:
        file.writelines(updated_text)



# chosen_lang = chooseLang()

# img = cv.imread('assets/img5.png')
# convert_image_to_text(img, chosen_lang)



