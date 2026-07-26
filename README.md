# 📂 FileFlow

> A lightweight Windows desktop application that previews and organizes files intelligently.

![Version](https://img.shields.io/badge/version-v0.2.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows-0078D6)
![Language](https://img.shields.io/badge/Python-3.x-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Overview

FileFlow is an open-source Windows application that automatically organizes files into categorized folders based on their filenames and file types.

Unlike many basic file organizers, FileFlow lets you preview exactly where every file will go before any changes are made, giving you complete control over the organization process.

---

## 🚀 Features

- 📂 Automatic file organization
- 👀 Preview Mode before organizing
- 🗂 Smart categorization using filenames and extensions
- 🖥 Clean and lightweight desktop interface
- ⚡ Fast local processing
- 📊 Organization summary after every run
- 🔓 Open-source

---

## 🆕 What's New in v0.2.0

### Added

- 👀 Preview Mode
- 📋 File preview table
- 📂 Selected folder display
- 🚀 Confirmation before organizing files

### Improved

- Rebranded to **FileFlow**
- Larger and cleaner interface
- Better organization summary
- Improved stability and error handling

---

## 📷 How It Works

1. Launch FileFlow.
2. Click **Select Folder**.
3. Preview where each file will be moved.
4. Click **Organize Files**.
5. View the organization summary.

---

## 🧠 Smart Categories

FileFlow currently organizes files into:

- 📚 School
- 💻 Programming
- 🎵 Music
- 🎮 Games
- 🖼 Images
- 🎥 Videos
- 📄 Documents
- 📦 Others

---

## ⌨ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl + O | Select Folder |
| F5 | Refresh Preview |
| Esc | Exit |

---

## 🛠 Installation

### Option 1 (Recommended)

Download the latest release from the **Releases** section.

Extract the ZIP file and run:

```
FileFlow.exe
```

No installation required.

---

### Option 2

Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/FileFlow.git
```

Install Python 3 and run:

```bash
python FileFlow.py
```

---

## 📦 Building the Executable

Using PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=fileflow.ico FileFlow.py
```

The executable will be generated inside:

```
dist/
```

---

## 📁 Project Structure

```
FileFlow
│
├── FileFlow.py
├── LICENSE
├── README.md
├── .gitignore
├── fileflow.ico
└── dist/
```

---

## 🗺 Roadmap

### ✅ v0.1.0

- Initial public release

### ✅ v0.2.0

- Preview Mode
- Improved interface
- Better organization summary

### 🔜 Upcoming

- ↩ Undo last organization
- 📜 Organization history
- 🎨 Improved UI
- 🖱 Drag & Drop support
- ⚙ Custom categories
- 📂 Folder monitoring

---

## 🤝 Contributing

Contributions, bug reports and feature suggestions are always welcome.

If you'd like to improve FileFlow:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.

---

## 👨‍💻 Developer

Created by **Reyansh Prasad**

GitHub: https://github.com/YOUR_USERNAME

---

⭐ If you like FileFlow, consider starring the repository.
