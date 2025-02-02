import os
import json
import subprocess

# Configuration
COOKIES_FILE = "cookies.txt"  # Fichier de cookies
DOWNLOADED_FILE = "downloaded_videos.json"  # Fichier pour suivre les vidéos téléchargées

# Charger les vidéos déjà téléchargées
if os.path.exists(DOWNLOADED_FILE):
    with open(DOWNLOADED_FILE, "r") as f:
        downloaded_videos = json.load(f)
else:
    downloaded_videos = []

# Télécharger une vidéo avec yt-dlp (via subprocess)
def download_video(video_id, title):
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
        print(f"Téléchargé : {title}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du téléchargement de {title}: {e}")

# Fonction principale
def main():
    # Charger les vidéos à télécharger
    if os.path.exists("videos_to_download.json"):
        with open("videos_to_download.json", "r") as f:
            videos = json.load(f)

        for video in videos:
            video_id = video["video_id"]
            title = video["title"]

            # Vérifier si la vidéo a déjà été téléchargée
            if video_id in downloaded_videos:
                print(f"Déjà téléchargée : {title}")
                continue

            # Télécharger la vidéo
            try:
                download_video(video_id, title)
                downloaded_videos.append(video_id)

                # Sauvegarder l'état
                with open(DOWNLOADED_FILE, "w") as f:
                    json.dump(downloaded_videos, f)

                break  # Télécharger seulement une vidéo à chaque exécution
            except Exception as e:
                print(f"Erreur lors du téléchargement de {title}: {e}")
    else:
        print("Aucune vidéo à télécharger, le fichier 'videos_to_download.json' est manquant.")

if __name__ == "__main__":
    main()
