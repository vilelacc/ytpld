import os
from pytube import YouTube, Playlist
from pytube.exceptions import MaxRetriesExceeded
from pytube.cli import on_progress
from utils.functions import get_download_path, validate_folder_name

def download_playlist(playlist_url):
    full_path = get_download_path()  # os.getcwd()
    playlist = Playlist(playlist_url)
    path = os.path.join(full_path, validate_folder_name(playlist.title))

    if not os.path.isdir(path):
        os.mkdir(path)

    for url in playlist:
        try:
            video = YouTube(url, on_progress_callback=on_progress)
            stream = video.streams.get_highest_resolution()
            try:
                print(f"Downloading {video.title}")
                stream.download(output_path=path, skip_existing=True, max_retries=2)
            except MaxRetriesExceeded:
                print(f"Maximum number of retries exceeded for video: {video.title}")
        except Exception as e:
            print(f"An error occurred while downloading the video: {e}")
        finally:
            print()
            # os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    playlist_url = input("Enter the playlist link: ")
    download_playlist(playlist_url)
