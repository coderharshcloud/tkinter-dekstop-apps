from tkinter import*

window=Tk()

r=IntVar()
s=IntVar()


def clicked():
    mylabel=Label(window,text=r.get())
    mylabel.pack()
    lbl=Label(window,text=s.get())
    lbl.pack()
mybutton1=Radiobutton(window,text="option1",variable=r,value=1,command=clicked)
mybutton2=Radiobutton(window,text="option2",variable=s,value=2,command=clicked)
mybutton1.pack()
mybutton2.pack()
window.mainloop()