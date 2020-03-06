from tkinter import *
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.4)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()
window.title("Welcome ")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)

def clicked():
	text = txt.get()
	speak(text)

def speak(text):
	engine.say(text)
	engine.runAndWait()


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
