from pytube import YouTube
from pytube import Playlist
from pytube import Channel


#download a single video..
def Download(link):
    vid = YouTube(link)
    vid = youtubeObject.streams.get_highest_resolution()
    try:
        vid.download()
    except:
        print(f"An error has occurred while downloading {vid.title}") 
    print("Download is completed successfully")

def Download_playlist(link):
    p = Playlist(link)
    print(f'Downloading: {p.title}')
    for video in p.videos:
        try:
            video.streams.first().download()
            print(f"{video.title} downloded")
        except:
            print(f"error occured while downloading {video.title}")
    print("Download is completed successfully")
    
def Download_channel(link):
    c = Channel(link)
    print(f'Downloading videos from: {c.channel_name}')
    for video in c.videos:
        try:
            video.streams.first().download()
            print(f"{video.title} downloded")
        except:
            print(f"error occured while downloading {video.title}")
    print("Download is completed successfully")
                

link = input("Enter the YouTube video URL: ")
Download(link)
