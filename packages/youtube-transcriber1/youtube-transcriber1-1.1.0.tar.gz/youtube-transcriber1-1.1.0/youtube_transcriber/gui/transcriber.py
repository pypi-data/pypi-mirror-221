import os
import pytube as pt
import whisper
import platform
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog

def download_transcribe_open():
    youtube_link = url_entry.get()
    model_type = model_var.get()

    if youtube_link:
        # Download mp3 from YouTube video
        yt = pt.YouTube(youtube_link)
        stream = yt.streams.filter(only_audio=True)[0]
        stream.download(filename="audio_english.mp3")

    audio_file_path = audio_entry.get()
    if audio_file_path and os.path.exists(audio_file_path):
        # Use the uploaded local audio file
        audio_file_path = os.path.abspath(audio_file_path)
    else:
        # Fallback to the default downloaded file
        audio_file_path = "audio_english.mp3"

    model = whisper.load_model(model_type)

    result = model.transcribe(audio_file_path)

    # Write the transcribed text to a text file
    output_file_path = "transcribed_text.txt"
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(result["text"])

    # Open the text file using the default text editor
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["start", "", output_file_path], shell=True)
        elif platform.system() == "Darwin":  # For MacOS
            subprocess.Popen(["open", output_file_path])
        else:  # For Linux and other systems
            subprocess.Popen(["xdg-open", output_file_path])
    except Exception as e:
        print("Text file saved as:", output_file_path)

def browse_audio_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav")])
    if file_path:
        audio_entry.delete(0, tk.END)
        audio_entry.insert(0, file_path)

# Create the main application window
root = tk.Tk()
root.title("YouTube Transcriber")

# Set the background and foreground colors
root.configure(background="white")
root.option_add("*Foreground", "black")

# Update the style for the widgets
style = ttk.Style()
style.configure("TLabel", foreground="black", background="white")
style.configure("TButton", foreground="black", background="white")
style.configure("TEntry", foreground="black", background="white")

# URL Entry
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Audio File Entry
audio_label = tk.Label(root, text="OR Upload Audio File:")
audio_label.pack()
audio_entry = tk.Entry(root, width=50)
audio_entry.pack()
browse_button = tk.Button(root, text="Browse", command=browse_audio_file)
browse_button.pack()

# Model Type Dropdown
model_var = tk.StringVar(value="tiny")
model_label = tk.Label(root, text="Select Model Type:")
model_label.pack()
model_dropdown = ttk.Combobox(root, textvariable=model_var, values=["tiny", "base", "small", "medium"])
model_dropdown.pack()

# Download, Transcribe, and Open Button
download_button = tk.Button(root, text="Download, Transcribe, and Open", command=download_transcribe_open)
download_button.pack()

# Run the Tkinter main loop
root.mainloop()
