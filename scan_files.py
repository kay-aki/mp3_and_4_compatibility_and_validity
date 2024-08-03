from pymediainfo import MediaInfo
from mutagen.mp3 import MP3
from mutagen import MutagenError

def is_mp3_valid(file_path):
    try:
        audio = MP3(file_path)
        return audio.info is not None
    except MutagenError:
        return False

def is_mp4_valid(file_path):
    try:
        media_info = MediaInfo.parse(file_path)
        return len(media_info.tracks) > 0
    except:
        return False

def is_file_path_valid(file_path):
    invalid_signs = ["'", "\"", ";", "--", "\\", "\0"]
    for c in invalid_signs:
        if (file_path.includes(c))
            return False
        if ord(c) in list(range(0, 32)) + [127]:
            return False
    return True
    

def clean_string(file_path):
    # Entferne Null-Bytes
    cleaned_string = file_path.replace('\0', '')

    # Entferne Steuerzeichen (ASCII 0-31) außer Newline und Carriage Return
    cleaned_string = re.sub(r'[\x00-\x1F\x7F]', '', cleaned_string)

    # Optional: Entferne spezifische problematische Zeichen
    cleaned_string = re.sub(r"[\'\";\\]", '', cleaned_string)
    cleaned_string = re.sub(r"--", ' ', cleaned_string)

    # Trim whitespace
    cleaned_string = cleaned_string.strip()

    return cleaned_string

def scan_dir(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            if not is_file_path_valid(file_path):
                cleaned_path = clean_string(file_path)
                print(f"Ungültiger Dateipfad: {file_path}")
                print(f"Besser wäre: {cleaned_path}")

            if file_name.lower().endswith('.mp3'):
                if not is_mp3_valid(file_path):
                    print(f"Ungültige MP3: {file_path}")

            elif file_name.lower().endswith('.mp4'):
                if not is_mp4_valid(file_path):
                    print(f"Ungültige MP4: {file_path}")

# Beispielaufruf
print("Verzeichnis: ")
scan_dir(input())
