# Step size. Determines the increment size for the number loop.
steps = 1
# Number of iterations. Determines how many times the loop will iterate.
iterations = 50
# Break iteration. Determines when the iteration breaks.
breakIteration = 44
# Continue iteration. Determines when the iteration continues.
continueIteration = 9

# Current iterations. Stores the current iteration during the loop.
currentIteration = 0
# Loop while currentIteration is less than iteration
while currentIteration < iterations :
    # Step forward
    currentIteration += steps
    # Check if it meets break condition
    if currentIteration == breakIteration :
        break
    # Check if it meets break condition
    if currentIteration == continueIteration :
        continue
    # Print current iteration
    print(currentIteration)
# The else conditiion used here is utterly useless but is used regardless
else :
    # End of loop
    print("Loop complete")

# Ask user for the table multiplier
tableMultiplier = int(input("Enter table multiplier: "))
# Ask user for the table range
tableRange = int(input("Enter table range: "))

# Current iterations. Stores the current iteration during the loop.
currentIteration = 0
# Loop while currentIteration is less than tableRange
while currentIteration < tableRange :
    # Step forward
    currentIteration += 1
    # Print table with the end result as currentIteration multiplied by the tableMultiplier
    print(currentIteration, "*", tableMultiplier, "=", currentIteration * tableMultiplier)

# Ase user for the factorial
factorial = int(input("Enter factorial range: "))

# Current iterations. Stores the current iteration during the loop.
currentIteration = 0
# Current factorial. Stores the current factorial during the loop.
currentFactorial = 1
# Loop while currentIteration is less than factorial
while currentIteration < factorial :
    # Step forward
    currentIteration += 1
    # Multiply the current factorial
    currentFactorial *= currentIteration
    # Preint the factorial table
    print("The factorial of", currentIteration, "is:", currentFactorial)

# Simplified edition of 
for i in range(0, 20, 1) :
    print(i)

for i in range(3) :
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    result = a * b * c
    print(result)

# Create a list of fruits
fruitList = ["Apple", "Bannana", "Optimus Prime", "Mango", "Cherry", "Grapes"]

# Iterate through the list
for iteration in fruitList :
    print(iteration)

    # Check if the iteration contains a specific string
    if iteration == "Optimus Prime" :
        # Break the loop
        break

adjectiveList = ["Red", "Green", "Big", "Sentinel", "Tasty", "Juicy"]

for iterationX in adjectiveList :
    for iterationY in fruitList :
        print(iterationX, iterationY)

for iterationX in range(1, 11) :
    for iterationY in range(1, 11) :
        print(iterationX * iterationY, end = " ")
    print()

def callValue() :
    return "Yoink!"

def callReference() :
    print("Yoink!")

print(callValue())
callReference()

def favoriteFilm(title) :
    print("You favorite film is", title)

favoriteFilm(input("Enter favorite film: "))