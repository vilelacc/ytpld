import os
from pytube import YouTube, Playlist
from pytube.cli import on_progress


def validate_folder_name(name):
    invalid_characters = r'\/:*?"<>|'
    for character in invalid_characters:
        name = name.replace(character, ' - ')
    return name


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


full_path = get_download_path() #os.getcwd()
playlist_url = input("Enter the playlist link: ")
playlist = Playlist(playlist_url)
path = os.path.join(full_path, validate_folder_name(playlist.title))

if not os.path.isdir(path):
    os.mkdir(path)

for url in playlist:
    try:
        video = YouTube(url, on_progress_callback=on_progress)
        print(f"Downloading {video.title}")

        # check if the file already exists before downloading again
        video_path = os.path.join(path, f"{video.title}.mp4")

        if os.path.isfile(video_path):
            print("Video already exists. Skipping...")
            continue

        stream = video.streams.get_highest_resolution()
        stream.download(output_path=path)
        cls()

    except Exception as e:
        print(f"Am error occurred while downloading the video: {e}")
