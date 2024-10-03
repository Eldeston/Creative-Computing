# -------- Exercise 3 --------

# Note that we are using a consistent variable name format for all variables, this is known as camelCase.

# Create a dictionary containing a biography for Frem
# All keys and values are strings
biography = {
    "fullName" : "Frem Fredric Baring Patalinghug",
    "homeTown" : "Million Flowers",
    "age" : "20"
}

# For this one, I used 3 double quotes to use multiple lines and used the f-string to conveniently use variables in a string using a brackets
print(
    f"""
    My name is {biography["fullName"]}.
    My hometown is {biography["homeTown"]}.
    I am {biography["age"]} years old.
    """
)

# -------- Advanced Requirements --------

# Create a dictionary containing a biography for the user
# All keys and values are strings

# We are going to ask the user their info
# In this one, we can use the input() function inside a dictionary
biography = {
    "fullName" : input("It is your turn, what is your full name? "),
    "homeTown" : input("Where is your hometown? "),
    "age" : input("How old are you? ")
}

# Note that I am using the same dictionary. This is because the variables initialized are not constants. It does however replace the previous initialized data assigned to the variables.

# Finally, do the same print message as the last
print(
    f"""
    Your name is {biography["fullName"]}.
    Your hometown is {biography["homeTown"]}.
    You are {biography["age"]} years old.
    """
)