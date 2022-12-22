from pytube import YouTube
from pytube import Playlist
from pytube import Channel

from flask import Flask,request,jsonify,render_template,send_file


#download a single video..
def Download(link):
    print(link)
    vid = YouTube(link)
    vid = vid.streams.get_highest_resolution()
    try:
        print("Downloading...")
        vid.download()
        print("Downloaded")
        return vid.title
    except:
        print(f"An error has occurred while downloading {vid.title}") 
        print("Download is completed successfully")
    return ""
        

def Download_playlist(link):
    p = Playlist(link)
    print(f'Downloading: {p.title}')
    print(f"no of videos = {len(p.videos)}")
    l=[]

    for video in p.videos:
        try:
            print(f"downoading {video.title}")
            video.streams.first().download()
            l.append(video.title + ".mp4")
            
        except:
            print(f"error occured while downloading {video.title}")
    print("Download is completed successfully")
    return l


app = Flask(__name__)


@app.route("/", methods = ["GET","POST"])

def home():
    if request.method == 'POST':
        link = request.form.get('link')
        mode = request.form.get('mode')

        if int(mode) == 1:
            title = Download(link)
            return send_file(f"{title}.mp4")

        if int(mode) == 2:
            titles = Download(link)
            for i in titles:  
                return send_file(i)
            
            
            
    return render_template('index.html')




if __name__ == '__main__':
    # Running the application and leaving the debug mode ON
    app.run(debug = True)
