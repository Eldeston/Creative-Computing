# Imports graphical window
from tkinter import *

import random

def openFile() :
    text0.delete(1.0, END)

    with open("Year 2 - Semester 1/3 - Advanced Programming/Activities/Activity 05/beemovie.txt") as file_handler :
        contents = file_handler.read()
        # contents = file_handler.readlines()
        # contents = random.choice(contents).strip()

    text0.insert(END, contents)

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
    bg = "dark gray"
)

# Image

text0 = Text(
    mainWindow,
    width = 80,
    height = 20
)

# Scrollbar

scroll0 = Scrollbar(
    mainWindow,
    orient = VERTICAL
)

# Button

button0 = Button(
    mainWindow,
    text = "Open File",
    font = ("Consolas", 16),
    # Remember to use the directory Python is running on
    command = openFile,
    fg = "white",
    bg = "black"
)

# Config

text0.config(yscrollcommand = scroll0.set)

scroll0.config(command = text0.yview)

# Placing the widgets

frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

text0.place(relx = 0.5, rely = 0.45, anchor = "center")

scroll0.place(relx = 0.7, rely = 0.45, height = 300, anchor = "center")

button0.place(relx = 0.5, rely = 0.7, anchor = "center")

# Needs to be at the end
mainWindow.mainloop()