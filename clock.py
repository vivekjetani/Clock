from tkinter import *         # Import everything from tkinter module
from tkinter.ttk import *     # Import everything from tkinter.ttk module
from time import strftime     # Import strftime function from time module to format time and date

# Create the main window
root = Tk()
root.title("Clock")           # Set the title of the window to "Clock"
root.geometry("1920x1080")    # Set the size of the window
root.config(bg="Black")       # Set the background color of the window to black

# Function to toggle fullscreen mode
def fullscreen():
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

# Function to update the time every second
def time():
    t = strftime("%H:%M:%S %p")            # Get current time in the format Hour:Minute:Second AM/PM
    label.config(text=t)                   # Update the label with the current time
    label.place(relx=0.5, rely=0.45, anchor="center")  # Position the label at the center of the window
    label.after(1000, time)                # Call the time function again after 1000 milliseconds (1 second)

# Function to update the date every second
def date():
    d = strftime("%d %b %y")               # Get current date in the format Day Month Year
    label2.config(text=d)                  # Update the label with the current date
    label2.place(relx=0.5, rely=0.65, anchor="center")  # Position the label at the center of the window
    label2.after(1000, date)               # Call the date function again after 1000 milliseconds (1 second)

# Create a label to display the time
label = Label(root, font=("Helvetica", 180), background="Black", foreground="White")
label.pack(anchor='s')                    # Pack the label into the window, aligned to the south

# Create a label to display the date
label2 = Label(root, font=("Helvetica", 90), background="Black", foreground="White")
label2.pack(anchor='s')                   # Pack the label into the window, aligned to the south

# Call the functions to update time and date
time()
date()

# Bind the Escape key to toggle fullscreen mode
root.bind('<Escape>', lambda e: fullscreen())

# Run the main loop to keep the window open
mainloop()
