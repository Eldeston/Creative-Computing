# -------- Exercise 7 --------

# This one is easy, it's just counting with loops

print(
    """
Beginning iteration: 0
Ending iteration: 50
Step size: 1
    """
)

# Starting iteration
currentIteration = 0
# Keep loop running while current iteration is below or equal to 50
while currentIteration <= 50 :
    # Print current iteration
    print(currentIteration)
    # Step forward by 1
    currentIteration += 1

print(
    """
Beginning iteration: 50
Ending iteration: 0
Step size: -1
    """
)

# Starting iteration
currentIteration = 50
# Keep loop running while current iteration is more than or equal to 0
while currentIteration >= 0 :
    # Print current iteration
    print(currentIteration)
    # Step backward by 1
    currentIteration -= 1

print(
    """
Beginning iteration: 30
Ending iteration: 50
Step size: 1
    """
)

# Starting iteration
currentIteration = 30
# Keep loop running while current iteration is below or equal to 50
while currentIteration <= 50 :
    # Print current iteration
    print(currentIteration)
    # Step forward by 1
    currentIteration += 1

print(
    """
Beginning iteration: 50
Ending iteration: 10
Step size: -2
    """
)

# Starting iteration
currentIteration = 50
# Keep loop running while current iteration is more than or equal to 10
while currentIteration >= 10 :
    # Print current iteration
    print(currentIteration)
    # Step backward by 2
    currentIteration -= 2

print(
    """
Beginning iteration: 100
Ending iteration: 200
Step size: 5
    """
)

# Starting iteration
currentIteration = 100
# Keep loop running while current iteration is below or equal to 200
while currentIteration <= 200 :
    # Print current iteration
    print(currentIteration)
    # Step forward by 5
    currentIteration += 5