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
    height = int(screenHeight * 0.5),
    bg = "light gray"
)

# Labels

label0 = Label(
    mainWindow,
    text = "Hello, my name is Frem.",
    font = ("Arial", 24, "bold")
)

label1 = Label(
    mainWindow,
    text = "I am studying in Metaverse Age Training Institute Dubai.",
    font = ("Arial", 24, "bold")
)

label2 = Label(
    mainWindow,
    text = "I am enrolled in Creative Computing L5.",
    font = ("Arial", 24, "bold")
)

# Check

check0 = Checkbutton(
    frame0,
    text = "Fixing Stuff",
    font = ("Arial", 16, "bold"),
    bg = "light gray"
)

check1 = Checkbutton(
    frame0,
    text = "Watching Movies",
    font = ("Arial", 16, "bold"),
    bg = "light gray"
)

check2 = Checkbutton(
    frame0,
    text = "Playing Games",
    font = ("Arial", 16, "bold"),
    bg = "light gray"
)

check3 = Checkbutton(
    frame0,
    text = "Family Time",
    font = ("Arial", 16, "bold"),
    bg = "light gray"
)

# Radio

radio0 = Radiobutton(
    frame0,
    text = "Cybersecurity Analyst",
    value = 1,
    font = ("Arial", 16, "bold"),
    bg = "light gray"
)

radio1 = Radiobutton(
    frame0,
    text = "Frontend Developer",
    value = 2,
    font = ("Arial", 16, "bold"),
    bg = "light gray"
)

radio2 = Radiobutton(
    frame0,
    text = "Backend Developer",
    value = 3,
    font = ("Arial", 16, "bold"),
    bg = "light gray"
)

radio3 = Radiobutton(
    frame0,
    text = "CEO",
    value = 4,
    font = ("Arial", 16, "bold"),
    bg = "light gray"
)

# Buttons

button0 = Button(
    frame0,
    text = "Submit",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

# Placing the widgets

frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

label0.place(relx = 0.5, rely = 0.05, anchor = "center")
label1.place(relx = 0.5, rely = 0.1, anchor = "center")
label2.place(relx = 0.5, rely = 0.15, anchor = "center")

check0.place(relx = 0.4, rely = 0.1, anchor = "w")
check1.place(relx = 0.4, rely = 0.2, anchor = "w")
check2.place(relx = 0.4, rely = 0.3, anchor = "w")
check3.place(relx = 0.4, rely = 0.4, anchor = "w")

radio0.place(relx = 0.4, rely = 0.5, anchor = "w")
radio1.place(relx = 0.4, rely = 0.6, anchor = "w")
radio2.place(relx = 0.4, rely = 0.7, anchor = "w")
radio3.place(relx = 0.4, rely = 0.8, anchor = "w")

button0.place(relx = 0.5, rely = 0.9, anchor = "center")

# Needs to be at the end
mainWindow.mainloop()