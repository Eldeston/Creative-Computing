# Imports graphical window
import tkinter as tk
import tkinter.ttk as ttk

# Initializes a main TKinter window
mainWindow = tk.Tk()

# Sets the window's name/title
mainWindow.title("Student Management System")

# Gets window size
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()

halfWidth = int(screenWidth * 0.5)
halfHeight = int(screenHeight * 0.5)

# Sets window size
mainWindow.geometry(f"{halfWidth}x{halfHeight}")

frame0 = tk.Frame(
    mainWindow,
    width = int(screenWidth * 0.5),
    height = int(screenHeight * 0.5),
    bg = "light gray"
)

# Labels

label0 = tk.Label(
    frame0,
    text = "Student Management System",
    font = ("Arial", 24, "bold")
)

label1 = tk.Label(
    frame0,
    text = "New Student Registration",
    font = ("Arial", 16, "bold"),
    bg = "light gray"
)

label2 = tk.Label(
    frame0,
    text = "Student Name",
    font = ("Consolas", 16),
    bg = "light gray"
)

label3 = tk.Label(
    frame0,
    text = "Mobile Number",
    font = ("Consolas", 16),
    bg = "light gray"
)

label4 = tk.Label(
    frame0,
    text = "Email ID",
    font = ("Consolas", 16),
    bg = "light gray"
)

label5 = tk.Label(
    frame0,
    text = "Home Address",
    font = ("Consolas", 16),
    bg = "light gray"
)

label6 = tk.Label(
    frame0,
    text = "Parent Details",
    font = ("Consolas", 16),
    bg = "light gray"
)

label7 = tk.Label(
    frame0,
    text = "Course Enrolled",
    font = ("Consolas", 16),
    bg = "light gray"
)

# Entries

entry0 = tk.Entry(
    frame0,
    font = ("Consolas", 16),
    fg = "white",
    bg = "gray"
)

entry1 = tk.Entry(
    frame0,
    font = ("Consolas", 16),
    fg = "white",
    bg = "gray"
)

entry2 = tk.Entry(
    frame0,
    font = ("Consolas", 16),
    fg = "white",
    bg = "gray"
)

entry3 = tk.Entry(
    frame0,
    font = ("Consolas", 16),
    fg = "white",
    bg = "gray"
)

entry4 = tk.Entry(
    frame0,
    font = ("Consolas", 16),
    fg = "white",
    bg = "gray"
)

# List

combobox0style = ttk.Style()
combobox0style.theme_use('clam')  # Use a theme that supports styling

# Configure the Combobox style
combobox0style.configure("TCombobox",
    fieldbackground="gray",   # Background of the entry field
    background="gray",         # Background of the dropdown
    foreground="white",         # Text color
)

combobox0 = ttk.Combobox(
    frame0,
    values = ["Creative Computing", "Business Management", "Psychology", "Cybersecurity"],
    font = ("Consolas", 16, "bold"),
    foreground = "white",
    background = "gray"
)

# Buttons

button0 = tk.Button(
    frame0,
    text = "Submit",
    font = ("Consolas", 16),
    fg = "white",
    bg = "black"
)

# Placing the widgets

label0.grid(row = 0, column = 0)

frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

label1.grid(row = 1, column = 0)
label2.grid(row = 2, column = 0)
label3.grid(row = 3, column = 0)
label4.grid(row = 4, column = 0)
label5.grid(row = 5, column = 0)
label6.grid(row = 6, column = 0)
label7.grid(row = 7, column = 0)

entry0.grid(row = 2, column = 1, sticky = "we")
entry1.grid(row = 3, column = 1, sticky = "we")
entry2.grid(row = 4, column = 1, sticky = "we")
entry3.grid(row = 5, column = 1, sticky = "we")
entry4.grid(row = 6, column = 1, sticky = "we")

combobox0.grid(row = 7, column = 1, sticky = "we")

button0.grid(row = 8, column = 0, columnspan = 2, sticky = "we")

# Needs to be at the end
mainWindow.mainloop()