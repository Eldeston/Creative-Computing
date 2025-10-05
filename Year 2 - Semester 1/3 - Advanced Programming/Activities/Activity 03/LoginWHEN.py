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

frame0 = Frame(
    mainWindow,
    width = int(screenWidth * 0.5),
    height = int(screenHeight * 0.5)
)

# Labels

label0 = Label(
    frame0,
    text = "Find: ",
    font = ("Arial", 16)
)

label1 = Label(
    frame0,
    text = "Replace: ",
    font = ("Arial", 16)
)

label2 = Label(
    frame0,
    text = "Direction",
    font = ("Arial", 16)
)

# Entry

entry0 = Entry(
    frame0,
    font = ("Arial", 16)
)

entry1 = Entry(
    frame0,
    font = ("Arial", 16)
)

# Buttons

button0 = Button(
    frame0,
    text = "Find",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button1 = Button(
    frame0,
    text = "Find All",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button2 = Button(
    frame0,
    text = "Replace",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button3 = Button(
    frame0,
    text = "Replace All",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

# Check

check0 = Checkbutton(
    frame0,
    text = "Match Whole Word Only",
    font = ("Arial", 16),
)

check1 = Checkbutton(
    frame0,
    text = "Match Case",
    font = ("Arial", 16),
)

check2 = Checkbutton(
    frame0,
    text = "Wrap Around",
    font = ("Arial", 16),
)

# Radio

radio0 = Radiobutton(
    frame0,
    text = "Up",
    value = 1,
    font = ("Arial", 16),
)

radio1 = Radiobutton(
    frame0,
    text = "Down",
    value = 2,
    font = ("Arial", 16),
)

# Placing the widgets

frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

label0.grid(row = 0, column = 0, sticky = "w")
label1.grid(row = 1, column = 0, sticky = "w")
label2.grid(row = 2, column = 2, sticky = "w")

entry0.grid(row = 0, column = 1, columnspan = 2, sticky = "ew")
entry1.grid(row = 1, column = 1, columnspan = 2, sticky = "ew")

button0.grid(row = 0, column = 5, sticky = "ew")
button1.grid(row = 1, column = 5, sticky = "ew")
button2.grid(row = 2, column = 5, sticky = "ew")
button3.grid(row = 3, column = 5, sticky = "ew")

check0.grid(row = 2, column = 1, sticky = "w")
check1.grid(row = 3, column = 1, sticky = "w")
check2.grid(row = 4, column = 1, sticky = "w")

radio0.grid(row = 3, column = 2, sticky = "w")
radio1.grid(row = 4, column = 2, sticky = "w")

# Needs to be at the end
mainWindow.mainloop()