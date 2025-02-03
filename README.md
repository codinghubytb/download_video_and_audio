# Téléchargement de Vidéos YouTube avec yt-dlp

Ce projet permet de télécharger une vidéo YouTube en utilisant l'ID de la vidéo, via l'outil `yt-dlp`. Vous pouvez spécifier l'ID de la vidéo à télécharger en paramètre lors de l'exécution du script.

## Prérequis

Avant de pouvoir exécuter le script, vous devez avoir installé les dépendances suivantes :

- **yt-dlp** : Un outil en ligne de commande pour télécharger des vidéos depuis YouTube et d'autres sites.
- **Python 3** : Le script est écrit en Python 3 et utilise `argparse` pour gérer les arguments de ligne de commande.

### Installation des dépendances

1. Clonez ce dépôt ou téléchargez le code source sur votre machine.
2. Installez les dépendances nécessaires en utilisant `pip` :

    ```bash
    pip install yt-dlp
    ```

## Configuration

1. **Cookies** : Le fichier `cookies.txt` doit être présent dans le répertoire où vous exécutez le script. Vous pouvez obtenir ce fichier en exportant vos cookies de votre navigateur.
2. **Fichier de suivi des vidéos téléchargées** : Le fichier `downloaded_videos.json` est utilisé pour suivre les vidéos déjà téléchargées. Il n'est pas nécessaire de le créer manuellement ; il sera créé automatiquement par le script s'il n'existe pas.

## Utilisation

### Exécution du script

Pour télécharger une vidéo en passant l'ID de la vidéo YouTube comme argument, exécutez la commande suivante :

```bash
python download_video.py <video_id>
