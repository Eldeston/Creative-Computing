"""

ACTIVITIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIEEEEEEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

"""

import sys
import datetime

# Python version information
print("Python Version: \n" + sys.version)
print(sys.version_info)

timeData = datetime.datetime.now()

print("Current date and time: \n" + timeData.strftime("%Y-%m-%d %H:%M:%S"))

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

# Print the results
# This is an example print involving the use of backslash "\" to recognize the character " as part of a string and a new line "\n" to print to a new line
print("He said, \"JavaScript is \nawesome\" I replied, \n'Python is more awesome'")

# Um aktually I love C++.

num1 = int(input("Enter your first number."))
num2 = int(input("Enter your second number."))
num3 = int(input("Enter your last number."))
product1 = num1 * num2 * num3

print("You will die in " + str(product1) + " years. \nJust kidding, your product is " + str(product1) + ".")

def getCircleArea(radius):
    return 3.1415 **radius

circleRadius = float(input("Enter the radius of your circle."))

print("The area of a circle with a radius of " + str(circleRadius) + " is " + str(getCircleArea(circleRadius)) + ".")

# -------- Experimental Zone --------

baseString = "Your name is "

userName = input("What is your name?")
baseString += userName + ". "

userPenNameBool = input("Do you have a penname?")
userNickNameBool = input("Do you have a nickname?")

if userPenNameBool == "Yes":
    userPenName = input("Please tell me your penname.")
    baseString += "Your penname is " + userPenName + ". "
if userNickNameBool == "Yes":
    userNickName = input("Please tell me your nickname.")
    baseString += "Your nickname is " + userNickName + ". "

userAge = int(input("What is your age?"))
baseString += "You are " + str(userAge) + " years old."

print(baseString)



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