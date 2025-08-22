from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t = 0

def set():
    global t
    rem = sd.askstring("Время напоминания","введите время напоминания в формате ЧЧ:ММ (в 24ч. формате)")
    if rem:
       try:
           hour = int(rem.split(":")[0])
           minute = int(rem.split(":")[1])
           now = datetime.datetime.now()
           print(now)
           dt = now.replace(hour=hour, minute=minute)
           print(dt)
           t = dt.timestamp()
           print(t)
       except Exception as e:
           mb.showerror("Ошибка!", f"Произошла ошибка {e}")


def chek():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
    window.after(10000,chek)


window = Tk()
window.title("Напоминание")
label = Label(text="Установите напоминание")
label.pack(pady=10)
set_button = Button(text="Установите напоминание", command=set)
set_button.pack()

window.mainloop()


