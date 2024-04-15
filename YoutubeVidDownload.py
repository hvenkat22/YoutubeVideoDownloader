from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_vid(url, path):
    try:
        yt = YouTube(url)
        streams=yt.streams.filter(progressive=True,file_extension="mp4")
        highest = streams.get_highest_resolution()
        highest.download(output_path=path)
        print("Video was downloaded successfully!")

    except Exception as e:
        print(e)

def open_file():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    
    return folder

if __name__ == "__main__":
    win = tk.Tk()
    win.withdraw()

    url= input("Enter the Youtube URL: ")
    save = open_file()

    if save:
        print("Started download...")
        download_vid(url,save)
    else:
        print("An Error occured.....")