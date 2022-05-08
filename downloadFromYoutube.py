from pytube import YouTube

def download_youtube_video():
    # ask for the link from user
    link = input("\nType youtube link: ")
    print("\nDownloading...")

    yt = YouTube(link)
    # Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    ys.download(filename='assets/videoSample.mp4')
    print("Download completed!!")