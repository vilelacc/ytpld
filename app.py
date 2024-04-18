import os
from pytube import YouTube, Playlist


def validate_folder_name(name):
    invalid_characters = r'\/:*?"<>|'
    for character in invalid_characters:
        name = name.replace(character, ' - ')
    return name

full_path = os.getcwd()
playlist_url = input("Enter the playlist link: ")
playlist = Playlist(playlist_url)
path = os.path.join(full_path, validate_folder_name(playlist.title))

if not os.path.isdir(path):
    os.mkdir(path)

for url in playlist:
    try:
        video = YouTube(url)
        print(f"Downloading {video.title}")

        # check if the file already exists before downloading again
        video_path = os.path.join(path, f"{video.title}.mp4")

        if os.path.isfile(video_path):
            print("Video already exists. Skipping...")
            continue

        stream = video.streams.get_highest_resolution()
        stream.download(output_path=path)
        print("Download completed.")

    except Exception as e:
        print(f"Am error occurred while downloading the video: {e}")
