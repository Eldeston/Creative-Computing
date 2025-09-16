import os
import time
import math

# This is a simple area and perimeter calculator for squares, rectangles, and circles
# Be aware that this program does not have any for of error handling from user input

# Store PI in a variable for later use and reduce memory usage
pi = math.pi

# Clear function
def clearConsole() :
    # For windows, use "cls"
    if os.name == "nt" : os.system("cls")
    # For Linux/Mac, use "clear"
    else : os.system("clear")

# Clear console
clearConsole()

# Square area function
def getAreaSquare(length) :
    return round(length * length, 2)

# Rectangle area function
def getAreaRect(width, height) :
    return round(width * height, 2)

# Circle area function
def getAreaCircle(radius) :
    return round(radius ** pi, 2)

# Square perimeter function
def getPerimeterSquare(length) :
    return round(length * 4, 2)

# Rectangle perimeter function
def getPerimeterRect(width, height) :
    return round((width + height) * 2, 2)

# Circle perimeter function
def getPerimeterCircle(radius) :
    return round(radius * pi, 2)

# Main loop
while True:
    # Clear console
    clearConsole()

    # Present user input menu
    userInput0 = input("Enter square, rectangle, and circle. Otherwise exit.\n").lower()
    
    # Check if square
    if userInput0 == "square" :
        userInput0 = input("Enter length: ")

        # Print function results
        print("Area of square is", getAreaSquare(float(userInput0)), "u²")
        print("Perimeter of square is", getPerimeterSquare(float(userInput0)), "u")

        # Wait for 2 second
        time.sleep(2)

        # Begin again
        continue
    
    # Check if rectangle
    if userInput0 == "rectangle" :
        userInput0 = input("Enter width: ")
        userInput1 = input("Enter height: ")

        # Print function results
        print("Area of rectangle is", getAreaRect(float(userInput0), float(userInput1)), "u²")
        print("Perimeter of rectangle is", getPerimeterRect(float(userInput0), float(userInput1)), "u")

        # Wait for 2 second
        time.sleep(2)

        # Begin again
        continue
    
    # Check if circle
    if userInput0 == "circle" :
        userInput0 = input("Enter radius: ")

        # Print function results
        print("Area of circle is", getAreaCircle(float(userInput0)), "u²")
        print("Perimeter of circle is", getPerimeterCircle(float(userInput0)), "u")

        # Wait for 2 second
        time.sleep(2)

        # Begin again
        continue
    
    # Check if exit
    if userInput0 == "exit" :
        break

    # Clear console
    clearConsole()

    # If none of the options are selected, inform the user of invalid input
    print("Invalid input.")

    # Wait for 1 second
    time.sleep(1)