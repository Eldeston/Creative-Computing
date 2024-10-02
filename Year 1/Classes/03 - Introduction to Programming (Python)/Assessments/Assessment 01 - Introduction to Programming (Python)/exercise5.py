# -------- Exercise 5 --------

# We gather here today to take refuge from exercise4.py which devastatingly took a lot of time.
# We shall TAKE BACK WHAT IS OURS.

# For sys.exit()
import sys

# Announce program.
print(
    """
        ================================================================
        
        Welcome to the \"Days O' Month Counter\" program!
        To enter advanced mode, type \"Advanced.\"
        To exit the program, just type \"Exit.\"
        
        ================================================================
    """
)

# Day calendar dictionary. Contains the number of days each month has.
dayCalendar = {
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

# Month number dictionary. It acts as a look up table (LUT) so you would not need to do additional calculations like with lists like listName[numberInput - 1].
monthCalendar = {
    1 : "January",
    2 : "Febuary",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
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

    # Editor's Note: It would be much simpler if I use some kind of loop for an infinite amount of user inputs

    # If the input is "exit," say goodbye and exit program.
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

    # Enables advanced mode features such as adjusting for leap year
    if userInput1.isdigit() and advancedMode :
        year = int(userInput1)

        # Call me pessimistic but I don't think humankind is gonna live that long.
        # range() generates a list from 0-10000. Optionally, you can change the increment.
        if year in range(0, 10000) :
            if year % 4 == 0 : dayCalendar["Febuary"] = 29
            else : dayCalendar["Febuary"] = 28

    # Here is the core of the program. First check if it is a digit with isdigit().
    if userInput0.isdigit() :
        # Use a look up table what month is referred to the number input
        month = monthCalendar[int(userInput0)]

        # Check if month exists in day calendar
        if month in dayCalendar :
            # Display month and days in that month and jump back to the beginning of the loop
            print("The number of days in", month, "is", dayCalendar[month], "days.")
            continue

    # Should all conditions are avoided, it will display invalid input
    print("Invalid input. Please enter a month name or month number between 1-12 or type \"Exit.\" to exit the program. ")