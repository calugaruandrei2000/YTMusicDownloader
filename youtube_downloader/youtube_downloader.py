import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_youtube_video(url, output_path):
    """
    Descarcă audio de pe YouTube și îl salvează într-un folder specificat.
    """
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': r'C:\Users\georg\Downloads\%(title)s.%(ext)s',
    'postprocessors': [],
}





    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        print(f"Eroare la descărcare: {e}")
        return False

def on_download_click():
    """
    Funcția care este apelată atunci când se apasă pe butonul de descărcare.
    """
    url = entry_url.get()  # Preia URL-ul introdus în câmpul text
    if url.strip() == "":  # Verifică dacă câmpul URL este gol
        messagebox.showerror("Eroare", "Te rog introdu un URL valid.")
        return

    # Definirea locației de salvare (poți modifica acest lucru)
    output_path = "./downloads/"

    # Descarcă melodia
    success = download_youtube_video(url, output_path)

    if success:
        messagebox.showinfo("Succes", "Melodia a fost descărcată cu succes!")
    else:
        messagebox.showerror("Eroare", "A apărut o problemă la descărcarea melodiei.")

# Creare fereastră principală
root = tk.Tk()
root.title("Descărcător YouTube")

# Setează dimensiunea ferestrei
root.geometry("400x200")

# Etichetă
label = tk.Label(root, text="Introdu URL-ul YouTube pentru descărcare:")
label.pack(pady=10)

# Câmp de text pentru URL
entry_url = tk.Entry(root, width=40)
entry_url.pack(pady=5)

# Buton pentru descărcare
download_button = tk.Button(root, text="Descarcă MP3", command=on_download_click)
download_button.pack(pady=10)

# Rulează aplicația
root.mainloop()
