# FileFlow 📂

**Organize your files effortlessly.**

FileFlow is a lightweight Windows desktop application that helps you organize cluttered folders in just a few clicks. It automatically sorts files into categorized folders based on their names and file types.

> ⚠️ **FileFlow v0.1.0 is an early release.** More features and improvements are planned for future updates.

## Features

* 📂 Select any folder to organize
* 🏷️ Automatically categorize files using keywords and file extensions
* 📁 Create category folders automatically
* ⚡ Fast and easy-to-use interface
* 🖥️ Standalone Windows executable

## Current Categories

* Documents
* Images
* Videos
* Music
* Programming
* School
* Games
* Others

## Installation

### Option 1: Download the executable

1. Go to the **Releases** section of this repository.
2. Download the latest release ZIP file.
3. Extract the ZIP file.
4. Run `FileFlow.exe`.

### Option 2: Run from source

1. Ensure Python 3.14 or later is installed.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run:

```bash
python FileFlow.py
```

## Building the Executable

If you want to build the application yourself:

```bash
python -m PyInstaller --onefile --windowed FileFlow.py
```

The generated executable will be located in the `dist` folder.

## Disclaimer

FileFlow moves files within the selected folder. Although the application is designed to operate safely, it is recommended to back up important files before performing large-scale organization tasks.

## License

This project is licensed under the MIT License.
