# Import os, used to clear console
import os
# Import time, used to time animations and utilize delays
import time

# ---------------------------------------------------------------- # Debugging Settings # ---------------------------------------------------------------- #

# Display console
displayConsole = False

# Define common durations
longDuration = 8
normalDuration = 4
shortDuration = 2

# Declare user cash
userCash = 0.0
# Declare store cash
machineProfit = 0.0

# Declare user reciept
userReceipt = []
# Declare receipt history
machineHistory = []

# Declare item stock
itemStock = [
    {
        "Name" : "Coca Cola",
        "Stock" : 16,
        "Price" : 3.0
    },
    {
        "Name" : "Pepsi",
        "Stock" : 16,
        "Price" : 3.0
    },
    {
        "Name" : "Miranda",
        "Stock" : 16,
        "Price" : 3.0
    },
    {
        "Name" : "Fanta",
        "Stock" : 16,
        "Price" : 3.0
    },
    {
        "Name" : "Water",
        "Stock" : 16,
        "Price" : 1.0
    }
]

# ---------------------------------------------------------------- # Display Functions # ---------------------------------------------------------------- #

# Clear console function
def clearConsole() :
    # If display console is enabled
    if displayConsole : return
    # Check if the OS is Linux and use "clear instead"
    os.system("cls" if os.name == "nt" else "clear")

# Text animation function
def textAnimation(prompt = "Loading...", duration = shortDuration) :
    # Find the number of iterations based on the length of the string
    iterations = len(prompt)
    # This makes sure the loading bar will stop at a specified duration
    # timeStep / timeLength = 1 / iterations
    # timeStep = timeLength / iterations
    timeStep = duration / iterations
    # Run loop through set iterations
    for iterations in range(iterations) :
        # Loop through the prompt and iterate
        print(prompt[iterations], end = "")
        # Wait until specified duration
        time.sleep(timeStep)

# Loading animation function
def loadingAnimation(prompt = "Loading...", duration = shortDuration, iterations = 64) :
    # Announce prompt
    print(prompt)
    # Reuse text animation as a loading bar because I'm lazy lol
    textAnimation("████████████████████████████████████████████████████████████████", duration)

# ---------------------------------------------------------------- # Common Functions # ---------------------------------------------------------------- #

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

# Converts input to lower case
def inputLower(prompt = "") :
    return input(prompt).lower()

# ---------------------------------------------------------------- # Admin Functions # ---------------------------------------------------------------- #

# Withdraw profit function
def withdrawProfit() :
    # Access machineProfit as a global variable
    global machineProfit

    # Announce withdrawal
    loadingAnimation(f"Withdrawing AED {machineProfit}...")

    # Set profit to 0.0
    machineProfit = 0.0

    # Announce stock successfuly added
    print("\nProfits successfully withdrawn.")

# Add stock
def addStock() :
    # Access itemStock as a global variable
    global itemStock

    # Enter item name
    userItemName = input("Enter item name: ")

    # Enter item stock
    userItemStock = inputToInteger("\nEnter item stock: ")

    # Enter item price
    userItemPrice = inputToFloat("\nEnter item price: ")

    # Add new stock
    itemStock += [
        {
            "Name" : userItemName,
            "Stock" : userItemStock,
            "Price" : userItemPrice    
        }
    ]

    # Announce stock successfuly added
    print("\nStock successfuly added.")

# Remove stock
def removeStock() :
    # Access itemStock as a global variable
    global itemStock

    # Enter item index
    itemIndex = inputToInteger("\nEnter item stock: ")

    # Remove item
    del itemStock[itemIndex]

    # Announce stock successfuly added
    print("\nStock successfuly removed.")

