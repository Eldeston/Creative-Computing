# Imports graphical window
from tkinter import *

# Initializes a main TKinter window
mainWindow = Tk()

# Sets the window's name/title
mainWindow.title("My First TKinter GUI")

# Gets window size
screenWidth = int(mainWindow.winfo_screenwidth() * 0.5)
screenHeight = int(mainWindow.winfo_screenheight() * 0.5)

# Sets window size
mainWindow.geometry(f"{screenWidth}x{screenHeight}")

frame0 = Frame(
    mainWindow,
    width = screenWidth,
    height = screenHeight,
    bg = "lime"
)

label0 = Label(
    frame0,
    text = "I am studying in Metaverse Training Institute at Dubai.",
    # text = "WHERE'S THE",
    font = ("Times New Roman", 16, "italic"),
    bg = "lime"
)

label1 = Label(
    frame0,
    text = "Hello, my name is Eldeston.",
    # text = "LAMB SAUCE",
    font = ("Arial", 32, "bold"),
    bg = "lime"
)

label2 = Label(
    frame0,
    text = "I am enrolled in Creative Computing Level 5.",
    # text = "BLOODY HAIL.",
    font = ("Papyrus", 16, "bold"),
    bg = "lime"
)

# Centers horizontally and adds horizontal padding
# label0.pack(pady = 16)

# Anchors text at its center and places its position at the center relative to window size
frame0.place(relx = 0.5, rely = 0.5, anchor = "center")
label0.place(relx = 0.5, rely = 0.4, anchor = "center")
label1.place(relx = 0.5, rely = 0.5, anchor = "center")
label2.place(relx = 0.5, rely = 0.6, anchor = "center")

# Needs to be at the end
mainWindow.mainloop()