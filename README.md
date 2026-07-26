# FileFlow

A lightweight Windows desktop application that previews and organizes files intelligently.

![Version](https://img.shields.io/badge/version-v0.2.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows-0078D6)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Overview

FileFlow is an open-source Windows application that automatically organizes files into categorized folders based on filenames and file extensions.

Before moving any files, FileFlow generates a preview so you can see exactly where every file will be placed. This makes organizing safer, clearer, and easier.

---

## Features

- Preview Mode before organizing files
- Automatic file organization
- Smart categorization using filenames and file extensions
- Clean and lightweight desktop interface
- Fast local processing
- Organization summary after every run
- Open-source

---

## What's New in v0.2.0

### Added

- Preview Mode
- File preview table
- Selected folder display
- Confirmation before organizing files

### Improved

- Rebranded to FileFlow
- Larger and cleaner interface
- Improved organization summary
- Better stability and error handling

---

## How It Works

1. Launch FileFlow.
2. Click **Select Folder**.
3. Preview where each file will be moved.
4. Click **Organize Files**.
5. View the organization summary.

---

## Categories

FileFlow currently organizes files into:

- School
- Programming
- Music
- Games
- Images
- Videos
- Documents
- Others

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl + O | Select Folder |
| F5 | Refresh Preview |
| Esc | Exit |

---

## Installation

### Option 1 — Download Release

Download the latest release from the **Releases** page.

Extract the ZIP archive and run:

```text
FileFlow.exe
```

No installation is required.

---

### Option 2 — Run from Source

Clone the repository:

```bash
git clone https://github.com/reyanshprasad09-star/FileFlow.git
```

Run the application:

```bash
python FileFlow.py
```

---

## Building from Source

Build the executable using PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=fileflow.ico FileFlow.py
```

The executable will be created in:

```text
dist/
```

---

## Project Structure

```text
FileFlow/
│
├── FileFlow.py
├── LICENSE
├── README.md
├── CHANGELOG.md
├── .gitignore
├── fileflow.ico
└── dist/
```

---

## Roadmap

### ✅ v0.1.0
- Initial public release

### ✅ v0.2.0
- Preview Mode
- Improved interface
- Better organization summary

### 🔜 Planned

- Undo last organization
- Organization history
- Drag and Drop support
- Improved interface
- Custom categories
- Folder monitoring
- Performance improvements

---

## Contributing

Contributions, bug reports and feature requests are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## Developer

**Reyansh Prasad**

GitHub: https://github.com/reyanshprasad09-star

Repository: https://github.com/reyanshprasad09-star/FileFlow

---

If you find FileFlow useful, consider giving the repository a ⭐.
