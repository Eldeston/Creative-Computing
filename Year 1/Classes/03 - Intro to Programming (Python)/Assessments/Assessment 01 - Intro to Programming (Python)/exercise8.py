# -------- Exercise 8 --------

# For sys.exit()
import sys

userList = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Announce program
print(
    """
================================================================

Welcome to "Wayfinder"
Search a name, or type "Exit."

================================================================
    """
)

# Do an example search in case sensitive
if "Sam" in userList :
    # Announce found user
    print("Sam is discovered on Wayfinder.")

# Keep programming running until user exits with a loop
while True :
    # Seek for user input. Change string to capitalized by default.
    userInput = input().capitalize()

    # If the input is "Exit," say goodbye and exit program.
    if userInput == "Exit" :
        print("Goodbye and have a nice day!")
        sys.exit()

    # Check if user input is in the list
    if userInput in userList :
        # Announce found user
        print(userInput, "is discovered on Wayfinder.")
        # Reset loop
        continue
    

    # Announce user is unknown
    print(userInput, "is an unknown name.")