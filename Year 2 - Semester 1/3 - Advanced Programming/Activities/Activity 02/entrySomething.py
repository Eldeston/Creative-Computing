# Imports graphical window
from tkinter import *

# Initializes a main TKinter window
mainWindow = Tk()

# Sets the window's name/title
mainWindow.title("Entry")

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
    text = "GIVE ME YOUR CREDIT CARD NUMBER.",
    # text = "LAMB SAUCE",
    font = ("Arial", 32, "bold"),
    bg = "lime"
)

entry0 = Entry(
    frame0,
    font = ("Arial", 32, "bold")
)

button0 = Button(
    frame0,
    text = "Ok.",
    font = ("Arial", 16, "bold")
)

check0 = Checkbutton(
    frame0,
    text = "Ok.",
    font = ("Arial", 16, "bold"),
    bg = "lime"
)

radio0 = Radiobutton(
    frame0,
    text = "Ok.",
    value = 1,
    font = ("Arial", 16, "bold"),
    bg = "lime"
)

radio1 = Radiobutton(
    frame0,
    text = "Ok.",
    value = 2,
    font = ("Arial", 16, "bold"),
    bg = "lime"
)

list0 = Listbox(
    frame0,
    font = ("Arial", 16, "bold")
)

list0.insert(END, "Item 1")
list0.insert(END, "Item 2")
list0.insert(END, "Item 3")
list0.insert(END, "Item 4")

frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

label0.place(relx = 0.5, rely = 0.3, anchor = "center")
entry0.place(relx = 0.5, rely = 0.4, anchor = "center")

check0.place(relx = 0.4, rely = 0.5, anchor = "center")
button0.place(relx = 0.6, rely = 0.5, anchor = "center")

radio0.place(relx = 0.4, rely = 0.6, anchor = "center")
radio1.place(relx = 0.6, rely = 0.6, anchor = "center")

list0.place(relx = 0.5, rely = 0.7, anchor = "n")

# Needs to be at the end
mainWindow.mainloop()