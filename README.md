# YouTube playlist download script
![License](https://img.shields.io/github/license/vilelajs/youtube-playlist-downloader)
![Last Commit](https://img.shields.io/github/last-commit/vilelajs/youtube-playlist-downloader)
![Issues](https://img.shields.io/github/issues/vilelajs/youtube-playlist-downloader)
![Pull Requests](https://img.shields.io/github/issues-pr/vilelajs/youtube-playlist-downloader)
![Forks](https://img.shields.io/github/forks/vilelajs/youtube-playlist-downloader)
![Stars](https://img.shields.io/github/stars/vilelajs/youtube-playlist-downloader)

This Python script allows you to download all the videos in a YouTube playlist at once. It uses the ``pytubefix`` library to download videos.

> [!WARNING]
> This script is provided as-is, and the user assumes all responsibility for its usage. Make sure to comply with YouTube terms of service and respect the rights and privacy of others while using this script.

## Requirements
* Python 3.x installed on your system.
* Installing the pytube library. You can install it via pip using the following command:

```bash
pip install pytubefix
```

## How to use the script

1. Clone the repository: Clone the repository where the script is hosted to your local environment using the git clone command. For example:

```bash
git clone https://github.com/vilelajs/YouTubePlaylistDownloader.git
```

2. Navigate to directory: Use the terminal or command prompt to navigate to the project directory where the script is located.
3. Run the script: Run the Python script by typing the following command:

```bash
python app.py
```

4. Enter playlist link: The script will ask you to enter the link of the YouTube playlist you want to download. Copy and paste the playlist link and press Enter.
5. Download in progress: The script will begin downloading the playlist videos to your operating system's default downloads directory.
6. Track progress: You'll see a message indicating which video is currently downloading.
7. Check the download directory: After the download is complete, check the default download directory for your operating system. The videos will be saved in a folder with the name of the playlist.
