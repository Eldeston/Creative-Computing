# -------- Exercise 4 --------

# Announce the game
print("Let's play a game! You have 3 attempts. Your answers will be case sensitive.")

# Initialize variable for counting remaining attempts. The user is given 3 attempts.
attempt = 3

# While the attempt count remained 0, run the following code.
while attempt != 0 :
    # Ask user the question for input
    userAnswer = input("What is the capital of France? ")

    # Check if user guessed correctly. Break the loop if they guessed right.
    if userAnswer == "Paris" : break
    # Otherwise, we tell the user their answer is arong and how many attempts they have left. For display reasons, we subtract 1.
    else : print("Your answer", userAnswer, "is wrong. You have", str(attempt - 1), "attempts.")

    # If user is wrong, take away 1 attempt. This line is ignored when break is used.
    attempt -= 1

# Check if user has 0 attempts. Display game over message and exit Python with quit().
if attempt == 0 :
    print("You lost all 3 attempts. \nGAME OVER! \nRun this program to try again!")
    quit()
# If the user guessed correctly, display remaining attempts.
else: print("Congratulations! You are correct! You guessed in", str(attempt), "attempt(s).")

# ---------------- Advanced Requirements ----------------

# NOW LETS GET THIS PARTY STARTED
# Announce beginning of advanced requirements
print(
    """
---------------- Advanced Requirements ----------------
    """
)

# Announce a new game
print("Let's play another game! You have 10 attempts. Your answers will be case insensitive.")

# This time we give the user 10 attempts
attempt = 10

# I will say however, coding this is rather difficult to get if you don't know everything.
# Thanks to my previous experience with programming (namely with shader programs in C syntax), the time has been cut down to find the functions I need.

# Initialize a list for defining countries
countries = ["Ukraine", "Switzerland", "Kazakhstan", "Russia", "France"]
# Initialize another list for capitals
capitals = ["Kyiv", "Bern", "Seoul", "Astana", "Paris"]

# zip() allows to iterate over several lists in parallel.
# In this case iterates city to countries and capital to capitals
for city, capital in zip(countries, capitals) :
    while attempt != 0 :
        # Ask user the question for input
        userAnswer = input("What is the capital of " + city + "? ")

        # Check if user guessed correctly. Break the loop if they guessed right.
        # We will use str.lower() to transform BOTH strings to lower case. We do not need to check for every posible case sensitive string which is rather time consuming and inefficient.
        # Great hack, not gonna lie
        if userAnswer.lower() == capital.lower() :
            # Announce correct answer
            print("You are correct!")
            # Break loop and continue to the next question
            break

        # Otherwise, we tell the user their answer is arong and how many attempts they have left.
        # We do not need to use an else statement as the loop is designed to break if the correct answer is used

        # Take away 1 attempt
        attempt -= 1

        # Announce the statement
        print("Your answer", userAnswer, "is wrong. You have", str(attempt), "attempts.")

# Check if user has 0 attempts. Display game over message. There is no need to exit Python as this is the end of the line.
if attempt == 0 : print("You lost all 10 attempts. \nGAME OVER! \nRun this program to try again!")
# If the user guessed correctly, display remaining attempts.
else: print("Congratulations! You guessed in", str(attempt), "attempt(s).")

# One more thing to note, do NOT forget to add parentheses "()" to ANY function. It's a rookie mistake and it tooke me HOURS to debug "WHY IS THIS STRING NOT TOKYO??!?!?!??""