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
passWord = "iAmIronMan"

attemptCount = 5
currentAttempt = 0

while currentAttempt < attemptCount :
    userInput = input()

    if userInput == passWord : break

    currentAttempt += 1

    print(
        f"""
Your password is incorrect.
Current attempts: {currentAttempt}
        """
    )

if currentAttempt == attemptCount : print(attemptCount, "attempts has been reached. Closing program.")
else :
    print(
        """
================================

J.A.R.V.I.S.

Welcome home, Mr. Stark.

================================
        """
    )