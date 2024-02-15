from tkinter import messagebox
from pytube import YouTube
import tkinter as tk


root = tk.Tk()
root.title("YouTube download")
root.geometry("300x300")
root.configure(bg="red")

def click():
    url_text = url.get()
    yt = YouTube(url_text)
    video = yt.streams.get_highest_resolution()
    video.download()
    messagebox.showinfo("YouTube download", "Film został pobrany!")


url = tk.Entry(root, width=30, fg="white")
url.configure(bg="black")
url.pack()

button = tk.Button(root, text="Pobierz", command=click, fg="white")
button.configure(bg="black")
button.pack()



root.mainloop()
