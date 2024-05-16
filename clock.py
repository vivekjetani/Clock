from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")
root.geometry("1920x1080")
root.config(bg="Black")

def time():
    t = strftime("%H:%M:%S %p")
    label.config(text=t)
    label.place(relx=0.5,rely=0.5,anchor="center")
    label.after(1000,time)


label = Label(root ,font=("Helvetica",180), background="Black",foreground="White")
label.pack(anchor='s')


time()
mainloop()