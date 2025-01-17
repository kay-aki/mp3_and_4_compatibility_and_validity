# Verzeichnis-Scanner für MP3- und MP4-Dateien

1. **Voraussetzungen**:
Dieses Projekt enthält ein Python-Skript, das ein Verzeichnis rekursiv durchsucht und die Validität von MP3- und MP4-Dateien überprüft sowie ungültige Zeichen in Dateipfaden bereinigt.
Stellen Sie sicher, dass Python 3 installiert ist. Sie können die Installation von Python 3 wie folgt überprüfen:

      python3 --version

3. **Installation von Python 3**:
Auf Windows

Laden Sie das Installationsprogramm von der offiziellen Python-Website herunter.
Führen Sie das Installationsprogramm aus und folgen Sie den Anweisungen. Stellen Sie sicher, dass Sie die Option "Add Python to PATH" aktivieren.

Auf macOS
Installieren Sie Python 3 über Homebrew:

    brew install python3

Falls Homebrew nicht installiert ist, folgen Sie den Anweisungen auf der Homebrew-Website.

Auf Linux (Debian/Ubuntu-basiert)
Aktualisieren Sie die Paketliste und installieren Sie Python 3:

    sudo apt update
    sudo apt install python3 python3-pip

3. **Installation der notwendigen Bibliotheken**
Installation der notwendigen Bibliotheken

Nach der Installation von Python 3 müssen Sie die erforderlichen Bibliotheken installieren. Dies kann mit pip erfolgen, dem Python-Paketmanager.

    pip install pymediainfo mutagen

4. **Verwendung**: 
Windows + R drücken und 'cmd' eingeben, sonst Kommandozeile oder Terminal über die Suche öffnen.
Eintippen:
      python3 pfad/zum/script/scan_files.py
Enter drücken
    
6. **Funktionen**: Kompatibilität der Dateinamen für Datenbanken und Korruptheit der MP3 und MP4 Dateien prüfen
7. **Autor und Lizenz**: Autor: ChatGPT und Annika Schomber, Lizenz ziehe License
