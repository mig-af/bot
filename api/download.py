from pytubefix import YouTube
from pytubefix.cli import on_progress
import io


def verificar_link(url:str):
    try:
        YouTube(url).title
        return True
    except:
        return False

def descarga(url:str):
    
    yt = YouTube(url)
    
    try:
        music = yt.streams.get_audio_only()
        buffer = io.BytesIO()
        music.stream_to_buffer(buffer)
        buffer.seek(0)
        return (buffer, yt.title)
    except Exception as erro:
        return (str(erro), "error")

#print(descarga("https://youtu.be/6cucosmPj-A?si=zEOuk_ezjmvEiwF8"))
