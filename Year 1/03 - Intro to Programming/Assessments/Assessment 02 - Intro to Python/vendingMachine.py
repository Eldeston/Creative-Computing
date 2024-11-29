# Announce program
print(
    """
----------------------------------------------------------------

Vending Machine
Version 2.0

----------------------------------------------------------------
    """
)

# Declare current cash
currentCash = 0.0

# Declare item stock
itemStock = [
    {
        "Name" : "Coca Cola",
        "Stock" : 10,
        "Price" : 3.0
    },
    {
        "Name" : "Pepsi",
        "Stock" : 10,
        "Price" : 3.0
    },
    {
        "Name" : "Water",
        "Stock" : 10,
        "Price" : 3.0
    }
]

# Input to integer function, default input argument set to ""
def inputToInteger(prompt = "") :
    # Run under an infnite loop until return to exit function
    while True :
        # Input prompt
        userInput = input(prompt)

        # Checks if the input is a digit
        if userInput.isdigit() :
            # Convert string to integer and return output
            return int(userInput)

        # Announce incorrect input
        print("\nInvalid input.")

# Input to float function, default input argument set to ""
def inputToFloat(prompt = "") :
    # Run under an infnite loop until return to exit function
    while True :
        # Input prompt
        userInput = input(prompt)

        # Removes decimals once to check if the string is a digit
        if userInput.replace('.', '', 1).isdigit() :
            # Convert string to float and return output
            return float(userInput)

        # Announce incorrect input
        print("\nInvalid input.")

# Display stock function
def displayStock() :
    # Display top header
    print("----------------------------------------------------------------\n")
 
    # Display current stock using a loop
    for index, properties in enumerate(itemStock) :
        print(f"ID: {index}, Name: {properties["Name"]}, Stock: {properties["Stock"]}, Price: {properties["Price"]}")

    # Display bottom header
    print("\n----------------------------------------------------------------")

# Insert cash function
def insertCash() :
    # Access currentCash as a global variable
    global currentCash

    # Ask user cash input
    userCash = inputToFloat("\nEnter cash: ")

    # Insert cash
    currentCash += userCash

    # Announce amount inserted
    print("\nInserted", "AED", userCash)

# Purchase stock function
def purchaseStock() :
    # Access currentCash as a global variable
    global currentCash

    # Ask user item ID input
    itemID = inputToInteger("\nEnter item ID: ")

    # Check if item ID does not exists
    if itemID not in range(len(itemStock)) :
        # Announce item ID does not exist
        print("\nItem ID does not exist.")
        # Exit function
        return

    # Ask user stock amount
    stock = inputToInteger("\nEnter item amount: ")

    # Check if item stock is insufficient
    if itemStock[itemID]["Stock"] < stock :
        # Announce insufficient item stock
        print("\nInsufficient item stock.")
        # Exit function
        return

    # Calculate total price by multiplying item price and stock
    totalPrice = itemStock[itemID]["Price"] * stock

    # Check if the user has insufficient funds.
    if totalPrice > currentCash :
        # Announce insufficient cash
        print("\nInsufficient cash.")
        # Exit function
        return

    # If all checks are valid, subtract current cash by total price
    currentCash -= totalPrice
    # Subtract current stock by stock requested
    itemStock[itemID]["Stock"] -= stock

    # Announce items purchased
    print(f"Purchased {stock} {itemStock[itemID]["Name"]} for AED {totalPrice}")

# Core of the program
# Run under an infnite loop until program exit
while True :
    # Announce current cash stored
    print(f"Current cash stored: AED {currentCash}\n")

    # Display stock
    displayStock()

    # Display available user options and ask user for input
    # Set output string to all lowercase allowing for case insensitive inputs
    userInput = input("\nType \"Insert\" to insert cash, \"Purchase\" to purchase items, or \"Exit\" to exit machine.\n").lower()

    # Check if user types "Insert"
    if userInput == "insert" :
        # Announce inserting cash
        print("\nInserting cash...")
        # Insert cash
        insertCash()
        # Reset loop
        continue

    # Check if user types "Purchase"
    if userInput == "purchase" :
        # Announce purchasing items
        print("\nPurchasing items...")
        # Purchase stock
        purchaseStock()
        # Reset loop
        continue

    # Check if user types "Exit"
    if userInput == "exit" :
        # Announce program exit
        print("\nGoodbye and have a nice day!")
        # Exit program
        quit()
    
    # If for some reason all inputs are not one of the above, announce invalid input
    print("Invalid input.")