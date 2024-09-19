"""

ACTIVITIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIEEEEEEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

"""

# -------- Getting Pragram Information --------

# Import code packages
import sys
import datetime

# Print Python version information
print("Python Version: \n" + sys.version)
print(sys.version_info)

# Get time data
timeData = datetime.datetime.now()

# Print date and time
print("Current date and time: \n" + timeData.strftime("%Y-%m-%d %H:%M:%S"))

# -------- Printing Exercise 1 --------

# Declaration of strings
studentName = "Frem"
studentPenName = "Eldeston"
# Declaration of an integer
studentAge = 20
# Declaration of a complex
studentCode = 20j + 2004j
# Declaration of a float
studentHeight = 5.3
studentWeight = 60.4
# Declaration of a boolean
studentIsMeta = True

# Declaration of a tuple
studentParents = ("Milfred", "Mechan")
# Declaration of a list
studentSiblings = ["Maudric", "Faith", "Mikhyla"]
# Declaration of a set
studentHobbies = {"Programming", "Games"}
# Declaration of a frozenset
studentSubjects = ({"Digital Visual Design", "Digital Storytelling", "Introduction to Programming (Python)"})

# Declaration of a byte
variableByte = b"This is a decrypted message."
# Declaration of a byte array
variableArray = bytearray(5)
# Declaration of a memory view
variableMemoryView = memoryview(bytes(5))

# Print the results
# Inside this first print function, it combines the strings via the plus operator "+"
print("Hi I'm " + studentName + ", and my penname is " + studentPenName + ". I am " + str(studentAge) + " years old and live in Sharjah. \nI am a shader developer who developed Super Duper Vanilla. \nSubscribe to Frem Patalinghug on YouTube!")

# This is a comment.
# Reality can be whatever I want. -Thanos

# -------- Printing Exercise 2 --------

# Print the results
# This is an example print involving the use of backslash "\" to recognize the character " as part of a string and a new line "\n" to print to a new line
print("He said, \"JavaScript is \nawesome\" I replied, \n'Python is more awesome'")

# Um aktually I love C++.

# -------- Calculating Products --------

# User input 3 multipliers
num1 = int(input("Enter your first number."))
num2 = int(input("Enter your second number."))
num3 = int(input("Enter your last number."))
# Calculate the product
product1 = num1 * num2 * num3

# Print results
print("You will die in " + str(product1) + " years. \nJust kidding, your product is " + str(product1) + ".")

# -------- Calculating Area of Circle --------

# Function for calculating the area of a circle
def getCircleArea(radius):
    return 3.1415 **radius

# User inputs circle radius
circleRadius = float(input("Enter the radius of your circle."))

# Print results
print("The area of a circle with a radius of " + str(circleRadius) + " is " + str(getCircleArea(circleRadius)) + ".")

# -------- Experimental Zone --------

# This is a basic question and answer code
# We will start with a base string and add along some sentences along the way as we ask the user some questions
baseString = "Your name is "

# Ask user name
userName = input("What is your name?")
# Add string
baseString += userName + ". "

# Ask if user has a penname
userPenNameBool = input("Do you have a penname?")
# Check if yes (with both case sensitive options)
if userPenNameBool == "Yes" or userNickNameBool == "yes" or userNickNameBool == "YES":
    # Ask user penname
    userPenName = input("Please tell me your penname.")
    # Add string
    baseString += "Your penname is " + userPenName + ". "

# Ask if user has a nickname
userNickNameBool = input("Do you have a nickname?")
# Check if yes (with both case sensitive options)
if userNickNameBool == "Yes" or userNickNameBool == "yes" or userNickNameBool == "YES":
    # Ask user nickname
    userNickName = input("Please tell me your nickname.")
    # Add string
    baseString += "Your nickname is " + userNickName + ". "

# Ask user age
userAge = int(input("What is your age?"))
# Add last string
baseString += "You are " + str(userAge) + " years old."

# Print final results
print(baseString)

# -------- Junk --------

thisIsString = "Are you a developer because you can code or you can code because you are a developer? Always bet on green."
thisIsInteger = 1984
thisIsBoolean = True

if(thisIsBoolean):
    print(thisIsString + " " + str(thisIsInteger) + ".")
else:
    print("thisIsConditional")
    
# camelCase is superior.

def basicFunction():
    return 12

test=12
print("testing", test ,"this thing")