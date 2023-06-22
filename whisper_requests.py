import subprocess
from youtube_downloader import titulos
def run_whisper(quality,path):
    global titulos
    for j in titulos:
        command=(f"whisper {'/content/audios/'+j} --task transcribe --model {quality} --verbose False --output_format srt --output_dir {path}")
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in process.stdout:print(line, end='')