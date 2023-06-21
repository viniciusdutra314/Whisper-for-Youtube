import pytube
from unidecode import unidecode
import string

def playlist_expander(links : list) -> list:
  for url in links:
    if "playlist" in url:
        videos=[pytube.Playlist(url) for url in links]
        return videos
  videos=links
  return videos
titulos=[]
def download_single_audio(link : "str or list"):
  global path
  yt = pytube.YouTube(link)
  title=yt.title
  title = unidecode(title) #removing special characters
  title = title.translate(title.maketrans('','',string.punctuation))
  title=title.replace(" ","_")
  title=title.lower() +".mp3"
  audio_stream = yt.streams.filter(only_audio=True).first()
  audio_stream.download(filename="audios//"+title)
  titulos.append(title)
def download_all_audios(videos):
  if isinstance(videos[0],str):
      for video in videos:
          download_single_audio(video)
  else:
      for playlists in videos:
          for video in playlists:
              download_single_audio(video)