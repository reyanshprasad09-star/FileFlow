import os
import sys
import shutil
import logging
import traceback
from collections import defaultdict
from pathlib import Path

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# ==========================================================
# FileFlow v1.0
# Smart File Organizer
# ==========================================================

APP_NAME = "FileFlow"
APP_VERSION = "1.0"

logging.basicConfig(
    filename="fileflow.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ----------------------------------------------------------
# Supported Extensions
# ----------------------------------------------------------

CATEGORY_EXTENSIONS = {

    "Images": {
        ".png", ".jpg", ".jpeg", ".bmp",
        ".gif", ".tiff", ".webp", ".ico",
        ".svg"
    },

    "Videos": {
        ".mp4", ".avi", ".mov",
        ".mkv", ".wmv", ".flv",
        ".webm"
    },

    "Music": {
        ".mp3", ".wav", ".aac",
        ".ogg", ".flac", ".m4a"
    },

    "Documents": {
        ".pdf", ".doc", ".docx",
        ".txt", ".rtf", ".odt",
        ".ppt", ".pptx",
        ".xls", ".xlsx",
        ".csv"
    },

    "Archives": {
        ".zip", ".rar",
        ".7z", ".tar",
        ".gz", ".iso"
    },

    "Programs": {
        ".exe", ".msi",
        ".apk", ".bat",
        ".cmd", ".jar"
    },

    "Code": {
        ".py", ".cpp", ".c",
        ".cs", ".java",
        ".js", ".ts",
        ".html", ".css",
        ".json", ".xml",
        ".sql", ".php",
        ".swift", ".kt",
        ".go", ".rs"
    }

}

# ----------------------------------------------------------
# Filename Keywords
# ----------------------------------------------------------

KEYWORDS = {

    "School": [
        "homework",
        "assignment",
        "math",
        "science",
        "biology",
        "chemistry",
        "physics",
        "history",
        "geography",
        "english",
        "computer",
        "project",
        "notes",
        "worksheet",
        "exam",
        "test",
        "class"
    ],

    "Finance": [
        "invoice",
        "receipt",
        "salary",
        "tax",
        "bank",
        "payment",
        "upi",
        "bill",
        "gst"
    ],

    "Screenshots": [
        "screenshot",
        "screen shot",
        "snip",
        "capture"
    ],

    "Downloads": [
        "download",
        "installer",
        "setup"
    ],

    "Design": [
        "logo",
        "poster",
        "banner",
        "mockup",
        "thumbnail",
        "icon"
    ]

}

# ----------------------------------------------------------
# Utility Functions
# ----------------------------------------------------------

def get_resource_path(relative_path: str) -> str:
    """
    Get absolute path to resource, works for dev and for PyInstaller.
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


def safe_filename(name: str) -> str:
    """
    Removes invalid filename characters.
    """
    invalid = '<>:"/\\|?*'

    for ch in invalid:
        name = name.replace(ch, "_")

    return name.strip()


def unique_destination(path: Path) -> Path:
    """
    Prevent overwriting.
    """
    if not path.exists():
        return path

    counter = 1

    while True:
        new_name = f"{path.stem} ({counter}){path.suffix}"
        candidate = path.with_name(new_name)

        if not candidate.exists():
            return candidate

        counter += 1


# ----------------------------------------------------------
# Smart Categorization
# ----------------------------------------------------------

def categorize_file(filepath: Path) -> str:
    """
    Decide the destination folder using both
    filename keywords and extension.
    """
    filename = filepath.name.lower()

    # Priority 1:
    # Keyword-based classification
    for category, words in KEYWORDS.items():
        for word in words:
            if word in filename:
                return category

    # Priority 2:
    # Extension-based classification
    extension = filepath.suffix.lower()

    for category, extensions in CATEGORY_EXTENSIONS.items():
        if extension in extensions:
            return category

    # Priority 3:
    # Empty extension
    if extension == "":
        return "No Extension"

    return "Others"


# ----------------------------------------------------------
# Main Application
# ----------------------------------------------------------

class FileFlow(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title(f"{APP_NAME} {APP_VERSION}")
        self.geometry("1100x700")
        self.minsize(900, 600)

        self.preview_data = []
        self.summary = defaultdict(int)
        self.selected_folder = None
        self.preview_completed = False

        try:
            icon_path = get_resource_path("fileflow.ico")
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)
        except Exception:
            pass

        self.create_styles()
        self.create_variables()

    # ------------------------------------------------------
    # Variables
    # ------------------------------------------------------

    def create_variables(self):
        self.folder_var = tk.StringVar(value="No folder selected")
        self.status_var = tk.StringVar(value="Ready")

    # ------------------------------------------------------
    # Styling
    # ------------------------------------------------------

    def create_styles(self):
        style = ttk.Style(self)

        try:
            style.theme_use("vista")
        except tk.TclError:
            try:
                style.theme_use("clam")
            except tk.TclError:
                pass

        self.configure(bg="#f3f3f3")

        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 22, "bold"),
            background="#f3f3f3"
        )

        style.configure(
            "Subtitle.TLabel",
            font=("Segoe UI", 10),
            background="#f3f3f3",
            foreground="#555555"
        )

        style.configure(
            "Status.TLabel",
            font=("Segoe UI", 9),
            background="#f3f3f3"
        )

        style.configure(
            "Summary.TLabelframe",
            font=("Segoe UI", 10, "bold")
        )

        style.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=26
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

        style.configure(
            "Accent.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=8
        )

        style.map(
            "Accent.TButton",
            background=[("active", "#0078D7")]
        )

        self.create_widgets()

    # ------------------------------------------------------
    # UI
    # ------------------------------------------------------

    def create_widgets(self):

        # ===========================
        # Header
        # ===========================
        header = ttk.Frame(self)
        header.pack(fill="x", padx=20, pady=15)

        ttk.Label(
            header,
            text="FileFlow",
            style="Title.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            header,
            text="Smart File Organizer",
            style="Subtitle.TLabel"
        ).pack(anchor="w")

        # ===========================
        # Toolbar
        # ===========================
        toolbar = ttk.Frame(self)
        toolbar.pack(fill="x", padx=20, pady=(0, 10))

        self.select_btn = ttk.Button(
            toolbar,
            text="📁 Select Folder",
            command=self.select_folder,
            style="Accent.TButton"
        )
        self.select_btn.pack(side="left")

        self.preview_btn = ttk.Button(
            toolbar,
            text="👀 Preview",
            command=self.preview_files,
            style="Accent.TButton"
        )
        self.preview_btn.pack(side="left", padx=6)

        self.organize_btn = ttk.Button(
            toolbar,
            text="🚀 Organize",
            command=self.organize_files,
            state="disabled",
            style="Accent.TButton"
        )
        self.organize_btn.pack(side="left")

        # ===========================
        # Selected Folder
        # ===========================
        folder_frame = ttk.Frame(self)
        folder_frame.pack(fill="x", padx=20, pady=(0, 10))

        ttk.Label(
            folder_frame,
            textvariable=self.folder_var,
            font=("Segoe UI", 10)
        ).pack(anchor="w")

        # ===========================
        # Main Area
        # ===========================
        main = ttk.Frame(self)
        main.pack(fill="both", expand=True, padx=20, pady=10)

        # Treeview
        tree_frame = ttk.Frame(main)
        tree_frame.pack(side="left", fill="both", expand=True)

        columns = ("Name", "Category", "Destination")

        self.tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        self.tree.heading("Name", text="Filename")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Destination", text="Destination Folder")

        self.tree.column("Name", width=350)
        self.tree.column("Category", width=150, anchor="center")
        self.tree.column("Destination", width=220, anchor="center")

        scrollbar = ttk.Scrollbar(
            tree_frame,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ===========================
        # Summary Panel
        # ===========================
        summary_frame = ttk.LabelFrame(
            main,
            text="Organization Summary",
            style="Summary.TLabelframe",
            width=250
        )
        summary_frame.pack(side="right", fill="y", padx=(12, 0))

        self.summary_text = tk.Text(
            summary_frame,
            width=28,
            height=25,
            relief="flat",
            font=("Consolas", 10),
            bg="#FAFAFA"
        )
        self.summary_text.pack(fill="both", expand=True, padx=8, pady=8)
        self.summary_text.configure(state="disabled")

        # ===========================
        # Status Bar
        # ===========================
        status = ttk.Label(
            self,
            textvariable=self.status_var,
            relief="sunken",
            anchor="w",
            style="Status.TLabel"
        )
        status.pack(side="bottom", fill="x")

    # ------------------------------------------------------
    # Folder Selection
    # ------------------------------------------------------

    def select_folder(self):
        folder = filedialog.askdirectory(title="Select Folder to Organize")

        if not folder:
            return

        self.selected_folder = Path(folder)
        self.folder_var.set(str(self.selected_folder))
        self.preview_completed = False
        self.organize_btn.config(state="disabled")
        self.tree.delete(*self.tree.get_children())
        self.summary.clear()
        self.update_summary()
        self.status_var.set(f"Selected folder: {self.selected_folder}")

    # ------------------------------------------------------
    # Preview Mode
    # ------------------------------------------------------

    def preview_files(self):
        if not self.selected_folder:
            messagebox.showwarning(APP_NAME, "Please select a folder first.")
            return

        self.tree.delete(*self.tree.get_children())
        self.summary.clear()
        self.preview_data.clear()

        files_found = 0

        try:
            for item in self.selected_folder.iterdir():
                if not item.is_file():
                    continue

                category = categorize_file(item)
                destination = self.selected_folder / category

                self.preview_data.append({
                    "source": item,
                    "category": category,
                    "destination": destination
                })

                self.summary[category] += 1

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        item.name,
                        category,
                        destination.name
                    )
                )

                files_found += 1

            self.update_summary()
            self.preview_completed = True
            self.organize_btn.config(state="normal")
            self.status_var.set(f"Preview complete • {files_found} files")

            if files_found == 0:
                messagebox.showinfo(APP_NAME, "No files found in the selected folder.")

        except Exception as e:
            logging.exception(e)
            messagebox.showerror(APP_NAME, f"Preview failed.\n\n{e}")

    # ------------------------------------------------------
    # Summary Panel
    # ------------------------------------------------------

    def update_summary(self):
        self.summary_text.configure(state="normal")
        self.summary_text.delete("1.0", tk.END)

        total = sum(self.summary.values())
        self.summary_text.insert(tk.END, f"Total Files : {total}\n\n")

        if total == 0:
            self.summary_text.insert(tk.END, "Nothing to preview.")
        else:
            for category in sorted(self.summary):
                count = self.summary[category]
                self.summary_text.insert(tk.END, f"{category:<18} {count}\n")

        self.summary_text.configure(state="disabled")

    # ------------------------------------------------------
    # Organize Files
    # ------------------------------------------------------

    def organize_files(self):
        if not self.preview_completed:
            messagebox.showwarning(APP_NAME, "Please run Preview before organizing.")
            return

        moved = 0
        skipped = 0
        failed = 0

        self.status_var.set("Organizing files...")
        self.update_idletasks()

        try:
            for item in self.preview_data:
                source = item["source"]
                destination_folder = item["destination"]

                try:
                    # Skip if file disappeared
                    if not source.exists():
                        skipped += 1
                        continue

                    # Create destination folder
                    destination_folder.mkdir(parents=True, exist_ok=True)

                    # Sanitize filename and construct path
                    clean_name = safe_filename(source.name)
                    destination = destination_folder / clean_name

                    # Prevent overwriting
                    destination = unique_destination(destination)

                    shutil.move(str(source), str(destination))
                    moved += 1

                except Exception as e:
                    failed += 1
                    logging.exception("Failed moving %s", source)

            self.status_var.set(f"Finished • {moved} moved")

            messagebox.showinfo(
                APP_NAME,
                (
                    "Organization Complete!\n\n"
                    f"Moved : {moved}\n"
                    f"Skipped : {skipped}\n"
                    f"Failed : {failed}"
                )
            )

            # Refresh Preview
            self.preview_completed = False
            self.organize_btn.config(state="disabled")
            self.preview_files()

        except Exception as e:
            logging.exception(e)
            traceback.print_exc()
            messagebox.showerror(APP_NAME, f"Unexpected error.\n\n{e}")

    # ------------------------------------------------------
    # Refresh Preview
    # ------------------------------------------------------

    def refresh_preview(self):
        if self.selected_folder:
            self.preview_files()

    # ------------------------------------------------------
    # Clear Preview
    # ------------------------------------------------------

    def clear_preview(self):
        self.tree.delete(*self.tree.get_children())
        self.summary.clear()
        self.preview_data.clear()
        self.preview_completed = False
        self.organize_btn.config(state="disabled")
        self.update_summary()
        self.status_var.set("Preview cleared")

    # ------------------------------------------------------
    # Utility
    # ------------------------------------------------------

    def selected_item(self):
        selection = self.tree.selection()
        if not selection:
            return None
        return self.tree.item(selection[0], "values")

    def preview_destination(self, event=None):
        item = self.selected_item()
        if item is None:
            return

        filename, category, destination = item

        messagebox.showinfo(
            "Destination Preview",
            (
                f"Filename:\n{filename}\n\n"
                f"Will be moved to:\n"
                f"{self.selected_folder / destination}"
            )
        )

    # ------------------------------------------------------
    # Context Menu
    # ------------------------------------------------------

    def create_context_menu(self):
        self.context_menu = tk.Menu(self, tearoff=False)
        self.context_menu.add_command(label="Copy Filename", command=self.copy_filename)

        self.tree.bind("<Button-3>", self.show_context_menu)
        self.tree.bind("<Double-1>", self.preview_destination)

    def show_context_menu(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.tk_popup(event.x_root, event.y_root)

    def copy_filename(self):
        item = self.selected_item()
        if item is None:
            return

        filename = item[0]
        self.clipboard_clear()
        self.clipboard_append(filename)
        self.status_var.set(f"Copied '{filename}'")

    # ------------------------------------------------------
    # Keyboard Shortcuts
    # ------------------------------------------------------

    def register_shortcuts(self):
        self.bind("<Control-o>", lambda e: self.select_folder())
        self.bind("<F5>", lambda e: self.preview_files())
        self.bind("<Escape>", lambda e: self.on_close())

    # ------------------------------------------------------
    # Window Closing
    # ------------------------------------------------------

    def on_close(self):
        if messagebox.askyesno(APP_NAME, "Exit FileFlow?"):
            self.destroy()

    # ------------------------------------------------------
    # Finish Initialization
    # ------------------------------------------------------

    def initialize(self):
        self.create_context_menu()
        self.register_shortcuts()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.status_var.set("Ready")

# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    try:
        app = FileFlow()
        app.initialize()
        app.mainloop()

    except Exception as e:
        logging.exception(e)
        traceback.print_exc()
        messagebox.showerror(APP_NAME, f"A fatal error occurred.\n\n{e}")
