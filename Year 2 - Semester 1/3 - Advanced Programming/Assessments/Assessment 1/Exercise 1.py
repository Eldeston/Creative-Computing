# Imports graphical window
from tkinter import *
from tkinter import ttk as ttk

# Will be needed for randomInt()
from random import *

count = 0
scores = 0

# -------------------------------- Additional Functions -------------------------------- #

# Clears frame
def clearFrame() :
    for widget in frame0.winfo_children() : widget.grid_forget()

# -------------------------------- Core Functions -------------------------------- #

# A function that determines the values used in each question. The min and max values of the numbers should be based on the difficulty level chosen as described above.
def randomInt(digits) :
    randFloat = random() * 9.99999999

    return int(randFloat * (10.0 ** (digits - 1)))

# A function that checks whether the users answer was correct and outputs an appropriate message
def isCorrect(userInput, solution, level) :
    global count
    global scores

    clearFrame()

    if not userInput.isdigit() :
        Label(frame0, text = "Please enter in digits", font = ("Arial", 16, "bold"), bg = "light gray").grid(column = 0, row = 0, sticky = "EW")
        Button(frame0, text = "Continue", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayProblem(level)).grid(column = 0, row = 1, sticky = "EW")
        return

    count += 1

    Label(frame0, text = f"Solution: {solution}\nYour Answer: {userInput}", font = ("Arial", 16, "bold"), bg = "light gray").grid(column = 0, row = 0, sticky = "EW")

    if int(userInput) == solution : scores += level

    if count < level * 4 :
        Button(frame0, text = "Continue", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayProblem(level)).grid(column = 0, row = 1, sticky = "EW")
        return

    Button(frame0, text = "Results", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayResults(scores)).grid(column = 0, row = 1, sticky = "EW")

# function that outputs the users final score out of a possible 100 and ranks the user based on their score (e.g. A+ for a score over 90)
def displayResults(scores) :
    global count

    clearFrame()

    Label(frame0, text = f"Score: {scores}\nSolved: {count}", font = ("Arial", 16, "bold"), bg = "light gray").grid(column = 0, row = 0, sticky = "EW")
    Button(frame0, text = "Menu", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayMenu()).grid(column = 0, row = 1, sticky = "EW")

    # Resets counter
    count = 0

# A function that randomly decides whether the problem is an addition or subtraction problem and returns a char.
def decideOperation() :
    return "-" if bool(getrandbits(1)) else "+"

# A function that displays the question to the user and accepts their answer.
def displayProblem(level) :
    clearFrame()

    num0 = randomInt(2)
    problemo = "0"

    if level == 1 : problemo = f"{num0} {decideOperation()} {randomInt(1)}"
    if level == 2 : problemo = f"{num0} {decideOperation()} {randomInt(2)}"
    if level == 3 : problemo = f"{num0} {decideOperation()} {randomInt(2)} {decideOperation()} {randomInt(2)}"
    if level == 4 : problemo = f"{num0} {decideOperation()} {randomInt(3)} {decideOperation()} {randomInt(3)}"
    
    solution = eval(problemo)
    entry0 = Entry(frame0, font = ("Arial", 16, "bold"))

    Label(frame0, text = problemo, font = ("Arial", 16, "bold"), bg = "light gray").grid(column = 0, row = 0, sticky = "EW")
    entry0.grid(column = 0, row = 1, sticky = "EW")

    Button(frame0, text = "Check", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: isCorrect(entry0.get(), solution, level)).grid(column = 0, row = 2, sticky = "EW")

# A function that displays the difficulty level menu at the beginning of the quiz.
def displayMenu() :
    clearFrame()

    Label(frame0, text = "Math Quize' 9000", font = ("Arial", 16, "bold"), bg = "light gray").grid(column = 0, row = 0, sticky = "EW")
    Button(frame0, text = "Beginner", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayProblem(1)).grid(column = 0, row = 1, sticky = "EW")
    Button(frame0, text = "Moderate", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayProblem(2)).grid(column = 0, row = 2, sticky = "EW")
    Button(frame0, text = "Advanced", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayProblem(3)).grid(column = 0, row = 3, sticky = "EW")
    Button(frame0, text = "Insanity", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: displayProblem(4)).grid(column = 0, row = 4, sticky = "EW")

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

# Display menu first
displayMenu()

# -------------------------------- Main Loop -------------------------------- #

# Required at the end
mainWindow.mainloop()