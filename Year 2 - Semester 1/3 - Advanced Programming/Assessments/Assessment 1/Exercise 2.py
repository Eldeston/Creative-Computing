# Imports graphical window
from tkinter import *

# Will be needed to randomize the selected jokes
import random

# -------------------------------- Main Window -------------------------------- #

# Initializes a main TKinter window
mainWindow = Tk()

# Sets the window's name/title
mainWindow.title("Exercise 1: Math Quiz")

# Starts maximized
mainWindow.after(1, mainWindow.wm_state, 'zoomed')

# -------------------------------- Main Loop -------------------------------- #

# Required at the end
mainWindow.mainloop()