from time import time
from languages import chooseLang
from convertVideoToText import convert_video_to_text
from downloadFromYoutube import download_youtube_video

start_time = time()


def main():
    chosen_lang = chooseLang()

    download_youtube_video()
    convert_video_to_text(chosen_lang)


main()

stop_time = time()
process_time = round(stop_time - start_time, 1)
minutes = int(process_time / 60)
seconds = int(process_time % 60)
print('Time elapsed:', minutes, 'minutes and ', seconds, 'seconds')
