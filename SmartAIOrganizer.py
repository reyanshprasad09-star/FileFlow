
import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from collections import defaultdict

TOPIC_KEYWORDS = {
    "School": ["math", "science", "history", "physics", "chemistry", "biology", "assignment", "project"],
    "Programming": ["python", "java", "code", "javascript", "cpp", "html", "css"],
    "Music": ["song", "album", "phonk", "music", "track"],
    "Games": ["game", "minecraft", "roblox", "valorant", "steam"],
    "Images": ["photo", "image", "screenshot", "wallpaper"],
    "Videos": ["video", "movie", "clip", "episode"],
    "Documents": ["report", "notes", "invoice", "receipt", "resume"],
}

EXTENSION_FALLBACK = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".mp4": "Videos", ".mkv": "Videos",
    ".mp3": "Music", ".wav": "Music",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents",
}

def classify(filename):
    name = filename.lower()
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(word in name for word in keywords):
            return topic
    return EXTENSION_FALLBACK.get(os.path.splitext(name)[1], "Others")

def organize(folder):
    moved = defaultdict(int)
    for item in os.listdir(folder):
        path = os.path.join(folder, item)
        if os.path.isfile(path):
            category = classify(item)
            dest = os.path.join(folder, category)
            os.makedirs(dest, exist_ok=True)
            try:
                shutil.move(path, os.path.join(dest, item))
                moved[category] += 1
            except:
                pass

    summary = "\n".join(f"{k}: {v}" for k, v in moved.items()) or "No files moved."
    messagebox.showinfo("Completed", summary)

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        organize(folder)

root = tk.Tk()
root.title("Smart AI File Organizer")
root.geometry("500x300")

ttk.Label(root, text="Smart AI File Organizer", font=("Segoe UI", 18)).pack(pady=20)
ttk.Label(root, text="Organize files by understanding filename topics").pack()

ttk.Button(root, text="Select Folder", command=choose_folder).pack(pady=30)

root.mainloop()
