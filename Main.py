from tkinter import *
import tkinter as tk
from gtts import gTTS
from playsound import playsound
import os
import pyttsx3
import speech_recognition as sr

root = tk.Tk()
root.geometry('350x300')
root.configure(bg='ghost white')
root.title("TEXT TO SPEECH")

Label(root, text="TEXT TO SPEECH", font='arial 20 bold', bg='white smoke',).pack()
Label(text="Panny Tech", font='arial 15 bold', bg='white smoke', width='20',).pack(side='bottom')

Msg = StringVar()
Label(root,text ="Enter Text", font='arial 15 bold', bg='white smoke').place(x=20,y=60)

entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20,y=100)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Panny.mp3')
    playsound('Panny.mp3')
    os.remove('Panny.mp3')
    

def Exit():
    root.destroy()

def Reset():
    Msg.set(" ")

Button(root, text="Play", font='arial 15 bold',
    command=Text_to_speech, width='4', bg='light blue').place(x=25, y=140)

Button(root, text="Reset", font='arial 15 bold',
    command=Reset).place(x=125, y=140)



root.mainloop()