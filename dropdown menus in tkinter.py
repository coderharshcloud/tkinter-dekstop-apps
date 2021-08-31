from tkinter import*

window=Tk()

window.title("dropdown menus")
window.geometry("500x500")

r=IntVar()

menu=OptionMenu(window, r ,"monday","tuesday","wednesday",'thursday')
menu.pack()

window.mainloop()