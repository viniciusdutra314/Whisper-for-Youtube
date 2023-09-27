import pytube
from unidecode import unidecode
import string

titulos=[]

def playlist_expander(links : list) -> list:
  for url in links:
    if "playlist" in url:
        videos=[pytube.Playlist(url) for url in links]
        return videos
  videos=links
  return videos

def download_single_video(link,path_videos) -> list:
  yt = pytube.YouTube(link)
  title=yt.title
  title = unidecode(title) #removing special characters
  title = title.translate(title.maketrans('','',string.punctuation))
  title=title.replace(" ","_")
  title=title.lower() +".mp4"
  video_stream = yt.streams.get_highest_resolution()
  video_stream.download(filename=path_videos+title)
  titulos.append(title)

def download_all_videos(videos,path_videos):
  if isinstance(videos[0],str):
      for video in videos:
          download_single_video(video,path_videos)
  else:
      for playlists in videos:
          for video in playlists:
              download_single_video(video,path_videos)