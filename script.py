import yt_dlp
import argparse
import os

def download_video(url, titre, extension, cookies_file=None):
    output_directory = ""
    os.makedirs(output_directory, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(output_directory, f"{titre}.%(ext)s"),
        'format': 'bestvideo+bestaudio/best' if extension == "video" else 'bestaudio/best',
    }

    if cookies_file:
        ydl_opts['cookiefile'] = cookies_file

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Video")
    parser.add_argument("url", help="URL")
    parser.add_argument("title", help="Title (without extension)")
    parser.add_argument("extension", choices=["video", "audio"], help="Extension du fichier (video ou audio)")
    parser.add_argument("cookies", help="Chemin vers le fichier de cookies", default=None)
    
    
    args = parser.parse_args()

    download_video(args.url, args.title, args.extension, args.cookies)
    print(f"Download Finished : {args.extension.upper()} !")
