import os
path_response=input("You want to save the subtitles locally or on google drive? (l =local, g=google): ")
path="/content/drive/MyDrive/whisper_for_all/" if path_response[0].lower()=="g" else "/content/legendas/"
if path_response=="g":
    from google.colab import drive
    drive.mount('/content/drive')
quality=input("what will be the quality mode? (ex :small, medium, large): ")
links=[]
while True:
    link=input("put the links of the videos, to stop please type (quit): ")
    if link=="quit":
        break
    else:
        links.append(link)

from youtube_downloader import*
if not os.path.exists("/content/audios"):
   os.mkdir("/content/audios")
videos=playlist_expander(links)
download_all_audios(videos)
from whisper_requests import *
run_whisper(quality,path)





