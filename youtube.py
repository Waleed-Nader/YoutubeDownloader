import os
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from pytube import YouTube
from pytube.cli import on_progress
from threading import *

#Display Window
dock = tk.Tk()
dock.geometry('500x300')
dock.resizable(0,0)
dock.title("Youtube Video Downloader")

tk.Label(dock, text ="| Youtube Video Downloader |", font ="arial 20 bold").pack()

#Enter the URL
link = tk.StringVar()

tk.Label(dock, text ="Paste Link Here:", font ="arial 15 bold").place(x=160, y=60)
link_error = tk.Entry(dock, width =70, textvariable = link).place(x =32, y=90)

#progress bar
bar= Progressbar(dock, orient=tk.HORIZONTAL, length=300,mode='determinate').place(x=100,y=120)    

def on_progress(stream, chunk, bytes_remaining):
  global inc,bar
  total_size = YouTube(str(link.get())).streams.get_highest_resolution().filesize
  bytes_downloaded = total_size - bytes_remaining
  percentage_of_completion = bytes_downloaded / total_size * 100
  inc=float(percentage_of_completion)
  print(inc)
  bar= Progressbar(dock, orient=tk.HORIZONTAL, length=300,mode='determinate',value=inc).place(x=100,y=120)    

#getusername
username= os.getlogin()

#path
path= "C:/Users/"+username+"/Downloads"

#downloader func
def Downloader():
    url =YouTube(str(link.get()),on_progress_callback= on_progress)
    video =url.streams.filter(file_extension = "mp4").first()
    video.download(path)
    tk.Label(dock, text ="Successfully Downloaded", font ="arial 15").place(x =120, y =220)


def threading():
    t1=Thread(target=Downloader)
    t1.start()

#Download Button
tk.Button(dock, text ="DOWNLOAD", font ="Verdana 15 bold", bg ="orange", padx =2, command =threading).place(x=180, y=170)


win = dock.mainloop()

Thread(target=win).start()
