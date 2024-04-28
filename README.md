# ExtractMP3

## Overview
The `extractmp3.py` script is a convenient tool for extracting audio from MP4 video files. It saves the audio in MP3 format in the same directory as the video, using the same base file name.

## Requirements
- Python 3
- `moviepy`
- `tqdm`

## Installation

### Step 1: Install Dependencies
Before using the script, you must ensure that the required Python libraries are installed. You can install them using pip:

```bash
pip install moviepy tqdm
```

### Step 2: Make the Script Executable
After downloading the script, you need to make it executable and move it to a directory in your PATH to use it from anywhere in the terminal. Run the following commands:

```bash
chmod +x extractmp3.py
sudo mv extractmp3.py /usr/local/bin/extractmp3
```

## Usage
To extract audio from a video, simply use the script from the command line by providing the path to the MP4 video file:

```bash
extractmp3 path_to_your_video.mp4
```

The script will show a progress bar during the extraction process and notify you when the MP3 file has been successfully created.

Enjoy :)