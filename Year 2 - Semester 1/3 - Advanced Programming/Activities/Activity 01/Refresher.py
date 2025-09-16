import os
import time

# Clear function
def clearConsole() :
    # For windows, use "cls"
    if os.name == "nt" : os.system("cls")
    # For Linux/Mac, use "clear"
    else : os.system("clear")

# Clear console
clearConsole()

waitTime = float(input("Enter time in seconds for each iteration: "))
maxIterations = int(input("Enter maximum iteration: "))

# The simplest but also the memory intensive way
for i in range(1, maxIterations) :
    # Print current iteration
    print("Current iteration in integer is", i)
    # Wait for 1 second
    time.sleep(waitTime)
    # Clear console
    clearConsole()

# Least memory intensive
iterations = 0.0
while iterations < float(maxIterations) :
    # Advance
    iterations += 1.0
    # Print current iteration
    print("Current iteration in float is", iterations)
    # Wait for 1 second
    time.sleep(waitTime)
    # Clear console
    clearConsole()

# Checks the data type of iterations
print(f"After {maxIterations} iterations, the data type of iterations is", type(i))
print(f"After {maxIterations} iterations, the data type of iterations is", type(iterations))

secretTitle = "the adventures of sparta"

# This is an f-string
print(
    f'''
This is a multi-line string.
Reality can e whatever I want.

This is .title() in action.
{secretTitle.title() + " Part 2"}
    '''
)

secretMsg = "Ginisang mix is the best"

# This string has been sliced
print(secretMsg[0:6])
print(secretMsg[::-1])

# This string has been case converted
print(secretMsg.upper())
print(secretMsg.lower())
print(secretMsg.title())
print(secretMsg.capitalize())

secretMsg2 = "   what's up guys   "

# This message has been stripped of spaces
print(secretMsg2.upper())
print(secretMsg2.upper().strip())

# This message has been replaced
print(secretMsg.replace("Ginisang", "MagiSarap"))

slangs = "Skibidi, Ohio, Rizzler"

# Converts string to a list
slangs.replace(" ", "").split(",")

# Prints out the list
print(slangs.replace(" ", "").split(","))

# Joins items in a list to a string (Technical dificulties)
print(", ".join(slangs))

sampleMsg0 = "WHERE'S THE LAMB SAUCE???"
sampleMsg1 = "Engaging pulse engine in 5 seconds."
sampleMsg2 = "whispered message"

print(sampleMsg0.isalpha())
print(sampleMsg1.isdigit())
print(sampleMsg2.islower())