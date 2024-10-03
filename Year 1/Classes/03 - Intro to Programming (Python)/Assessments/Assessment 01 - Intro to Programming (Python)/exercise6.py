# -------- Exercise 6 --------

# With new knowledge of dictionaries, I have gained a far higher power
# LET'S ACE THIS EXERCISE!

# For sys.exit()
import sys

# Announce program.
print("================================ \n\nWelcome to \"Stark Industries Archive!\" \nPlease enter the correct password to access your account \nTo exit the program, just type \"Exit.\" \n\n================================")

# Create a dictionary of users
users = {
    "\"Tony\" Stark" : "iAmIronMan",
    "Loki Laufeyson" : "forAllTimeAlways",
    "Thor Odinson" : "xXgodOfThunderXx",
    "Steve Rogers" : "peggyCarter1945"
}

while True :
    userInput = input("Enter a password to sign in with one of the accounts: ")

    if userInput in users.values() :
        print(f"Welcome back, {users[userInput]}.")

    print("Invalid password.")