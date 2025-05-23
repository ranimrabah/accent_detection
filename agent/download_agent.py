import os
import uuid
import yt_dlp

def get_unique_filename(output_dir, ext=".wav"):
    return os.path.join(output_dir, f"{uuid.uuid4().hex}{ext}")

def download_audio_as_wav(url: str) -> str:
    output_dir = "audio_outputs"
    os.makedirs(output_dir, exist_ok=True)
    output = get_unique_filename(output_dir, ".wav")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output.replace(".wav", ".%(ext)s"),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'postprocessor_args': [
            '-ac', '1',
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        'quiet': True,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url, download=True)
        return output
