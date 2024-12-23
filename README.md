# YouTube Downloader

Acest proiect permite descărcarea fișierelor audio de pe YouTube în format MP3 printr-o interfață simplă. 

## Caracteristici
- Introducerea URL-ului videoclipului YouTube în interfață.
- Descărcarea automata a fișierului audio în formatul dorit.
- Salvarea fișierului audio în folderul specificat.

## Cerințe de sistem
- Python 3.7 sau o versiune mai recentă
- Biblioteci necesare:
  - `yt-dlp`
  - `tkinter`
  - `os`

## Instalare
1. Clonează acest repository:
   ```bash
   git clone https://github.com/utilizator/youtube-downloader.git
   ```
2. Navighează în folderul proiectului:
   ```bash
   cd youtube-downloader
   ```
3. Instalează biblioteca `yt-dlp`:
   ```bash
   pip install yt-dlp
   ```

## Utilizare
1. Rulează scriptul principal:
   ```bash
   python youtube_downloader.py
   ```
2. Introdu URL-ul videoclipului YouTube în caseta de text din interfață.
3. Apasă butonul "Download" pentru a descărca melodia.
4. Fișierul audio descărcat va fi salvat în folderul `downloads` situat în directorul proiectului.

## Personalizare
Dacă dorești să modifici locația unde sunt salvate fișierele descărcate:
1. Deschide fișierul `youtube_downloader.py`.
2. Modifică variabila `output_path` pentru a indica folderul dorit:
   ```python
   output_path = r'C:\calea\catre\folderul\tau\%(title)s.%(ext)s'
   ```
