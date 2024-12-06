# Chess.com Desktop

A simple application that let's you play chess.com as a desktop app.

## Features

- Play chess on Chess.com.
- Discord Rich Presence integration

## Installation Instructions

### Step 1: Download the Setup

1. Go to the [Releases](https://github.com/your-username/your-repository/releases) page.
2. Download the latest release setup executable (`chess.com_setup.exe`).

## Build Instructions

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- [PySide6](https://pypi.org/project/PySide6/) (for the user interface and web engine)
- [PyInstaller](https://www.pyinstaller.org/) (for compiling the Python script)
- [pypresence](https://pypi.org/project/pypresence/) (for Discord Rich Presence integration)

### Step 1: Install Dependencies

Run the following command to install required Python libraries:
```bash
pip install PySide6 pypresence pyinstaller
```

### Step 2: Compile the Application

To compile the app into a standalone executable, run the following command:

```bash
pyinstaller --onefile --windowed --icon=icon.ico app.py
```

- `--onefile`: Creates a single executable file.
- `--windowed`: Suppresses the terminal window for GUI apps.
- `--icon=chess_icon.ico`: Specifies the icon for the app.

### Step 3: Find the Executable

After the build process completes, you will find the executable in the `dist/` folder inside your project directory.

## Disclaimer

This app simply embeds the Chess.com website in a web view. It is not officially affiliated with Chess.com.