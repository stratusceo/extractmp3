#!/usr/bin/env python3
import sys
import moviepy.editor as mp
from tqdm import tqdm

def extract_audio(video_path):
    try:
        video = mp.VideoFileClip(video_path)
        audio = video.audio
        audio_path = video_path.rsplit('.', 1)[0] + '.mp3'
        audio.write_audiofile(audio_path, logger='bar')
        audio.close()
        video.close()
        print(f"Audio extrait avec succès et enregistré sous : {audio_path}")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract_mp3 <path_to_video>")
        sys.exit(1)
    extract_audio(sys.argv[1])
