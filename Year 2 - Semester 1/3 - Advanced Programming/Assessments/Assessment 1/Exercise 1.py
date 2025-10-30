# Imports graphical window
from tkinter import *

# Will be needed for randomInt()
from random import *

count = 0
scores = 0

# -------------------------------- Additional Functions -------------------------------- #

# Clears frame
def clearFrame() :
    for widget in frame0.winfo_children() :
        widget.pack_forget()

# -------------------------------- Main Functions -------------------------------- #

# A function that determines the values used in each question. The min and max values of the numbers should be based on the difficulty level chosen as described above.
def randomInt(digits) :
    randFloat = random() * 9.99999999

    return int(randFloat * (10.0 ** (digits - 1)))

# A function that checks whether the users answer was correct and outputs an appropriate message
def isCorrect(input, solution, level) :
    global count
    global scores

    count += 1

    if input == solution : scores += level

    if count < 4 :
        clearFrame()

        Label(frame0, text = f"Solution: {solution}", font = ("Arial", 16, "bold")).pack()
        Button(frame0, text = "Continue", font = ("Arial", 16, "bold"), command = lambda: displayProblem(level)).pack()

        return

    displayResults(scores)

# function that outputs the users final score out of a possible 100 and ranks the user based on their score (e.g. A+ for a score over 90)
def displayResults(scores) :
    clearFrame()

    Label(frame0, text = f"Score: {scores}", font = ("Arial", 16, "bold")).pack()
    Button(frame0, text = "Menu", font = ("Arial", 16, "bold"), command = lambda: displayMenu()).pack()

# A function that randomly decides whether the problem is an addition or subtraction problem and returns a char.
def decideOperation() :
    if bool(getrandbits(1)) : return "+"
    return "-"

# A function that displays the question to the user and accepts their answer.
def displayProblem(level) :
    clearFrame()

    num0 = randomInt(2)
    problemo = "0"

    if level == 0 :
        num1 = randomInt(1)
        problemo = f"{num0} {decideOperation()} {num1}"
    if level == 1 :
        num1 = randomInt(2)
        problemo = f"{num0} {decideOperation()} {num1}"
    if level == 2 :
        num1 = randomInt(2)
        num2 = randomInt(2)
        problemo = f"{num0} {decideOperation()} {num1} {decideOperation()} {num2}"
    
    solution = eval(problemo)

    entry0 = Entry(frame0, font = ("Arial", 16, "bold"))

    Label(frame0, text = problemo, font = ("Arial", 16, "bold")).pack()
    entry0.pack()
    Button(frame0, text = "Check", font = ("Arial", 16, "bold"), command = lambda: isCorrect(int(entry0.get()), solution, level)).pack()

# A function that displays the difficulty level menu at the beginning of the quiz.
def displayMenu() :
    clearFrame()

    Label(frame0, text = "Math Quize' 9000", font = ("Arial", 16, "bold")).pack()
    Button(frame0, text = "Beginner", font = ("Arial", 16, "bold"), command = lambda: displayProblem(0)).pack()
    Button(frame0, text = "Moderate", font = ("Arial", 16, "bold"), command = lambda: displayProblem(1)).pack()
    Button(frame0, text = "Advanced", font = ("Arial", 16, "bold"), command = lambda: displayProblem(2)).pack()

# -------------------------------- Main Window -------------------------------- #

# Initializes a main TKinter window
mainWindow = Tk()

# Sets the window's name/title
mainWindow.title("Exercise 1: Math Quiz")

# Gets window size
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()

halfWidth = int(screenWidth * 0.5)
halfHeight = int(screenHeight * 0.5)

# Sets window size
mainWindow.geometry(f"{halfWidth}x{halfHeight}")

# -------------------------------- Main Frame -------------------------------- #

frame0 = Frame(
    mainWindow,
    width = screenWidth,
    height = screenHeight
)

# Initial frame to contain all the elements
frame0.place(relx = 0.5, rely = 0.5, anchor = "center")

# Display menu first
displayMenu()

# Required at the end
mainWindow.mainloop()