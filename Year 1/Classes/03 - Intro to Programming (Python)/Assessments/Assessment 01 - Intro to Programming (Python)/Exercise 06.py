# -------- Exercise 6 --------

# With new knowledge of dictionaries, I have gained a far higher power
# LET'S ACE THIS EXERCISE!

# For sys.exit()
import sys

# Announce program.
print(
    """
================================

Welcome to "Stark Industries!" 
Please enter the correct password to access your account
To exit the program, just type "Exit."

================================
    """
)

# Define password
passWord = "12345"

# Define attempt count
attemptCount = 5
# Define current attempt (will be used later for the loop to work)
currentAttempt = 0

# While current attempts remain below the attempt count, run the loop
while currentAttempt < attemptCount :
    # Ask for user input, this time not using a prompt
    userInput = input()

    # If the user inputs the correct password, break loop
    if userInput == passWord : break

    # Otherwise, add one failed attempt
    currentAttempt += 1

    # Announce incorrect password
    print(
        f"""
{userInput} is incorrect.
Current attempts: {currentAttempt}
        """
    )

# If the current attempt equals attempt count, announce maximum attempts reached and close program
if currentAttempt == attemptCount :
    print(attemptCount, "attempts has been reached. Closing program.")
    sys.exit()
# Otherwise, announce program welcome and continue with the program
else :
    print(
        """
================================

J.A.R.V.I.S.

Welcome home, Mr. Stark.

================================
        """
    )