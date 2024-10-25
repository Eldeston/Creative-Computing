# -------- Exercise 10 --------

# For sys.exit()
import sys

# Create a new function checking if the number is odd
def isOdd(x) :
    # Convert input to integer
    # Check if modulo equals 0 and return as boolean
    return int(x) % 2 == 0

# Create main function
def main() :
    # Keep programming running until user exits with a loop
    while True :
        # Ask user for number
        userInput = input("Enter number: ")

        # Check if the input is "exit"
        # The user input is first converted to lowercase then checks if it contains the string "exit"
        if userInput.lower() == "exit" :
            print("Goodbye and have a nice day!")
            sys.exit()

        # Check if the input is not a digit
        if not userInput.isdigit() :
            print("Invalid input.")
            continue

        # Check if the numbder is odd
        # If the number is odd, announce the number is even
        # This is because we are looking if there are remainders left over
        if isOdd(userInput) : print("The number", userInput, "is even.")
        # Otherwise announce the number is odd
        else : print("The number", userInput, "is odd.")

# __name__ determines the context of the program which in this case is the main line.
if __name__ == "__main__":
    # Call on the function main()
    main()