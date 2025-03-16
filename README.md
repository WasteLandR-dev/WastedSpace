### README for Wasted Space

#### Overview
Wasted Space is a lightweight Python tool that scans directories, calculates file and folder sizes, and displays them in a tree-like structure. It offers two versions: a console interface for terminal users and a GUI interface with a modern design, built using Python's standard library.

#### Features
- **Directory Scanning**: Computes sizes of files and folders in a specified directory.
- **Tree Display**: Shows results in a hierarchical format.
- **Console Version**: Simple command-line interface.
- **GUI Version**: Modern, dark-themed interface with responsive layout using Tkinter.

#### Installation
1. Ensure **Python 3.4 or later** is installed ([download here](https://www.python.org/downloads/)).
2. Download:
   - `builder.py` (console version).
   - `gui.py` (GUI version).
3. On Linux, install `python3-tk` if needed for GUI:
   ```bash
   sudo apt-get install python3-tk
   ```

#### Usage
- **Console Version**:
  ```bash
  `python3 builder.py /path/to/directory`
  ```
  Displays a tree of sizes in the terminal.

- **GUI Version**:
  ```bash
  `python3 gui.py`
  ```
  Opens a window; enter or browse a directory, then click "Scan" to view results.

#### Dependencies
- **Python 3.4+**: Core requirement.
- **Tkinter**: Included with Python (install `python3-tk` on Linux if missing).

#### Notes
- Ensure read permissions for scanned directories.
- The GUI may freeze briefly when scanning large directories.

This README provides all you need to get started with the Wasted Space!