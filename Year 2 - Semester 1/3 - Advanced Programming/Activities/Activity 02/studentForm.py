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
    text = "Student Management System",
    font = ("Arial", 24, "bold")
)

label1 = Label(
    frame0,
    text = "New Student Registration",
    font = ("Arial", 16, "bold"),
    bg = "light gray"
)

label2 = Label(
    frame0,
    text = "Student Name",
    font = ("Consolas", 16),
    bg = "light gray"
)

label3 = Label(
    frame0,
    text = "Mobile Number",
    font = ("Consolas", 16),
    bg = "light gray"
)

label4 = Label(
    frame0,
    text = "Email ID",
    font = ("Consolas", 16),
    bg = "light gray"
)

label5 = Label(
    frame0,
    text = "Home Address",
    font = ("Consolas", 16),
    bg = "light gray"
)

label6 = Label(
    frame0,
    text = "Parent Details",
    font = ("Consolas", 16),
    bg = "light gray"
)

label7 = Label(
    frame0,
    text = "Course Enrolled",
    font = ("Consolas", 16),
    bg = "light gray"
)

# Entries

entry0 = Entry(
    frame0,
    font = ("Consolas", 16),
    fg = "white",
    bg = "gray"
)

entry1 = Entry(
    frame0,
    font = ("Consolas", 16),
    fg = "white",
    bg = "gray"
)

entry2 = Entry(
    frame0,
    font = ("Consolas", 16),
    fg = "white",
    bg = "gray"
)

entry3 = Entry(
    frame0,
    font = ("Consolas", 16),
    fg = "white",
    bg = "gray"
)

entry4 = Entry(
    frame0,
    font = ("Consolas", 16),
    fg = "white",
    bg = "gray"
)

# List

list0 = Listbox(
    frame0,
    height = 4,
    font = ("Consolas", 16, "bold"),
    fg = "white",
    bg = "gray"
)

list0.insert(END, "Creative Computing")
list0.insert(END, "Business Management")
list0.insert(END, "Psychology")
list0.insert(END, "Cybersecurity")

# Buttons

button0 = Button(
    frame0,
    text = "Submit",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

# Placing the widgets

label0.place(relx = 0.5, rely = 0.1, anchor = "n")

frame0.place(relx = 0.5, rely = 0.2, anchor = "n")

label1.place(relx = 0.5, rely = 0.1, anchor = "center")
label2.place(relx = 0.425, rely = 0.2, anchor = "e")
label3.place(relx = 0.425, rely = 0.3, anchor = "e")
label4.place(relx = 0.425, rely = 0.4, anchor = "e")
label5.place(relx = 0.425, rely = 0.5, anchor = "e")
label6.place(relx = 0.425, rely = 0.6, anchor = "e")
label7.place(relx = 0.425, rely = 0.75, anchor = "e")

entry0.place(relx = 0.45, rely = 0.2, anchor = "w")
entry1.place(relx = 0.45, rely = 0.3, anchor = "w")
entry2.place(relx = 0.45, rely = 0.4, anchor = "w")
entry3.place(relx = 0.45, rely = 0.5, anchor = "w")
entry4.place(relx = 0.45, rely = 0.6, anchor = "w")

list0.place(relx = 0.45, rely = 0.75, anchor = "w")

button0.place(relx = 0.5, rely = 0.9, anchor = "center")

# Needs to be at the end
mainWindow.mainloop()