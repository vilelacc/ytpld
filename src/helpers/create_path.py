from pathlib import Path    
from helpers.get_download_path import get_download_path
from helpers.validate_folder_name import validate_folder_name

def create_path(playlist_title: str) -> str:
    download_path = get_download_path()
    folder_name = validate_folder_name(playlist_title)
    path = Path(download_path, folder_name)
    path.mkdir(parents=True, exist_ok=True)
    return path