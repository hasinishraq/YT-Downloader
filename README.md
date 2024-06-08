# YouTube Video Downloader

This Python application is a simple YouTube video downloader with a graphical user interface (GUI) built using CustomTkinter. It allows users to download YouTube videos by providing a link and displays the download progress in real-time.

## Features

- **Responsive UI**: The application remains responsive during the download process by using threading to handle the download in the background.
- **Progress Display**: The download progress is displayed both as a percentage and with a progress bar.
- **Error Handling**: The application provides feedback if the download fails for any reason.

## Requirements

- Python 3.x
- CustomTkinter
- Pytube
- Threading

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/hasinishraq/YT-Downloader.git
    cd YouTube-Video-Downloader
    ```

2. **Install the required packages:**

    ```bash
    pip install customtkinter pytube
    ```

## Usage

1. **Run the application:**

    ```bash
    python downloader.py
    ```

2. **Enter a YouTube link** into the input field and click the "Download" button.
3. **Watch the progress** as the video downloads. The progress bar and percentage will update in real-time.
4. **Completion**: Once the download is complete, a message will indicate the successful download.

## Code Overview

### Main Functions

- `startDownload()`: Initiates the download process, retrieves video information, and starts the download in a separate thread.
- `download_video(video)`: Downloads the video and updates the UI upon completion or failure.
- `on_progress(stream, chunk, bytes_remaining)`: Updates the progress bar and percentage as the video downloads.

### UI Components

- **Title Label**: Displays the application title.
- **Link Input**: Field for entering the YouTube video link.
- **Finish Label**: Displays the status of the download (completed or failed).
- **Progress Percentage**: Shows the percentage of the download completed.
- **Progress Bar**: Visual representation of the download progress.
- **Download Button**: Starts the download process when clicked.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
