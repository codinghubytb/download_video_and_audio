# Téléchargement de Vidéos YouTube, Instagram, Tiktok, Snapchat, Reddit, Twitter etc... avec yt-dlp

Ce projet permet de télécharger des vidéos depuis Internet en utilisant `yt-dlp`.  

## Prérequis

Avant de pouvoir exécuter les scripts, vous devez installer les dépendances suivantes :

- **yt-dlp** : Un outil en ligne de commande pour télécharger des vidéos depuis YouTube, Instagram et d'autres plateformes.
- **Python 3** : Le script est écrit en Python 3 et utilise `argparse` pour gérer les arguments de ligne de commande.

### Installation des dépendances

1. Clonez ce dépôt ou téléchargez le code source sur votre machine.
2. Installez `yt-dlp` avec `pip` :

    ```bash
    pip install yt-dlp
    ```

## Utilisation

### 📌 Télécharger une vidéo YouTube

Utilisez `youtube.py` en fournissant **l'ID** de la vidéo :

```bash
python youtube.py <video_id>
````

### 📌 Télécharger une vidéo Instagram

Utilisez `instagram.py` en fournissant **l'URL complète** de la vidéo :

```bash
python instagram.py <url_de_la_video_instagram>
````
