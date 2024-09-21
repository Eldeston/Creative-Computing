# -------- Exercise 5 --------

# We gather here today to take refuge from exercise4.py which devastatingly took a lot of time.
# We shall take back what is ours.

# For sys.exit()
import sys

# Announce program.
print("Welcome to the \"Days O' Month Counter\" program! \nTo enter advanced mode, type \"Advanced.\" \nTo exit the program, just type \"Exit.\"")

# Create a "dictionary" for the months and days.
# Months is declared as a tuple as it remains constant througout the code.
months = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
# Days is declared as a list as the days of febuary will be changed when advanced mode is enabled.
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# (several hours later)

# MY GOODNESS how did I miss that dictionaries exist.
# TO BE CONTINUED
calendar = {
    "January" : 31,
    "Febuary" : 28,
    "March" : 31,
    "April" : 30,
    "May" : 31,
    "June" : 30,
    "July" : 31,
    "August" : 31,
    "September" : 30,
    "October" : 31,
    "November" : 30,
    "December" : 31
}

# Advanced mode setting disabled by default.
advancedMode = False

# Second input check to rerun the loop
secondInput = False
# Default number is 1
userInput1 = "1"

# For this one, I experimented using flow control functions after discovering how loops work in Python.
# Keep loop running until user exits.
while True :
    # Automagically turn every user input lower case.
    userInput0 = input("Enter month number between 1-12. ").lower()

    # Second input if advanced mode is enabled
    if advancedMode : userInput1 = input("Enter year number between 0-10000. ").lower()

    # If the input is "exit," say goodby and exit program.
    if "exit" in (userInput0, userInput1) :
        print("Goodbye and have a nice day!")
        sys.exit()

    # If the input is "advanced," enable or disable advanced mode
    if "advanced" in (userInput0, userInput1) :
        # This allows us to "switch" between True and False
        advancedMode = not advancedMode
        # Display status
        print("Advanced mode: ", advancedMode)
        # Go back to the start of the loop
        continue

    if userInput1.isdigit() and advancedMode :
        year = int(userInput1)

        # Call me pessimistic but I don't think humankind is gonna live that long.
        # range() generates a list from 0-10000. Optionally, you can change the increment.
        if year in range(0, 10000) :
            if year % 4 == 0 : days.insert(1, 29)
            else : days.insert(1, 28)

    # Here is the core of the program. First check if it is a digit with isdigit().
    if userInput0.isdigit() :
        # This correctly maps out the index of elements for the lists used.
        month = int(userInput0) - 1

        # For some reason, 12 is not counted?
        # Further debugging may be required
        if month in range(0, 12) :
            print("The number of days in", calendar.keys[month], "is", calendar.values[month], "days.")
            continue

    print("Invalid input. Please enter a month name or month number between 1-12 or type \"Exit.\" to exit the program. ")