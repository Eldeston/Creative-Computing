# Imports graphical window
from tkinter import *

# Will be needed to randomize the selected jokes
import random

# -------------------------------- Additional Functions -------------------------------- #

# Clears frame
def clearFrame() :
    for widget in frame0.winfo_children() : widget.pack_forget()

# -------------------------------- Core Functions -------------------------------- #

# Display the punchline
def displayPunch(setup, punch) :
    clearFrame()

    Label(frame0, text = setup, font = ("Arial", 16, "bold"), bg = "light gray").pack()
    Label(frame0, text = punch, font = ("Arial", 16, "bold"), bg = "light gray").pack()
    Button(frame0, text = "Okay.", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayMenu()).pack()
    Button(frame0, text = "Tell me another!", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayJoke()).pack()

# Display the joke
def displayJoke(prompt = "Alexa, tell me a joke.") :
    clearFrame()

    if prompt != "Alexa, tell me a joke." :
        Label(frame0, text = "I'm sorry, I don't recognize that function.", font = ("Arial", 16, "bold"), bg = "light gray").pack()
        Button(frame0, text = "Okay.", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayMenu()).pack()
        return

    with open("Year 2 - Semester 1/3 - Advanced Programming/Assessments/Assessment 1/randomJokes.txt") as fileHandler :
        contents = random.choice(fileHandler.readlines()).strip()
    
    setup, punch = contents.split("?", 1)
    setup = setup.strip() + "?"

    Label(frame0, text = setup, font = ("Arial", 16, "bold"), bg = "light gray").pack()
    Button(frame0, text = "Why?", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayPunch(setup, punch)).pack()

# Display menu
def displayMenu() :
    clearFrame()

    entry0 = Entry(frame0, font = ("Arial", 16, "bold"))

    Label(frame0, text = "Uncle Alexa, begin by asking \"Alexa, tell me a joke.\"", font = ("Arial", 16, "bold"), bg = "light gray").pack()
    entry0.pack()

    Button(frame0, text = "Enter Prompt.", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayJoke(entry0.get())).pack()

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

frame0 = Frame(mainWindow, bg = "light gray")

# Initial frame to contain all the elements
frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

# Display menu first
displayMenu()

# -------------------------------- Main Loop -------------------------------- #

# Required at the end
mainWindow.mainloop()