# -------- Exercise 3 --------

# Note that we are using a consistent name format for all variables, known as camelCase.

# Initialize full name as a string
fullName = "Frem Fredric Baring Patalinghug"
# Intialize hometown as a string
homeTown = "Million Flowers"
# Intialize age as a string after converting from integer
age = str(20)

# For this one, I used the plus operator "+" and not comma as I needed the period to end each sentence.
# Note that I am using a backlash n "n" to print the following string on a new line
print("Your name is " + fullName + ". \nYour hometown is " + homeTown + ". \nYou are " + age + " years old.")

# -------- Advanced Requirements --------

# Ask user their full name
fullName = input("It is your turn, what is your full name?")
# Ask user their hometown
homeTown = input("Where is your hometown?")
# Ask user how old they are
age = input("How old are you?")

# Note that I am using the same variables. This is because the variables initialized are not constants. It does however replace the previous initialized data assigned to the variables.

# Finally, do the same thing as the last
print("Your name is " + fullName + ". \nYour hometown is " + homeTown + ". \nYou are " + age + " years old.")