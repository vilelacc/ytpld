import os

from pytubefix import YouTube, Playlist
from pytubefix.exceptions import VideoUnavailable, RegexMatchError

from helpers.functions import get_download_path, validate_folder_name


def download_playlist(playlist_url: str) -> None:
    full_path = get_download_path()  # os.getcwd()
    playlist = Playlist(playlist_url)
    path = os.path.join(full_path, validate_folder_name(playlist.title))

    if not os.path.isdir(path):
        os.mkdir(path)

    for url in playlist:
        try:
            print(f"Attempting to download video from URL: {url}")
            # Create a YouTube object
            video = YouTube(url)
            # Download the video to the specified output path
            stream = video.streams.get_highest_resolution()
            stream.download(output_path=path, skip_existing=True, max_retries=2)
            print(f"Downloaded: {video.title}")
        except RegexMatchError:
            print("The URL is invalid. Please enter a valid YouTube URL.")
        except VideoUnavailable:
            print("The video is unavailable. Please enter a valid YouTube URL.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    playlist_url = input(r"Enter the playlist link: ")
    download_playlist(playlist_url)