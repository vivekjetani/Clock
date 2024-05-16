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
    label.place(relx=0.5,rely=0.45,anchor="center")
    label.after(1000,time)

def date():
    d = strftime("%d %b %y")
    label2.config(text=d)
    label2.place(relx=0.5,rely=0.65,anchor="center")
    label2.after(1000,date)


label = Label(root ,font=("Helvetica",180), background="Black",foreground="White")
label.pack(anchor='s')

label2 =Label(root,font=("Helvetica",90), background="Black",foreground="White")
label2.pack(anchor='s')

time()
date()
mainloop()