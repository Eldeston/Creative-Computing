# -------- Exercise 5 --------

# We gather here today to take refuge from exercise4.py which devastatingly took a lot of time.
# We shall TAKE BACK WHAT IS OURS.

# Announce program.
print(
    """
================================================================
        
        Welcome to the "Days O' Month Counter" program!
        To enter advanced mode, type "Advanced."
        To exit the program, just type "Exit."
        
================================================================
    """
)

# Day calendar dictionary. Contains the number of days each month has.
dayCalendar = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

# Month number dictionary. It acts as a look up table (LUT) so you would not need to do additional calculations like remapping list IDs listName[numberInput - 1].
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

# For this one, I experimented using more flow control functions after discovering how loops work in Python.
# Keep loop running until user exits
while True :
    # Automagically turn every user input lower case.
    userInput = input("Enter month number between 1-12. ").lower()

    # If the input is "exit," say goodbye and exit program.
    if "exit" == userInput :
        print("Goodbye and have a nice day!")
        quit()

    # Here is the core of the program. First check if it is a digit with isdigit().
    if userInput.isdigit() :
        # Use a look up table what month is referred to the number input
        monthNumber = int(userInput)

        # Check if month exists in day calendar
        if monthNumber in monthCalendar.keys() :
            # Ask if it is a leap year. Change the day count accordingly.
            if monthNumber == 2 and input("Is it a leap year?").lower() == "yes" : dayCalendar[2] == 29
            else : dayCalendar[2] == 28
    
            # Display month and days in that month and jump back to the beginning of the loop
            print("The number of days in", monthCalendar[monthNumber], "is", dayCalendar[monthNumber], "days.")
            continue

    # Should all conditions are avoided, it will display invalid input
    print("Invalid input. Please enter a month name or month number between 1-12 or type \"Exit.\" to exit the program. ")