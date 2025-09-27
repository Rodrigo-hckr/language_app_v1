import tkinter as tk
from tkinter import messagebox, filedialog
from phrases.loader import load_phrases
from audio.tts import speak 
from auth.user import User
from plans.access import get_plan_features
from ui.upload_window import open_upload_window

def launch_app():
    root = tk.Tk()
    root.title("LanguageApp")
    
    tk.Label(root, text="Nombre de usuario: ").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()
    
    tk.Label(root, text="Selecciona tu plan:").pack()
    plan_var = tk.Entry(root)
    username_entry.pack()
    
    def start_session():
        username = username_entry.get()
        plan = plan_var.get()
        user = User(username, plan)
        features = get_plan_features(plan)
        phrases = load_phrases(features["access"])
        
        phrases_window = tk.Toplevel(root)
        phrases_window.title("Frases")
        
        for item in phrases:
            frame = tk.Frame(phrases_window)
            frame.pack(pady=5)
            tk.Label(frame, text=f"{item['original']} -> {item['translation']}").pack(side="left")
            
            tk.Button(frame, text="▶️", command=lambda i=item: speak(i['original'], i['translation'])).pack(side="left")
            tk.Button(frame, text="⭐", command=lambda i=item: user.add_favorite(i)).pack(side="left")
            
        if plan in ["Practice", "Polyglot"]:
            tk.Button(phrases_window, text="Subir lista personal", command=lambda: open_upload_window(user)).pack(pady=10)
            
    tk.Button(root, text="Iniciar", command=start_session).pack(pady=10)
    root.mainloop()
            