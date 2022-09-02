from pytube import YouTube
import os
from moviepy.editor import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root=Tk()
def downloadVideo(downloadlink:str):
    try:
        yt=YouTube(downloadlink).streams.filter(progressive=True, file_extension="mp4").first().download()
        video=VideoFileClip(os.path.join(yt))
        video.audio.write_audiofile(os.path.join(str.replace(yt,".mp4",".mp3")))
        os.remove(yt)
        messagebox.showinfo("Jawoll","Download Erflogreich")
    except:
        messagebox.showerror("Auweh", "Ungültiger Link")


window= ttk.Frame(root, padding=10,height=1000,width=500)
window.grid()
inputLink=Entry(window)
inputLink.grid(column=0,row=0)

def startDownload():
    downloadVideo(inputLink.get())
    inputLink.delete(0,END)
    
ttk.Button(window, text="Download" ,command=startDownload).grid(column=0, row=1)

root=mainloop()





