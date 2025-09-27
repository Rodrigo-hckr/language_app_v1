import tkinter as tk
from tkinter import filedialog
from phrases.personal_lists import process_uploaded_file

def open_upload_window(user):
    window = tk.Toplevel()
    window.title("Subir lista personal")
    
    def upload_file():
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")])
        if path:
            phrases = process_uploaded_file(path)
            user.favorites.extend(phrases)
            tk.Label(window, text="lista cargada corectamente").pack()
            
    tk.Button(window, text="Seleccionar archivo", command=upload_file).pack(pady=10)