# Machine history function
def viewHistory() :
    # Access machineHistory as a global variable
    global machineHistory

    # Get machineHistory length
    receiptLength = len(machineHistory)

    # Check if recentReceipt is empty
    if receiptLength == 0 :
        # Announce recentReceipt is empty
        print("History is empty.")
        # Exit function
        return
    
    # This makes sure the loading bar will stop at a specified duration
    # timeStep / timeLength = 1 / iterations
    # timeStep = timeLength / iterations
    timeStep = shortDuration / receiptLength
    
    # Show machineHistory in a loop
    for index in range(receiptLength) :
        print(machineHistory[index])
        # Wait until specified duration
        time.sleep(timeStep)
    
    # Ask user to enter to continue
    textAnimation("\nPress enter to continue...")
    # This is for responding to prompt
    input()

# ---------------------------------------------------------------- # Admin Interface # ---------------------------------------------------------------- #

# Admin interface function
def adminInterface() :
    # Access machineHistory as a global variable
    global machineHistory

    while True :
        # Clear current console
        clearConsole()
        
        # Display admin interface
        print(
            f"""
    ___       __          _          ____      __            ____              
   /   | ____/ /___ ___  (_)___     /  _/___  / /____  _____/ __/___ _________ 
  / /| |/ __  / __ `__ \/ / __ \    / // __ \/ __/ _ \/ ___/ /_/ __ `/ ___/ _ \\
 / ___ / /_/ / / / / / / / / / /  _/ // / / / /_/  __/ /  / __/ /_/ / /__/  __/
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/  /___/_/ /_/\__/\___/_/  /_/  \__,_/\___/\___/ 

----------------------------------------------------------------

Machine profits: AED {machineProfit}
Machine history: {len(machineHistory)}
            """
            )

        # Display stock
        displayStock()

        # Display available user options and ask user for input
        textAnimation("\nType \"Withdraw\" to withdraw profits, \"Add\" to add new stock, \"Remove\" to remove stock, \"History\" to view history, or \"Exit\" to exit interface.\n")

        # Set output string to all lowercase allowing for all selections will be case insensitive
        userInput = inputLower()

        # Check if user types "withdraw"
        if userInput == "withdraw" :
            # Announce withdrawing profits
            print("Withdrawing profits...\n")
            # Record withdrawing profits
            machineHistory += ["Admin: withdrawing profits."]
            # Withdraw profit
            withdrawProfit()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "add"
        if userInput == "add" :
            # Announce adding stock
            print("Adding stock...\n")
            # Record adding stock
            machineHistory += ["Admin: adding stock."]
            # Add stock
            addStock()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "remove"
        if userInput == "remove" :
            # Announce removing stock
            print("Removing stock...\n")
            # Record adding stock
            machineHistory += ["Admin: removing stock."]
            # Remove stock
            removeStock()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue
    
        # Check if user types "history"
        if userInput == "history" :
            # Announce viewing history
            print("Viewing history...\n")
            # Record viewing history
            machineHistory += ["Admin: viewing history."]
            # View history
            viewHistory()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "exit"
        if userInput == "exit" :
            # Announce exiting interface
            print("Exiting interface...")
            # Record exiting interface
            machineHistory += ["Admin: exiting interface."]
            # Exit function
            return

# Admin mode function
def adminAccess() :
    # Access machineHistory as a global variable
    global machineHistory

    # Case sensitive input
    userInput = input("Enter password: ")

    # Check if password is correct
    if userInput == "nahIdWin" :
        # Announce access grants
        print("\nAccess granted.")
        # Record admin access
        machineHistory += ["Admin interface accessed."]
        # Enter admin interface
        adminInterface()
        # Exit function
        return
    
    # Announce invalid password and exit
    print("\nAccess denied.")

# ---------------------------------------------------------------- # Vending Machine Functions # ---------------------------------------------------------------- #

# Display stock function
def displayStock() :
    # Display top header
    print("----------------------------------------------------------------\n")
 
    # Display current stock using a loop
    for index, properties in enumerate(itemStock) :
        # Display item properties
        print(f"ID: {index}, Name: {properties["Name"]}, Stock: {properties["Stock"]}, Price: {properties["Price"]}")
        # Wait for a set amount of time
        time.sleep(0.0625)

    # Display bottom header
    print("\n----------------------------------------------------------------")

