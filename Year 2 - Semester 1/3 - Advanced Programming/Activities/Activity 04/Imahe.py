# Imports graphical window
from tkinter import *
from PIL import ImageTk, Image

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

image0 = Image.open("Year 2 - Semester 1/3 - Advanced Programming/Activities/Activity 04/hollowKnight.jpg")
image0 = image0.resize(
    (
        200,
        200
    )
)

image0 = ImageTk.PhotoImage(image0)

# Labels

label0 = Label(
    mainWindow,
    image = image0
)

# Placing the widgets

frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

label0.place(relx = 0.5, rely = 0.5, anchor = "center")

# Needs to be at the end
mainWindow.mainloop()