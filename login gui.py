from tkinter import*
from tkinter import messagebox


window=Tk()
window.geometry("500x500")
window.title("login")

username="harsh5"
password="12harsh2006"

mylbl=Label(window,text="Enter your username here:",font=20)
mylbl.grid(row=0,column=0)

e1=Entry(window,width=30,borderwidth=7)
e1.grid(row=0,column=1)

mylbl2=Label(window,text="Enter your password here:",font=20 )
mylbl2.grid(row=2,column=0)

e2=Entry(window,width=30,borderwidth=7)
e2.grid(row=2,column=1)

def login():
    if username!=e1.get():
        messagebox.showerror("error","This username does not exist")

    if password!=e2.get():
        messagebox.showerror("error","This password does not exist")

    if username == e1.get() and password == e2.get():
        messagebox.showinfo("logged in","You are successfully logeed in !")        
        new_window=Toplevel()
        newlbl=Label(new_window,text="welcome to the new window")
        newlbl.pack()
        
        new_window.mainloop()

login_but=Button(window,text="login",bg="orange",padx=30,pady=10,command=login)
login_but.grid(row=4,column=0)



window.mainloop()