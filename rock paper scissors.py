from tkinter import*
from tkinter import messagebox
import random

window=Tk()
window.geometry("500x500")
window.title("ROCK PAPER SCISSORS")

choices="r","p",'s'
system_choice=random.choice(choices)


user_choice_label=Label(window,text="please enter your choice",bg="skyblue")
myentry=Entry(window,borderwidth=5,width=30,bg="yellow")


def play():
    user_choice=myentry.get()
    
    if system_choice == "r" and user_choice == "paper":
        messagebox.showinfo("rc","you won the system chose rock")
    
    if system_choice == "r" and user_choice == "scissor":
        messagebox.showerror("rc","you lost the system chose rock")

    if system_choice == "r" and user_choice == "rock":
        messagebox.showinfo("rc","it is a tie")

    if system_choice == "p" and user_choice == "rock":
        messagebox.showerror("rc","you lost the system chose paper")        

    if system_choice == "p" and user_choice == "scissor":
        messagebox.showinfo("rc","you won the system chose paper")

    if system_choice == "p" and user_choice == "paper":
        messagebox.showinfo("rc","it is a tie")

    if system_choice == "s" and user_choice == "rock":
        messagebox.showinfo("rc","you won the system chose paper")

    if system_choice == "s" and user_choice == "paper":
        messagebox.showerror("rc","you lost the system chose scissor")

    if system_choice == "s" and user_choice == "scissor":
        messagebox.showinfo("rc","it is a tie")
    
            
mybutton=Button(window,text="show results",padx=20,pady=10,bg="orange",command=play)           
user_choice_label.grid(row=0,column=0)
myentry.grid(row=0,column=2)
mybutton.grid(row=2,column=0,columnspan=3)


window.mainloop()