# -------- Exercise 4 --------

"""
Concept code of inspiration

if(userAnswer == "France"):
    print("You are correct!")
else:
    print("You are wrong.")
"""

attempt = 3

while(attempt != 0):
    userAnswer = input("What is the capital of France?")

    if(userAnswer == "Paris"):
        break
    else:
        print("Wrong, please try again.")

    attempt -= 1

if(attempt == 0): print("You lost 3 attempts. \nGAME OVER! \nRun this program to try again!")
else: print("Congratulations! You are correct!")