# Imports graphical window
from tkinter import *

# Initializes a main TKinter window
mainWindow = Tk()

# Sets the window's name/title
mainWindow.title("Professor X")

# Frames

frame0 = Frame(
    mainWindow,
    width = 500,
    height = 500,
    bg = "light gray"
)

# Labels

label0 = Label(
    frame0,
    text = "BROS FOREVER",
    font = ("Arial", 8)
)

# Buttons

button0 = Button(
    frame0,
    text = "JAVIER",
    font = ("Consolas", 8),
    fg = "white",
    bg = "black"
)

# Place widgets
frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

label0.place(relx = 0.5, rely = 0.4, anchor = "center")

button0.place(relx = 0.5, rely = 0.6, anchor = "center")

# Needs to be at the end
mainWindow.mainloop()