# Insert cash function
def insertCash() :
    # Access userCash as a global variable
    global userCash
    # Access userReceipt as a global variable
    global userReceipt

    # Ask user cash input
    userInput = inputToFloat("Enter cash:\n")

    # Insert cash
    userCash += userInput

    # Make a recent receipt
    recentReceipt = f"Inserted AED {userInput}."
    # Record recent receipt as list
    userReceipt += [recentReceipt]

    # Announce amount inserted
    print(recentReceipt)

# Purchase stock function
def purchaseStock() :
    # Access userCash as a global variable
    global userCash
    # Access machineProfit as a global variable
    global machineProfit

    # Access userReceipt as a global variable
    global userReceipt
    # Access machineHistory as a global variable
    global machineHistory

    # Ask user item ID input
    itemID = inputToInteger("Enter item ID: ")

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
    if totalPrice > userCash :
        # Announce insufficient cash
        print("\nInsufficient cash.")
        # Exit function
        return

    # If all checks are valid, subtract current cash by total price
    userCash -= totalPrice
    # Add total price to storePrice
    machineProfit += totalPrice

    # Subtract current stock by stock requested
    itemStock[itemID]["Stock"] -= stock

    # Make a recent receipt
    recentReceipt = f"Purchased {stock} {itemStock[itemID]["Name"]} for AED {totalPrice}."

    # Record recent receipt as list
    userReceipt += [recentReceipt]
    # Record recent receipt for history
    machineHistory += [recentReceipt]

    # Announce recent receipt
    print("\n" + recentReceipt)

# Show receipt function
def showReceipt() :
    # Access userReceipt as a global variable
    global userReceipt

    # Get userReceipt length
    receiptLength = len(userReceipt)

    # Check if recentReceipt is empty
    if receiptLength == 0 :
        # Announce recentReceipt is empty
        print("Receipt is empty.")
        # Exit function
        return

    # This makes sure the loading bar will stop at a specified duration
    # timeStep / timeLength = 1 / iterations
    # timeStep = timeLength / iterations
    timeStep = shortDuration / receiptLength
    
    # Show userReceipt in a loop
    for index in range(receiptLength) :
        print(userReceipt[index])
        # Wait until specified duration
        time.sleep(timeStep)
    
    # Ask user to enter to continue
    input("\nPress enter to continue...")
    # This is for responding to prompt
    input()

# ---------------------------------------------------------------- # Vending Machine Interface # ---------------------------------------------------------------- #

def userInterface() :
    # Run under an infnite loop until program exit
    while True :
        # Clear current console
        clearConsole()
        
        # Display user interface
        print(
            f"""

    __  ___      _          ____      __            ____              
   /  |/  /___ _(_)___     /  _/___  / /____  _____/ __/___ _________ 
  / /|_/ / __ `/ / __ \    / // __ \/ __/ _ \/ ___/ /_/ __ `/ ___/ _ \\
 / /  / / /_/ / / / / /  _/ // / / / /_/  __/ /  / __/ /_/ / /__/  __/
/_/  /_/\__,_/_/_/ /_/  /___/_/ /_/\__/\___/_/  /_/  \__,_/\___/\___/ 

----------------------------------------------------------------

Current cash: AED {userCash}
Receipt history: {len(userReceipt)}
            """
        )

        # Display stock
        displayStock()

        # Display available user options and ask user for input
        textAnimation("\nType \"Insert\" to insert cash, \"Purchase\" to purchase items, \"Receipt\" to open receipt, or \"Exit\" to exit machine.\n")

        # Set output string to all lowercase allowing for all selections will be case insensitive
        userInput = inputLower()

        # Check if user types "Insert"
        if userInput == "insert" :
            # Announce inserting cash
            print("\nInserting cash...\n")
            # Insert cash
            insertCash()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "Purchase"
        if userInput == "purchase" :
            # Announce purchasing items
            print("\nPurchasing items...\n")
            # Purchase stock
            purchaseStock()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "Receipt"
        if userInput == "receipt" :
            # Announce opening reciept
            print("\nOpening receipt...\n")
            # Open reciept
            showReceipt()
            # Reset loop
            continue

        # Check if user types "Admin"
        if userInput == "admin" :
            # Announce admin enabled
            print("\nAdmin enabled...\n")
            # Admin access
            adminAccess()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "Exit"
        if userInput == "exit" :
            # Announce program exit
            print("\nGoodbye and have a nice day!")
            # Announce ejecting cash
            loadingAnimation(f"\nEjecting AED {userCash}...", shortDuration)
            # Wait for a small duration
            loadingAnimation("\nExiting interface...", shortDuration)
            # Exit program
            quit()
        
        # If for some reason all inputs are not one of the above, announce invalid input
        print("\nInvalid input.")
        # Wait for a small duration
        loadingAnimation("\nLoading interface...", shortDuration)

