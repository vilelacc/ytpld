from pytubefix import YouTube, Playlist

from helpers.create_path import create_path
from config.log import logging

def download_playlist(playlist_url: str) -> None:
    try:
        playlist = Playlist(playlist_url)
        path = create_path(playlist.title)
        for url in playlist:
            try:
                logging.info(f"Attempting to download video from URL: {url}")
                video = YouTube(url)
                stream = video.streams.get_highest_resolution()
                stream.download(output_path=path, max_retries=2)
                logging.info(f"Downloaded: {video.title}")
            except Exception as e:
                logging.error(f"An error occurred: {e}")
    except Exception as e:
        logging.error("The playlist url is not valid")