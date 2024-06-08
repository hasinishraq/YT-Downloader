import customtkinter
from pytube import YouTube
import threading

def startDownload():
    try:
        ytLink = link.get()
        yobject = YouTube(ytLink, on_progress_callback=on_progress)
        video = yobject.streams.get_highest_resolution()
        title.configure(text=yobject.title, text_color="white")
        finishLabel.configure(text="")

        # Downloading video in a separate thread to keep the GUI responsive
        download_thread = threading.Thread(target=download_video, args=(video,))
        download_thread.start()
    except Exception as e:
        finishLabel.configure(text="Download failed: " + str(e), text_color="red")

def download_video(video):
    try:
        video.download()
        finishLabel.configure(text="Download completed", text_color="white")
    except Exception as e:
        finishLabel.configure(text="Download failed: " + str(e), text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    progressBar.set(float(percentage_of_completion) / 100)

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("720x480")
app.iconbitmap
app.title("YouTube Downloader")


# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link", font=("Roboto", 20))
title.pack(padx=10, pady=10)

# Link input
url_var = customtkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=40, textvariable=url_var)
link.pack()

# Finish downloading label
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%", font=("Roboto", 20))
pPercentage.pack()

# Progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400,)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)



# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

app.mainloop()
