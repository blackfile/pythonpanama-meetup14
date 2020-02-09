#!/usr/bin/env python

import youtube_dl
from tkinter import *
from tkinter import messagebox as MessageBox

def my_hook(data):
    if data['status'] == 'finished':
        MessageBox.showinfo("Completado", "Video Descargado Correctamente")
   

def getvideo():
    ydl_opts = {
    #'format': 'bestaudio/best',
    'outtmpl': 'Download/%(title)s',
    'noplaylist' : True,
    'progress_hooks': [my_hook],

}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([txt.get()])


# Creamos gui
ventana = Tk()
ventana.resizable(1,1)
ventana.title("Python Panama - Video Downloader")
ventana.geometry('800x600')



lbl = Label(ventana, text="URL")

lbl.grid(row=0, column=0)

txt = Entry(ventana,width=40)
txt.grid(row=0, column=1)

btn = Button(ventana, text="Descargar Video", command=getvideo)
btn.grid(row=1, column=1)

#main
ventana.mainloop()
