import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from collections import defaultdict

# ==========================================
# FileFlow v0.2.0
# Preview Mode Update
# ==========================================

TOPIC_KEYWORDS = {
    "School": [
        "math", "science", "history", "physics",
        "chemistry", "biology", "assignment", "project"
    ],

    "Programming": [
        "python", "java", "code",
        "javascript", "cpp", "html", "css"
    ],

    "Music": [
        "song", "album", "phonk",
        "music", "track"
    ],

    "Games": [
        "game", "minecraft",
        "roblox", "valorant", "steam"
    ],

    "Images": [
        "photo", "image",
        "screenshot", "wallpaper"
    ],

    "Videos": [
        "video", "movie",
        "clip", "episode"
    ],

    "Documents": [
        "report", "notes",
        "invoice", "receipt",
        "resume"
    ]
}

EXTENSION_FALLBACK = {

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",

    ".gif": "Images",
    ".bmp": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",

    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",

    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".xlsx": "Documents"
}

selected_folder = ""
preview_files = []


def classify(filename):
    """
    Returns category based on filename.
    """

    lower = filename.lower()

    for category, keywords in TOPIC_KEYWORDS.items():

        for keyword in keywords:

            if keyword in lower:
                return category

    extension = os.path.splitext(lower)[1]

    return EXTENSION_FALLBACK.get(
        extension,
        "Others"
    )


def clear_preview():

    preview_tree.delete(*preview_tree.get_children())

    preview_files.clear()

    organize_button.config(
        state="disabled"
    )


def generate_preview(folder):

    clear_preview()

    total = 0

    for item in sorted(os.listdir(folder)):

        full_path = os.path.join(folder, item)

        if os.path.isfile(full_path):

            category = classify(item)

            preview_files.append(
                (item, category)
            )

            preview_tree.insert(
                "",
                tk.END,
                values=(
                    item,
                    category
                )
            )

            total += 1

    status_label.config(
        text=f"Ready to organize {total} files."
    )

    if total > 0:

        organize_button.config(
            state="normal"
        )


def choose_folder():

    global selected_folder

    folder = filedialog.askdirectory()

    if not folder:
        return

    selected_folder = folder

    folder_label.config(
        text=f"📂 {folder}"
    )

    def organize_files():

    if not selected_folder:
        return

    moved = defaultdict(int)

    failed = []

    total = 0

    for filename, category in preview_files:

        source = os.path.join(
            selected_folder,
            filename
        )

        destination_folder = os.path.join(
            selected_folder,
            category
        )

        os.makedirs(
            destination_folder,
            exist_ok=True
        )

        destination = os.path.join(
            destination_folder,
            filename
        )

        try:

            shutil.move(
                source,
                destination
            )

            moved[category] += 1
            total += 1

        except Exception as error:

            failed.append(
                (
                    filename,
                    str(error)
                )
            )

    clear_preview()

    folder_label.config(
        text="No folder selected."
    )

    summary = []

    summary.append(
        "Organization Complete!\n"
    )

    for category in sorted(moved):

        summary.append(
            f"{category}: {moved[category]}"
        )

    summary.append("")
    summary.append(
        f"Total Files Organized: {total}"
    )

    if failed:

        summary.append("")
        summary.append(
            f"Failed Files: {len(failed)}"
        )

    messagebox.showinfo(
        "FileFlow",
        "\n".join(summary)
    )

    status_label.config(
        text="Ready"
    )


def exit_app():

    root.destroy()


def about():

    messagebox.showinfo(
        "About FileFlow",
        "FileFlow v0.2.0\n\n"
        "Organize files by understanding\n"
        "their filenames before moving them.\n\n"
        "© 2026 Reyansh Prasad"
    )

    # =====================================================
# MAIN WINDOW
# =====================================================

root = tk.Tk()

root.title("FileFlow")
root.geometry("760x520")
root.minsize(760, 520)

style = ttk.Style()

try:
    style.theme_use("vista")
except:
    pass

# -----------------------------------------------------

title = ttk.Label(
    root,
    text="FileFlow",
    font=("Segoe UI", 24, "bold")
)

title.pack(pady=(18, 0))

subtitle = ttk.Label(
    root,
    text="Preview files before organizing them",
    font=("Segoe UI", 10)
)

subtitle.pack(pady=(0, 18))

# -----------------------------------------------------

top_frame = ttk.Frame(root)

top_frame.pack(
    fill="x",
    padx=20
)

select_button = ttk.Button(
    top_frame,
    text="📂 Select Folder",
    command=choose_folder
)

select_button.pack(
    side="left"
)

organize_button = ttk.Button(
    top_frame,
    text="🚀 Organize Files",
    command=organize_files,
    state="disabled"
)

organize_button.pack(
    side="left",
    padx=10
)

about_button = ttk.Button(
    top_frame,
    text="About",
    command=about
)

about_button.pack(
    side="right"
)

# -----------------------------------------------------

folder_label = ttk.Label(
    root,
    text="No folder selected.",
    font=("Segoe UI", 10)
)

folder_label.pack(
    anchor="w",
    padx=20,
    pady=(12, 5)
)

# =====================================================
# PREVIEW TABLE
# =====================================================

table_frame = ttk.Frame(root)

table_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=5
)

columns = (
    "filename",
    "category"
)

preview_tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

preview_tree.heading(
    "filename",
    text="File"
)

preview_tree.heading(
    "category",
    text="Destination Folder"
)

preview_tree.column(
    "filename",
    width=470,
    anchor="w"
)

preview_tree.column(
    "category",
    width=220,
    anchor="center"
)

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=preview_tree.yview
)

preview_tree.configure(
    yscrollcommand=scrollbar.set
)

preview_tree.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)

# =====================================================
# STATUS BAR
# =====================================================

status_label = ttk.Label(
    root,
    text="Ready",
    relief="sunken",
    anchor="w"
)

status_label.pack(
    fill="x",
    side="bottom"
)

# =====================================================
# KEYBOARD SHORTCUTS
# =====================================================

def refresh_preview(event=None):
    """
    Regenerate the preview for the currently selected folder.
    """
    if selected_folder:
        generate_preview(selected_folder)


root.bind("<Control-o>", lambda event: choose_folder())
root.bind("<F5>", refresh_preview)
root.bind("<Escape>", lambda event: exit_app())

# =====================================================
# RIGHT CLICK MENU (Preview Table)
# =====================================================

menu = tk.Menu(root, tearoff=0)


def copy_filename():
    selected = preview_tree.selection()

    if not selected:
        return

    filename = preview_tree.item(
        selected[0],
        "values"
    )[0]

    root.clipboard_clear()
    root.clipboard_append(filename)


menu.add_command(
    label="Copy File Name",
    command=copy_filename
)


def show_context_menu(event):

    row = preview_tree.identify_row(event.y)

    if row:

        preview_tree.selection_set(row)

        menu.tk_popup(
            event.x_root,
            event.y_root
        )


preview_tree.bind(
    "<Button-3>",
    show_context_menu
)

# =====================================================
# DOUBLE CLICK
# =====================================================

def show_category(event):

    selected = preview_tree.selection()

    if not selected:
        return

    values = preview_tree.item(
        selected[0],
        "values"
    )

    messagebox.showinfo(
        "Preview",
        f"{values[0]}\n\nWill be moved to:\n{values[1]}"
    )


preview_tree.bind(
    "<Double-1>",
    show_category
)

# =====================================================
# STARTUP MESSAGE
# =====================================================

status_label.config(
    text="Welcome to FileFlow v0.2.0"
)

root.mainloop()
    generate_preview(folder)