# ---------------------------------------------------------------- # Program Core # ---------------------------------------------------------------- #

# Clear current console
clearConsole()

# Announce program via text animation
textAnimation(
    """
----------------------------------------------------------------

 ▄█    █▄     ▄████████ ███▄▄▄▄   ████████▄   ▄█  ███▄▄▄▄      ▄██████▄         ▄▄▄▄███▄▄▄▄      ▄████████  ▄████████    ▄█    █▄     ▄█  ███▄▄▄▄      ▄████████ 
███    ███   ███    ███ ███▀▀▀██▄ ███   ▀███ ███  ███▀▀▀██▄   ███    ███      ▄██▀▀▀███▀▀▀██▄   ███    ███ ███    ███   ███    ███   ███  ███▀▀▀██▄   ███    ███ 
███    ███   ███    █▀  ███   ███ ███    ███ ███▌ ███   ███   ███    █▀       ███   ███   ███   ███    ███ ███    █▀    ███    ███   ███▌ ███   ███   ███    █▀  
███    ███  ▄███▄▄▄     ███   ███ ███    ███ ███▌ ███   ███  ▄███             ███   ███   ███   ███    ███ ███         ▄███▄▄▄▄███▄▄ ███▌ ███   ███  ▄███▄▄▄     
███    ███ ▀▀███▀▀▀     ███   ███ ███    ███ ███▌ ███   ███ ▀▀███ ████▄       ███   ███   ███ ▀███████████ ███        ▀▀███▀▀▀▀███▀  ███▌ ███   ███ ▀▀███▀▀▀     
███    ███   ███    █▄  ███   ███ ███    ███ ███  ███   ███   ███    ███      ███   ███   ███   ███    ███ ███    █▄    ███    ███   ███  ███   ███   ███    █▄  
███    ███   ███    ███ ███   ███ ███   ▄███ ███  ███   ███   ███    ███      ███   ███   ███   ███    ███ ███    ███   ███    ███   ███  ███   ███   ███    ███ 
 ▀██████▀    ██████████  ▀█   █▀  ████████▀  █▀    ▀█   █▀    ████████▀        ▀█   ███   █▀    ███    █▀  ████████▀    ███    █▀    █▀    ▀█   █▀    ██████████ 

Version 3.0, by Eldeston

----------------------------------------------------------------
    """
)

# Wait for a small duration
loadingAnimation("\nBooting machine...", normalDuration)

# Core of the program
userInterface()

# NOTE TO SELF:
# - [ ] Instead of using a menu selection at the start, make a flexible text detection based triggers
# - [ ] Ask user if they want to make a second purchase
# - [ ] Implement multiple categories of items
# - [x] Implement a secret trigger to access admin commands:
#   - [x] Admin command to add new items
#   - [x] Admin command to remove items
#   - [x] Admin command to withdraw profits