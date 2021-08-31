from tkinter import*

window=Tk()
window.title("sliders.py")
window.geometry("500x500")

vertical=Scale(window,from_=0,to=500)
vertical.pack()



def slide():
    num=horizontal.get()
    lbl=Label(window,text=num)
    lbl.pack()
    window.geometry(str(num) + "x500")

horizontal=Scale(window,from_=0,to=500,orient=HORIZONTAL)
horizontal.pack()

def slide2():
    num2=vertical.get()
    lbl2=Label(window,text=num2)
    lbl2.pack()
    window.geometry("500x" + str(num2))

but=Button(window,text="click me",command=slide)
but.pack()

but2=Button(window,text="click me",command=slide2)
but2.pack()

window.mainloop()