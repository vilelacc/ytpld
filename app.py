import os
from pytube import YouTube, Playlist
from pytube.cli import on_progress
from utils.functions import get_download_path, validate_folder_name

full_path = get_download_path() #os.getcwd()
playlist_url = input("Enter the playlist link: ")
playlist = Playlist(playlist_url)
path = os.path.join(full_path, validate_folder_name(playlist.title))

if not os.path.isdir(path):
    os.mkdir(path)

for url in playlist:
    try:
        video = YouTube(url, on_progress_callback=on_progress)
        file_name = f"{video.title}.mp4" 
        
        print(f"Downloading {video.title}")
        # check if the file already exists before downloading again
        video_path = os.path.join(path, file_name)

        if os.path.isfile(video_path):
            print("Video already exists. Skipping...")
            continue

        stream = video.streams.get_highest_resolution()
        stream.download(output_path=path)
        
        os.system("cls" if os.name == "nt" else "clear")

    except Exception as e:
        print(f"Am error occurred while downloading the video: {e}")
