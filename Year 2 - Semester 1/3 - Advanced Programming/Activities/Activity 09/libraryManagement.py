# Imports graphical window
from tkinter import *
from tkinter import ttk as ttk

class Application :
    def __init__(self, mainFrame):
        self.mainFrame = mainFrame

        self.mainLib = []

        with open("Year 2 - Semester 1/3 - Advanced Programming/Activities/Activity 09/library.txt") as fileHandler :
            # Reads each line as a list and compiles the items
            for record in fileHandler.readlines() :
                title, author, year, genre = record.strip().split(",")

                self.mainLib += [
                    {
                        "Title" : title,
                        "Author" : author,
                        "Year" : year,
                        "Genre" : genre
                    }
                ]

    def libInterface(self, decode) :
        return f"Title: {decode["Title"]}\nAuthor: {decode["Author"]}\nYear: {decode["Year"]}\nGenre: {decode["Genre"]}"
    
    def loadLibrary(self, mainText) :
        textContent = ""
        mainText.delete("1.0", END)

        for decode in self.mainLib : textContent += self.libInterface(decode) + "\n\n"

        mainText.insert(END, textContent)
    
    def clearFrame(self) :
        for widget in self.mainFrame.winfo_children() : widget.grid_forget()

    def displayMenu(self) :
        self.clearFrame()

        Label(self.mainFrame, text = "Library Management", font = ("Arial", 32, "bold"), bg = "light gray").grid(column = 1, row = 0, sticky = "EW")

        Label(self.mainFrame, text = "Enter Book Title:", font = ("Arial", 16, "bold"), bg = "light gray").grid(column = 0, row = 1, sticky = "EW")
        Entry(self.mainFrame, font = ("Arial", 16, "bold")).grid(column = 1, row = 1, columnspan = 2, sticky = "EW")

        text0 = Text(self.mainFrame, font = ("Arial", 16, "bold"))

        Button(self.mainFrame, text = "Add", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: self.displayMenu()).grid(column = 0, row = 2, sticky = "EW")
        Button(self.mainFrame, text = "View", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: self.loadLibrary(text0)).grid(column = 1, row = 2, sticky = "EW")
        Button(self.mainFrame, text = "Clear", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: self.displayMenu()).grid(column = 2, row = 2, sticky = "EW")

        text0.grid(column = 0, row = 3, columnspan = 3, sticky = "EW")

# -------------------------------- Main Window -------------------------------- #

# Initializes a main TKinter window
mainWindow = Tk()
# Sets the window's name/title
mainWindow.title("Exercise 1: Math Quiz")
# Set window size
mainWindow.geometry(f"360x360")
# Starts maximized
mainWindow.after(1, mainWindow.wm_state, 'zoomed')

# -------------------------------- Main Frame -------------------------------- #

ttk.Style().configure("frame0.TFrame", background = "light gray")
frame0 = ttk.Frame(mainWindow, style = "frame0.TFrame", padding = 32)
# Initial frame to contain all the elements
frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

# Create object
app = Application(frame0)

# Display
app.displayMenu()

# -------------------------------- Main Loop -------------------------------- #

# Required at the end
mainWindow.mainloop()