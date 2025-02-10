# Define PI accurate to 6 digits
pi = 3.14156

# Define function for calculating area of circle
def getCircleArea(radius) :
    return pi * radius ** 2

# Keep loop running forever until break or exit
while True :
    # Listen for user input
    userInput = input("Enter radius: ")

    # Check if the input is "exit"
    # Set user input to lowercase to accept case insensitive inputs
    if userInput.lower() == "exit" :
        # Announce program exit
        print("Goodbye and have a nice day.")
        # Exit program
        quit()

    # Check if the input is NOT a digit using .isdigit()
    if not userInput.isdigit() :
        # Announce incorrect input
        print("Incorrect input.")
        # Reset loop
        continue

    # Otherwise use function
    area = getCircleArea(int(userInput))

    # Print results
    print("Area of a circle with a radius of", userInput, "is", area)