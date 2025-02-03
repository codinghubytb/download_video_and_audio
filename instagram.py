import yt_dlp
import argparse

def download_instagram_video(url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Télécharge une vidéo Instagram.")
    parser.add_argument("url", help="URL de la vidéo Instagram")
    args = parser.parse_args()

    download_instagram_video(args.url)
    print("✅ Téléchargement terminé !")
