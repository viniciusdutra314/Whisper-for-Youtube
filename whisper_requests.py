import subprocess
from youtube_downloader import titulos
def run_whisper(quality):
    global titulos
    for j in titulos:
        command=(f"whisper {j} --task transcribe --model {quality} --verbose False --output_format srt --output_dir {'subtitles'}")
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in process.stdout:print(line, end='')