# Imports graphical window
from tkinter import *
from tkinter import ttk as ttk

# -------------------------------- Core Functions -------------------------------- #

# The basic text interface
def recordInterface(record) :
    return f"""ID: {record["ID"]}\nName: {record["Name"]}\nMath: {record["Math"]}\nEnglish: {record["English"]}\nScience: {record["Science"]}\nCourse Total: {record["Course Total"]}\nExam Percentage: {record["Exam Percentage"]}%\nTotal Percentage: {record["Total Percentage"]}%\nGrade: {record["Grade"]}"""

# Shows all records
def showAllRecords(textWidget, records) :
    textContent = ""
    textWidget.delete("1.0", END)

    for info in records : textContent += recordInterface(info) + "\n\n[ ---- Section ---- ]\n\n"

    textWidget.insert(END, textContent)

# Finds the highest scoring student
def showHighestScore(textWidget, records) :
    textContent = "Unknown Student"
    textWidget.delete("1.0", END)

    maxPercentage = max(info.get("Total Percentage") for info in records)
    highStudents = [info for info in records if info.get("Total Percentage") == maxPercentage]

    textContent = f"Highest Percentage: {maxPercentage}%\n\n[ ---- Section ---- ]\n\n"
    textContent += "\n\n[ ---- Section ---- ]\n\n".join(recordInterface(info) for info in highStudents)
    textWidget.insert(END, textContent)

# Finds the lowest scoring student
def showLowestScore(textWidget, records) :
    textContent = "Unknown Student"
    textWidget.delete("1.0", END)

    minPercentage = min(info.get("Total Percentage") for info in records)
    lowStudents = [info for info in records if info.get("Total Percentage") == minPercentage]

    textContent = f"Lowest Percentage: {minPercentage}%\n\n[ ---- Section ---- ]\n\n"
    textContent += "\n\n[ ---- Section ---- ]\n\n".join(recordInterface(info) for info in lowStudents)
    textWidget.insert(END, textContent)

# Shows the individual student
def showIndividual(textWidget, records, nameList, name) :
    textContent = "Unknown Student"
    textWidget.delete("1.0", END)

    if name not in nameList :
        textWidget.insert(END, textContent)
        return

    selectStudent = [info for info in records if info.get("Name") == name]

    textContent = f"Selected Student: {name}\n\n[ ---- Section ---- ]\n\n{recordInterface(selectStudent[0])}"
    textWidget.insert(END, textContent)

def compileRecords() :
    recordBook = []

    with open("Year 2 - Semester 1/3 - Advanced Programming/Assessments/Assessment 1/studentMarks.txt") as fileHandler :
        # Skip first line
        next(fileHandler, None)

        # Reads each line as a list and compiles the items
        for record in fileHandler.readlines() :
            studentId, studentName, course0, course1, course2, exam = record.strip().split(",")

            studentId = int(studentId)
            course0 = int(course0)
            course1 = int(course1)
            course2 = int(course2)
            exam = float(exam)

            totalMarks = course0 + course1 + course2
            percentage = round((totalMarks + exam) / 1.6, 1)

            grade = "D" if percentage > 40 else "F"
            grade = "C" if percentage > 50 else grade
            grade = "B" if percentage > 60 else grade
            grade = "A" if percentage > 70 else grade

            recordBook += [
                {
                    "ID" : studentId,
                    "Name" : studentName,
                    "Math" : course0,
                    "English" : course1,
                    "Science" : course2,
                    "Course Total" : totalMarks,
                    "Exam Percentage" : exam,
                    "Total Percentage" : percentage,
                    "Grade" : grade
                }
            ]

    return recordBook

# Display menu first
def displayMenu() :
    # Compile records first
    recordBook = compileRecords()
    # Get a list of names
    nameList = [info.get("Name") for info in recordBook]

    # Sets combobox style
    ttk.Style().configure("combo0.TCombobox", background = "light gray")
    # Assign combobox and textbox to a variable for later use
    combo0 = ttk.Combobox(frame0, values = nameList, font = ("Arial", 16, "bold"), style = "combo0.TCombobox")
    text0 = Text(frame0, font = ("Arial", 16, "bold"))

    # Main layout
    Label(frame0, text = "Student Manager", font = ("Arial", 32, "bold"), bg = "light gray").grid(column = 1, row = 0)
    Button(frame0, text = "View All Records", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: showAllRecords(text0, recordBook)).grid(column = 0, row = 1, sticky = "EW")
    Button(frame0, text = "Show Highest Score", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: showHighestScore(text0, recordBook)).grid(column = 1, row = 1, sticky = "EW")
    Button(frame0, text = "Show Lowest Score", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: showLowestScore(text0, recordBook)).grid(column = 2, row = 1, sticky = "EW")
    Button(frame0, text = "View Individual Record", font = ("Arial", 16, "bold"), fg = "white", bg = "black", command = lambda: showIndividual(text0, recordBook, nameList, combo0.get())).grid(column = 0, row = 2, sticky = "EW")
    combo0.grid(column = 1, row = 2, columnspan = 2, sticky = "NSEW")

    # The great wall of text
    text0.grid(column = 0, row = 3, columnspan = 3, sticky = "EW")

    # Selects the first available item
    combo0.current(0)

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