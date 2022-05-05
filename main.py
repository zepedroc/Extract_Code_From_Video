import os
from time import time
from checkResult import check_correct_result
from convertVideoToText import convert_video_to_text
from downloadFromYoutube import download_youtube_video

start_time = time()


def main():
    download_youtube_video()
    convert_video_to_text()


main()

stop_time = time()
process_time = round(stop_time - start_time, 1)
minutes = int(process_time / 60)
seconds = int(process_time % 60)
print('Time elapsed:', minutes, 'minutes and ', seconds, 'seconds')
