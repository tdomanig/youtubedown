from pytube import YouTube
import os
from moviepy.editor import *
from tkinter import *

link=input()



def downloadVideo(downloadlink:str):
    try:
        yt=YouTube(downloadlink).streams.filter(progressive=True, file_extension="mp4").first().download()
        video=VideoFileClip(os.path.join(yt))
        video.audio.write_audiofile(os.path.join(str.replace(yt,".mp4",".mp3")))
    except:
        print('Ungültiger Link')

downloadVideo(link)