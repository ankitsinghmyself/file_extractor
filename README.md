# File Extractor Application
Download The Application 
## Overview
The File Extractor is a Python application that allows users to extract specific file types from a source folder to a destination folder. Users can select multiple file types, and the application provides an option to delete the files from the source folder after extraction.

## Features
- Select source and destination folders using a graphical interface.
- Choose from various file types to extract: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.mp4`, `.mov`, `.heic`.
- Option to delete source files after moving them to the destination.
- Progress bar indicating the status of the extraction process.
- User-friendly interface built with Tkinter.

## Requirements
- Python 3.x
- Tkinter (usually included with Python installations)
- PyInstaller (for creating standalone executables)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/ankitsinghmyself/file_extractor
   cd file_extractor
   ```

2. Install the required packages (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python file_extractor.py
   ```

## Creating an Executable
To create a standalone executable for the application, use PyInstaller:
```bash
pyinstaller --onefile --windowed --icon="fileExtractor.ico" file_extractor.py
```


## Download the Application
You can download the application [here](https://github.com/ankitsinghmyself/file_extractor/raw/refs/heads/master/FileExtractorInstaller.exe).

## How to Use
1. Launch the application.
2. Select the source folder containing the files you want to extract.
3. Select the destination folder where the files should be moved.
4. Choose the file types you want to extract from the list.
5. (Optional) Check the box to delete files from the source after extraction.
6. Click the "Start Extraction" button to begin the process.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Tkinter for the graphical user interface
- PyInstaller for creating standalone executables
