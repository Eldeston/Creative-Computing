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
    font = ("Arial", 24, "bold"),
    bg = "white"
)

# Entries

entry00 = Entry(
    frame0,
    text = "Enter value to calculate",
    font = ("Consolas", 16)
)

# Buttons

button00 = Button(
    frame0,
    text = "1",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button01 = Button(
    frame0,
    text = "2",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button02 = Button(
    frame0,
    text = "3",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button03 = Button(
    frame0,
    text = "C",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button04 = Button(
    frame0,
    text = "4",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button05 = Button(
    frame0,
    text = "5",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button06 = Button(
    frame0,
    text = "6",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button07 = Button(
    frame0,
    text = "CE",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button08 = Button(
    frame0,
    text = "7",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button09 = Button(
    frame0,
    text = "8",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button10 = Button(
    frame0,
    text = "9",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button11 = Button(
    frame0,
    text = "+",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button12 = Button(
    frame0,
    text = "*",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button13 = Button(
    frame0,
    text = "0",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button14 = Button(
    frame0,
    text = "/",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

button15 = Button(
    frame0,
    text = "-",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

# Placing the widgets

frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

# label0.place(relx = 0.5, rely = 0.05, anchor = "center")

entry00.grid(row = 0, column = 0, columnspan = 4, sticky = "we")

button00.grid(row = 1, column = 0, sticky = "we")
button01.grid(row = 1, column = 1, sticky = "we")
button02.grid(row = 1, column = 2, sticky = "we")
button03.grid(row = 1, column = 3, sticky = "we")

button04.grid(row = 2, column = 0, sticky = "we")
button05.grid(row = 2, column = 1, sticky = "we")
button06.grid(row = 2, column = 2, sticky = "we")
button07.grid(row = 2, column = 3, sticky = "we")

button08.grid(row = 3, column = 0, sticky = "we")
button09.grid(row = 3, column = 1, sticky = "we")
button10.grid(row = 3, column = 2, sticky = "we")
button11.grid(row = 3, column = 3, sticky = "we")

button12.grid(row = 4, column = 0, sticky = "we")
button13.grid(row = 4, column = 1, sticky = "we")
button14.grid(row = 4, column = 2, sticky = "we")
button15.grid(row = 4, column = 3, sticky = "we")

# Needs to be at the end
mainWindow.mainloop()