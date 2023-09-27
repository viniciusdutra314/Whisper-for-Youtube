import os
path_response=input("You want to save the subtitles locally or on google drive? (l =local, g=google): ")
path_subtitles="/content/drive/MyDrive/whisper_for_all/legendas/" if path_response[0].lower()=="g" else "/content/legendas/"
path_videos="/content/drive/MyDrive/whisper_for_all/videos/" if path_response[0].lower()=="g" else "/content/videos/"
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
videos=playlist_expander(links)
download_all_videos(videos,path_videos)
from whisper_requests import *
run_whisper(quality,path_subtitles,path_videos)





