def validate_folder_name(name: str) -> str:
    """This function validates folder names by substituting invalid characters with dashes ('-')"""
    invalid_characters = r'\/:*?"<>|'
    for character in invalid_characters:
        name = name.replace(character, " - ")
    return name