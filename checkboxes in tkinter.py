from tkinter import*

window=Tk()
window.geometry("500x500")

var=StringVar()

mybox=Checkbutton(window,text="check me out",variable=var,onvalue="on",offvalue="off")
mybox.deselect()
mybox.pack()

def check():
    mylbl=Label(window,text=var.get())
    mylbl.pack()







btn=Button(window,text="click me",command=check)
btn.pack()


window.mainloop()