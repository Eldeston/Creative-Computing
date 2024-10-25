# -------- Exercise 3 --------

# Note that we are using a consistent variable name format for all variables, this is known as camelCase.

# Create a dictionary containing a biography for Frem
# All keys and values are strings
biography = {
    "full name" : "Frem Fredric Baring Patalinghug",
    "hometown" : "Million Flowers",
    "age" : "20"
}

# For this one, I used 3 double quotes to use multiple lines and used the f-string to conveniently use variables in a string using a brackets
print(
    f"""
    My name is {biography["full name"]}.
    My hometown is {biography["hometown"]}.
    I am {biography["age"]} years old.
    """
)

# -------- Advanced Requirements --------

# Create a dictionary containing a biography for the user
# All keys and values are strings

# We are going to ask the user their info
# For now, we will keep the dictionary empty
biography = {
    "first name" : "",
    "last name" : "",
    "hometown" : "",
    "age" : ""
}

# Loop through the biography dictionary through a variable "data"
for data in biography :
    if data == "age" :
        while True :
            biography[data] = input(f"What is your {data}?")

            if biography[data].isdigit() : break

            print("Invalid input, please entera digit")

    biography[data] = input(f"What is your {data}?")

print(
    f"""
    My name is {biography["first name"] + " " + biography["first name"]}.
    My hometown is {biography["hometown"]}.
    I am {biography["age"]} years old.
    """
)