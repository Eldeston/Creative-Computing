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

# Announce beginning of advanced requirements
print(
    """
---------------- Advanced Requirements ----------------
    """
)

# Announce the user's turn
print("Now it is your turn.")

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
    # If the loop reaches "age," do an additional check if the containing data is a digit
    if data == "age" :
        # Run the loop forever until it reaches a break
        while True :
            # Ask the user for their data (in this case it is "age")
            biography[data] = input(f"What is your {data}?")

            # Check if the input contains a digit, then break loop
            if biography[data].isdigit() : break
            
            # Otherwise, announce invalid input and go back to the start of the loop
            print("Invalid input, please enter a digit")

        # Skip loop
        continue

    # Run the loop forever until it reaches a break
    while True :
        # Ask user their data
        biography[data] = input(f"What is your {data}?")

        # If data contains actual data, break loop
        if not biography[data] == "" : break

        # Otherwise, announce empty input and go back to the start of the loop
        print("Empty input, please make an entry")

# Print final results
print(
    f"""
My name is {biography["first name"] + " " + biography["last name"]}.
My hometown is {biography["hometown"]}.
I am {biography["age"]} years old.
    """
)