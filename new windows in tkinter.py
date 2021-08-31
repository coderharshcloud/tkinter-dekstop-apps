from tkinter import*
from PIL import ImageTk,Image

window=Tk()

new_window=Toplevel()
my_img=ImageTk.PhotoImage(Image.open("harsh1.jpg"))
my_label=Label(new_window,image=my_img)
my_label.pack()





window.mainloop()
new_window.mainloop()