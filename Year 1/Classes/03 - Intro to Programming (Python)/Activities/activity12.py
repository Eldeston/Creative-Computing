# -------- Activity 12 --------

# Used for sys.exit()
import sys

# Announce program
print(
    """
================================================================
        
            Welcome to the Metaverse Admissions!
            To exit the program, just type "Exit."
        
================================================================
    """
)

# Initialize age requirement
ageRequirement = 12

# Keep program running until user exits or completes task
while True :
    # Take user imput, ask for the age
    userInput = input("Enter age: ")

    # First converts input to lowercase and checks if it is equal "exit"
    # This is needed for case insensitive inputs
    if userInput.lower() == "exit" :
        # Announce and exit program
        print("Goodbye and have a nice day!")
        sys.exit()

    # Checks if the string does not contain a digit
    if not userInput.isdigit() :
        # Announce incorrect input and go back to the start of the loop via continue
        print("Invalid input, try again.")
        continue

    # Should the other 2 checks are avoided, proceed converting string to integer
    # The checks make sure if the input is valid or the user decides to exit the program
    userInputInt = int(userInput)
    
    # The need for an else condition is not needed since the continue function will reset to the start of the loop, but should this be required for the activity the code looks like this:
    # Check if user is not within the age requirement
    if userInputInt < ageRequirement :
        # Announce the user is not eligible for college admission and exit program
        print("You are not eligible for college admission.")
        sys.exit()
    else :
        # Otherwise, announce the user is eligible and break the loop
        print("You are eligible for college admission.")
        break

# Announce program
print(
    """
================================================================
        
            Welcome to the Library Admissions!
            To exit the program, just type "Exit."
        
================================================================
    """
)

while True :
    # Take user imput, ask for the days since the book is not returned to the library
    userInput = input("Enter days since the book is not returned: ")

    # First converts input to lowercase and checks if it is equal "exit"
    # This is needed for case insensitive inputs
    if userInput.lower() == "exit" :
        # Announce and exit program
        print("Goodbye and have a nice day!")
        sys.exit()

    # Checks if the string does not contain a digit
    if not userInput.isdigit() :
        # Announce incorrect input and go back to the start of the loop via continue
        print("Invalid input, try again.")
        continue

    # Should the other 2 checks are avoided, proceed converting string to integer
    # The checks make sure if the input is valid or the user decides to exit the program
    userInputInt = int(userInput)

    # There is no need for checking if the number is more than a certain amount (ex. userInputInt >= 1) since Python interpreter checks line by line and not all lines at once
    # Should this be implemented in other programs, unexpected behaviour may occur
    if userInputInt == 0 :
        print("You have no library fines.")
    elif userInputInt <= 5 :
        print("Your library fine is:", userInputInt * 5)
    elif userInputInt <= 10 :
        print("Your library fine is:", userInputInt * 10)
    elif userInputInt <= 15 :
        print("Your library fine is:", userInputInt * 15)
    else :
        print("The book is past 15 days since the book is not returned to the library. Your library membership is cancelled.")

    # Break program when all tasks are complete
    break

# Announce program
print(
    """
================================================================
        
            Welcome to "Are You Even?" the game!
            To exit the program, just type "Exit."
        
================================================================
    """
)

while True :
    # Take user imput, ask for a number
    userInput = input("Enter any number: ")

    # First converts input to lowercase and checks if it is equal "exit"
    # This is needed for case insensitive inputs
    if userInput.lower() == "exit" :
        # Announce and exit program
        print("Goodbye and have a nice day!")
        sys.exit()

    # Checks if the string does not contain a digit
    if not userInput.isdigit() :
        # Announce incorrect input and go back to the start of the loop via continue
        print("Invalid input, try again.")
        continue

    # Should the other 2 checks are avoided, proceed converting string to integer
    # The checks make sure if the input is valid or the user decides to exit the program
    userInputInt = int(userInput)

    if userInputInt % 2 == 0 :
        print("The number is even!")
    else :
        print("The number is odd!")
    
    # Break program when all tasks are complete
    break

# Announce program
print(
    """
================================================================
        
            Welcome to Grade Calculator!
            To exit the program, just type "Exit."
        
================================================================
    """
)

# Declare a tuple list. This means that we won't be using the variables inside and the program will be memory efficient.
questions = (
    "Enter your Python mark: ",
    "Enter your Java mark: ",
    "Enter your Visual Studio mark: ",
    "Enter your game development mark: ",
    "Enter your C# mark: "
)

userInputInt = [
    0,
    0,
    0,
    0,
    0
]

while True :
    totalMarks = 0
    iteration = 0

    while iteration < 5 :
        # Take user input
        userInput = input(questions[iteration])

        # First converts input to lowercase and checks if it is equal "exit"
        # This is needed for case insensitive inputs
        if userInput.lower() == "exit" :
            # Announce and exit program
            print("Goodbye and have a nice day!")
            sys.exit()

        # Checks if the string does not contain a digit
        if not userInput.isdigit() :
            # Announce incorrect input and go back to the start of the loop via continue
            print("Invalid input, try again.")
            continue

        # Should the other 2 checks are avoided, proceed converting string to integer
        # The checks make sure if the input is valid or the user decides to exit the program
        userInputInt[iteration] = int(userInput)

        # Check if the input is over 100
        if userInputInt[iteration] > 100 :
            # Announce incorrect input and go back to the start of the loop via continue
            print("Grade is over 100 marks, try again.")
            continue

        totalMarks += userInputInt[iteration]

        iteration += 1

    # Calculate average
    average = totalMarks / 5

    # Set beginning grade to "Failed"
    grade = "Failed"

    # Check if all grades are above 50
    if userInputInt[0] >= 50 and userInputInt[1] >= 50 and userInputInt[2] >= 50 and userInputInt[3] >= 50 and userInputInt[4] >= 50 :
        # Check if grades are within the following critera A, B, C, D, and E in reverse order to go line by line with the interpreter
        if average <= 59 :
            grade = "Grade E"
        elif average <= 69 :
            grade = "Grade D"
        elif average <= 79 :
            grade = "Grade C"
        elif average <= 89 :
            grade = "Grade B"
        else :
            grade = "Grade A"
    else :
        # The else block of this code is actually useless since the starting variable can be set to "Failed" and there won't be a need for this block
        grade = "Failed"

    # Print results to user
    print(
        f"""

Your total mark is: {totalMarks}
Your average is: {average}
Your grade is: {grade}

        """
    )

    # Break program when all tasks are complete
    break