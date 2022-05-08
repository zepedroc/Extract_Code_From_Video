import os
import pytesseract
import cv2 as cv
from languages import handle_lang


def convert_video_to_text(lang):
    print('\nProcessing...')

    # add tesseract to the path
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    vid = cv.VideoCapture('assets/videoSample.mp4')

    totalFrames = 0

    # create file that will store the text / if it already exists, clean it
    if os.path.exists("assets/textFromVideo.txt"):
        with open('assets/textFromVideo.txt', 'w') as file:
            file.truncate()
        file.close()
    else:
        open('assets/textFromVideo.txt', 'x')

    while True:
        success, frame = vid.read()

        if not success:
            break

        # process one in every 300 frames
        if totalFrames % 300 == 0:
            text = pytesseract.image_to_string(frame, lang="eng")
            if len(text) >= 100:  # skip frames with less code

                # update text based on the chosen language
                updated_text = handle_lang(text, lang)
                new_frame_lines = updated_text.splitlines()

                line_found = False
                txt_file = open("assets/textFromVideo.txt", "r")
                saved_lines = txt_file.readlines()
                new_lines = []

                for idx1, new_line in enumerate(new_frame_lines):
                    if line_found:
                        break
                    for idx2, saved_line in enumerate(saved_lines):
                        # replace new line and the rest of the frame on the old file
                        if new_line.strip() == saved_line.strip():
                            line_found = True
                            for x in range(len(new_frame_lines) - idx1):
                                if idx2 + x < len(saved_lines):
                                    saved_lines[idx2 + x] = new_frame_lines[idx1 + x]
                                else:
                                    new_lines.append(new_frame_lines[idx1 + x])

                            # write the updated lines on the saved file
                            with open('assets/textFromVideo.txt', 'w') as file:
                                for line in saved_lines:
                                    file.write(line.strip() + '\n')
                            file.close()

                            # if added more lines that the file previously had
                            if len(new_lines) > 0:
                                with open('assets/textFromVideo.txt', 'a') as file:
                                    for line in new_lines:
                                        file.write(line.strip() + '\n')
                                file.close()
                            break

                # if content is new, append everything to the existing file
                if not line_found:
                    with open('assets/textFromVideo.txt', 'a') as file:
                        for line in new_frame_lines:
                            file.write(line.strip() + '\n')
                    file.close()

        totalFrames += 1

    # When everything done, release the capture
    vid.release()
