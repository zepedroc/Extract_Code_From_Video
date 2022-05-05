from pytube import YouTube

def download_youtube_video():
    # ask for the link from user
    link = input("Type youtube link: ")
    yt = YouTube(link)

    # Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    # Starting download
    print("Downloading...")
    ys.download(filename='assets/videoSample.mp4')
    print("Download completed!!")