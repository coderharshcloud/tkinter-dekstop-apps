import os
import pyttsx3
from tkinter import*
from tkinter import messagebox




for virus in range(100):
    
    os.system("start")
    engine=pyttsx3.init("sapi5")
    engine.say("your pc is infected")
    engine.runAndWait()
    
    window=Tk()
    
    label=Label(window,text="status : infected")
    label.pack()
    
    quitbut=Button(window,text="quit window",command=window.quit)
    quitbut.pack()
    
    messagebox.showwarning("device infected","your device is infected with a virus")
    
    window.mainloop()
    







