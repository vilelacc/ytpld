from service.download import download_playlist

if __name__ == "__main__":
    playlist_url = input(r"Enter the playlist link: ")
    download_playlist(playlist_url)