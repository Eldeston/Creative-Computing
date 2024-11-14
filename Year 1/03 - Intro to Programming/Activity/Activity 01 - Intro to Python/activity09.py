# -------- Arithmetic Operator --------

# Announce program
print("================================ \n\nArithmetic Operator v3.0 **Premium Edition** \nTo enter numerical mode, enter \"Numerical\" \nTo enter logical mode, enter \"Logic\" \nTo enter bitwise mode, enter \"Bitwise\" \nTo exit, enter \"Exit.\" \n\n================================")

# Create a list of input questions
questionsInput = [
    "Enter first input: ",
    "Enter second input: "
]

# Initialize user inputs. It is usually "null."
userInputs = [
    "null",
    "null"
]

# Settings for modes, we will be using a switch case to change between modes
# 0 for numeric, 1 for logical, 2 for bitwise
switchMode = 0

# Keep program running until user exits
while True :
    i = 0

    # Create a loop that sorts through user inputs
    while i < 2 :
        # Loop through user input questions and assign user input
        userInputs[i] = input(questionsInput[i])

        # If the input is "exit," say goodbye and exit program.
        if userInputs[i].lower() == "exit" :
            print("Goodbye and have a nice day!")
            quit()
        
        # If the input is "logic," set switch mode to 0 and announce and jump to the start of the loop.
        if userInputs[i].lower() == "numeric" :
            switchMode = 0
            print(f"Mode has been set to numeric.")
            continue

        # If the input is "logic," set switch mode to 1 and announce and jump to the start of the loop.
        if userInputs[i].lower() == "logical" :
            switchMode = 1
            print(f"Mode has been set to logical.")
            continue

        # If the input is "logic," set switch mode to 2 and announce and jump to the start of the loop.
        if userInputs[i].lower() == "bitwise" :
            switchMode = 2
            print(f"Mode has been set to bitwise.")
            continue

        # Switch between modes using case
        # There is no need for switch case for bitwise as it accepts raw string input
        match switchMode :
            case 0 :
                # If the input contains invalid characters, announce and jump to the start of the loop
                # Here, we check for digits
                if not userInputs[i].isdigit() :
                    print("Invalid input, try again.")
                    continue

                # Convert input from string to integer
                userInputs[i] = int(userInputs[i])
            case 1 :
                # If the input contains invalid characters, announce and jump to the start of the loop
                # Here, we check for booleans
                if not (userInputs[i].lower() in ("true", "false")) :
                    print("Invalid input, try again.")
                    continue

                # Convert input from string to boolean
                userInputs[i] = bool(userInputs[i])
            case _ :
                # If the input contains invalid characters, announce and jump to the start of the loop
                # Here, we check for digits
                if not userInputs[i].isdigit() :
                    print("Invalid input, try again.")
                    continue

                # Convert input from string to integer
                userInputs[i] = int(userInputs[i])

        # Iterate
        i += 1

    # Finally, the meat of the program.
    match switchMode :
        case 0 :
            # Addition
            addition = userInputs[0] + userInputs[1]
            # Subtraction
            subtraction = userInputs[0] - userInputs[1]
            # Multiplication
            multiplication = userInputs[0] * userInputs[1]
            # Division
            division = userInputs[0] / userInputs[1]

            # Compare more than
            moreThan = userInputs[0] > userInputs[1]
            # Compare less than
            lessThan = userInputs[0] < userInputs[1]
            # Compare more than or equal
            moreThanEqual = userInputs[0] >= userInputs[1]
            # Compare less than or equal
            lessThanEqual = userInputs[0] <= userInputs[1]
            # Compare equal
            equal = userInputs[0] == userInputs[1]
            # Compare not equal
            notEqual = userInputs[0] != userInputs[1]

            # Print all results in one string with nultiline strings
            print(
                f"""
                    The result for addition is: {addition}
                    The result for subtraction is: {subtraction}
                    The result for multiplication is: {multiplication}
                    The result for division is: {division}

                    The result for more than is: {moreThan}
                    The result for less than is: {lessThan}
                    The result for more than or equal is: {moreThanEqual}
                    The result for less thann or equal is: {lessThanEqual}
                    The result for equal is: {equal}
                    The result for not equal is: {notEqual}
                """
            )
        case 1 :
            # And gate
            andGate = userInputs[0] and userInputs[1]
            # Or gate
            orGate = userInputs[0] or userInputs[1]
            # Not gate
            notGate = userInputs[0] != userInputs[1]

            # Print all results in one string with nultiline strings
            print(
                f"""
                    The result for AND gate is: {andGate}
                    The result for OR gate is: {orGate}
                    The result for NOT gate is: {notGate}
                """
            )
        case _ :
            # Bitwise and
            bitAnd = userInputs[0] & userInputs[1]
            # Bitwise or
            bitOr = userInputs[0] | userInputs[1]
            # Bitwise xor
            bitXor = userInputs[0] ^ userInputs[1]
            # Bitwise not
            # This uses one input as it inverses the bits
            bitNot = ~userInputs[0]

            # Print all results in one string with nultiline strings
            print(
                f"""
                    The result for bit AND is: {bitAnd}
                    The result for bit OR is: {bitOr}
                    The result for bit XOR is: {bitXor}
                    The result for bit NOT (single input) is: {bitNot}
                """
            )