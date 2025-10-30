# Imports graphical window
from tkinter import *

# Will be needed to randomize the selected jokes
import random

# Initializes a main TKinter window
mainWindow = Tk()

# Sets the window's name/title
mainWindow.title("Exercise 1: Math Quiz")

# Gets window size
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()

halfWidth = int(screenWidth * 0.5)
halfHeight = int(screenHeight * 0.5)

# Sets window size
mainWindow.geometry(f"{halfWidth}x{halfHeight}")

# Required at the end
mainWindow.mainloop()