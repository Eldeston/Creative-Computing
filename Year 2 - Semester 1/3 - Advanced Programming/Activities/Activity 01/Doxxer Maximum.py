import os
import time

# Clear function
def clearConsole() :
    # For windows, use "cls"
    if os.name == "nt" : os.system("cls")
    # For Linux/Mac, use "clear"
    else : os.system("clear")

currList = []

while True :
    clearConsole()

    userInput = input("Give me your location credatials, there is no escape.\n")

    if userInput.lower() == "escape" : break

    if userInput.lower() == "extract" :
        print("Well done junior hacker, here is the extracted data:\n")
        print(currList)

        # Wait for 1 second
        time.sleep(2)

    currList += [userInput]

    print(userInput, "entered. Again.")

    # Wait for 1 second
    time.sleep(2)

print("You\'ve betrayed me junior hacker. Now you will never see the light of day ever again.")