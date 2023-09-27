import subprocess
from youtube_downloader import titulos
def run_whisper(quality,path_subtitles,path_videos):
    global titulos
    for titulo in titulos:
        command=(f"whisper {path_videos+titulo} --task transcribe --model {quality} --verbose False --output_format srt --output_dir {path_subtitles}")
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in process.stdout:print(line, end='')