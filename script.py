import os
import subprocess
import argparse

# Configuration
COOKIES_FILE = "cookies.txt"  # Fichier de cookies
DOWNLOADED_FILE = "downloaded_videos.json"  # Fichier pour suivre les vidéos téléchargées

# Télécharger une vidéo avec yt-dlp (via subprocess)
def download_video(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    command = [
        "yt-dlp",
        "--cookies", COOKIES_FILE,
        "--format", "bestaudio[ext=m4a]+bestvideo[ext=mp4]",
        "--merge-output-format", "mp4",
        "--output", "%(title)s.%(ext)s",
        url
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Téléchargé : {video_id}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du téléchargement de la vidéo {video_id}: {e}")

# Fonction principale
def main(video_id):
    # Télécharger la vidéo en passant l'ID
    download_video(video_id)

if __name__ == "__main__":
    # Ajouter l'argument pour passer l'ID de la vidéo
    parser = argparse.ArgumentParser(description="Télécharger une vidéo YouTube en utilisant yt-dlp.")
    parser.add_argument("video_id", type=str, help="ID de la vidéo YouTube à télécharger.")
    args = parser.parse_args()

    # Appeler la fonction principale avec l'ID de la vidéo fourni
    main(video_id=args.video_id)
