import pytube
from unidecode import unidecode
import string
drive=False
path="/content/drive/MyDrive/whisper_for_all/" if drive else ""
links=["https://www.youtube.com/playlist?list=PLpaKFn4Q4GMOBAeqC1S5_Fna_Y5XaOQS2",'https://www.youtube.com/playlist?list=PLdo5W4Nhv31YU5Wx1dopka58teWP9aCee']

def playlist_expander(links : list) -> list:
  for url in links:
    if "playlist" in url:
        videos=[pytube.Playlist(url) for url in links]
        return videos
  videos=links
  return videos

videos=playlist_expander(links)

def download_audio(link : "str or list"):
  global path
  yt = pytube.YouTube(link)
  title=yt.title
  title = unidecode(title) #removing special characters
  title = title.translate(title.maketrans('','',string.punctuation))
  title= title.lower() +".mp3"
  save_path=path+title
  audio_stream = yt.streams.filter(only_audio=True).first()
  audio_stream.download(filename=title)

if isinstance(videos[0],str):
    for video in videos:
        download_audio(video)
else:
     for playlists in videos:
        for video in playlists:
            download_audio(video)
