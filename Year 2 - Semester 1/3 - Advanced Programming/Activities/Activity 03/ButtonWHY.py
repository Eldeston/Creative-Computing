# Imports graphical window
from tkinter import *

# Initializes a main TKinter window
mainWindow = Tk()

# Sets the window's name/title
mainWindow.title("Student Management System")

# Gets window size
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()

halfWidth = int(screenWidth * 0.5)
halfHeight = int(screenHeight * 0.5)

# Sets window size
mainWindow.geometry(f"{halfWidth}x{halfHeight}")

# Frames

frame0 = Frame(
    mainWindow,
    width = halfWidth,
    height = halfHeight,
    bg = "light gray"
)

# Labels

label0 = Label(
    frame0,
    text = "WHERE'S THE LAMB SAUCE",
    font = ("Arial", 24, "bold")
)

# Buttons

button0 = Button(
    frame0,
    text = "A",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button1 = Button(
    frame0,
    text = "B",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button2 = Button(
    frame0,
    text = "C",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button3 = Button(
    frame0,
    text = "D",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

# Placing the widgets

frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

label0.place(relx = 0.5, rely = 0.05, anchor = "center")

button0.pack(side = "left", expand = "yes", fill = "y")
button1.pack(side = "top", expand = "yes", fill = "both")
button2.pack(side = "right", expand = "yes", fill = "none", anchor = "ne", pady = 6)
button3.pack(side = "bottom", expand = "no", fill = "y", pady = 6)

# Needs to be at the end
mainWindow.mainloop()