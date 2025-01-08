# Import os, used to clear console
import os
# Import time, used to time animations and utilize delays
import time

# -------------------------------- # Debugging Settings # -------------------------------- #

# Display console
displayConsole = False

# Define common durations
# This determines the length of animations
longDuration = 8
normalDuration = 4
shortDuration = 2

# Declare user cash
userCash = 0.0
# Declare store cash
machineProfit = 0.0

# Declare authors for logging
user = "User"
admin = "Admin"
system = "System"

# Declare password (case sensitive)
password = "nahIdWin"

# Declare user reciept
userReceipt = []
# Declare receipt history
systemLog = []

# Declare item stock as a list
# Each list contains a dictionary defining the properties of the item's name, stock, and price
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
        "Name" : "Mountain Dew",
        "Stock" : 16,
        "Price" : 3.0
    },
    {
        "Name" : "Water",
        "Stock" : 16,
        "Price" : 1.0
    }
]

# -------------------------------- # Display Functions # -------------------------------- #

# Clear console function
def clearConsole() :
    # If display console is enabled
    if displayConsole : return

    # Check if the OS is Linux and use "clear" instead
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

# -------------------------------- # Common Functions # -------------------------------- #

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

# -------------------------------- # Debug Functions # -------------------------------- #

# Log system action function
def logAction(author = system, log = "Logged action") :
    # Access systemLog as a global variable
    global systemLog

    # Log action as list to system log
    systemLog += [author + ": " + log]

# Display stock function
def displayStock() :
    # Display top header
    print("--------------------------------------------------------------------------------------------------------------------------------\n")
 
    # Display current stock using a loop
    for index, properties in enumerate(itemStock) :
        # Display item properties
        print(f"ID: {index}, Name: {properties["Name"]}, Stock: {properties["Stock"]}, Price: {properties["Price"]}")
        # Wait for a set amount of time
        time.sleep(0.0625)

    # Display bottom header
    print("\n--------------------------------------------------------------------------------------------------------------------------------")

# -------------------------------- # Admin Functions # -------------------------------- #

# Withdraw profit function
def withdrawInterface() :
    # Access machineProfit as a global variable
    global machineProfit

    # Log action as Admin
    logAction(admin, "Withdrawing profits.")

    # Announce withdrawal
    loadingAnimation(f"\nWithdrawing AED {machineProfit}...")

    # Set profit to 0.0 (because obviously this is just a program and we can't really emulate ejecting cash)
    machineProfit = 0.0

    # Announce stock successfuly added
    print("\nProfits successfully withdrawn.")

# Add stock interface
def addInterface() :
    # Access itemStock as a global variable
    global itemStock

    # Log action as Admin
    logAction(admin, "Adding stock.")

    # Enter item name
    userItemName = input("\nEnter item name: ")

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
def removeInterface() :
    # Access itemStock as a global variable
    global itemStock

    # Log action as Admin
    logAction(admin, "Removing stock.")

    # Enter item index
    itemIndex = inputToInteger("\nEnter item stock: ")

    # Remove item
    del itemStock[itemIndex]

    # Announce stock successfuly added
    print("\nStock successfuly removed.")

# Password interface function
def passwordInterface() :
    # Access password as a global variable
    global password

    # Log action as Admin
    logAction(admin, "Changing password.")

    # Enter old password
    userInput = input("\nEnter old password (case sensitive): ")

    # If password is incorrect
    if not userInput == password :
        # Announce incorrect password
        print("\nIncorrect password.")
        # Exit function
        return

    # Enter new password
    password = input("\nEnter new password (case sensitive): ")

    # Announce password successfuly changes
    print("\nPassword successfuly changed.")

# Logs interface function
def logsInterface() :
    # Access systemLog as a global variable
    global systemLog

    # Log action as Admin
    logAction(admin, "Viewing history.")

    # Get systemLog length
    logLength = len(systemLog)

    # Check if systemLog is empty
    if logLength == 0 :
        # Announce systemLog is empty
        print("\nLog is empty.")
        # Exit function
        return

    # Print new line for interface formatting sake,
    # print() by default prints a newline if the parameters are empty
    print()

    # This makes sure the loading bar will stop at a specified duration
    # timeStep / timeLength = 1 / iterations
    # timeStep = timeLength / iterations
    timeStep = shortDuration / logLength

    # Show systemLog in a loop
    for index in range(logLength) :
        print(systemLog[index])
        # Wait until specified duration
        time.sleep(timeStep)

    # Ask user to enter to continue
    textAnimation("\nPress enter key to continue...")
    # This is for responding to prompt
    input()

# -------------------------------- # Admin Interface # -------------------------------- #

# Admin interface function
def adminInterface() :
    # Access machineProfit as a global variable
    global machineProfit

    # Access systemLog as a global variable
    global systemLog

    # Log action as Admin
    logAction(admin, "Interface accessed.")

    # Run under an infnite loop until interface exit
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

--------------------------------------------------------------------------------------------------------------------------------

Machine profits: AED {machineProfit}
Machine history: {len(systemLog)}
            """
            )

        # Display stock
        displayStock()

        # Display available user options and ask user for input
        textAnimation("\nType \"Withdraw/W\" to withdraw profits, \"Add/A\" to add new stock, \"Remove/R\" to remove stock, \"Logs/L\" to view logs, or \"Exit/E\" to exit interface.\n")

        # Set output string to all lowercase allowing for all selections will be case insensitive
        userInput = inputLower()

        # Check if user types "withdraw"
        if userInput in ("withdraw", "w") :
            # Announce withdrawing profits
            print("\nWithdrawing profits...")
            # Enter withdraw interface
            withdrawInterface()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "add"
        if userInput in ("add", "a") :
            # Announce adding stock
            print("\nAdding stock...")
            # Enter add interface
            addInterface()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "remove"
        if userInput in ("remove", "r") :
            # Announce removing stock
            print("\nRemoving stock...")
            # Enter remove interface
            removeInterface()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "password"
        if userInput in ("password", "p") :
            # Announce changing password
            print("\nChanging password...")
            # Enter password interface
            passwordInterface()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "history"
        if userInput in ("logs", "l") :
            # Announce viewing history
            print("\nViewing logs...")
            # Enter history interface
            logsInterface()
            # Reset loop
            continue

        # Check if user types "exit"
        if userInput in ("exit", "e") :
            # Announce exiting interface
            print("\nExiting interface...")
            # Exit function
            return

# Admin access function
def adminAccess() :
    # Case sensitive input
    userInput = input("\nEnter password (case sensitive): ")

    # Check if password is correct
    if userInput == password :
        # Announce access grants
        print("\nAccess granted.")
        # Enter admin interface
        adminInterface()
        # Log action as Admin
        logAction(admin, "Exiting interface.")
        # Exit function
        return
    
    # Announce invalid password and exit
    print("\nAccess denied.")

# -------------------------------- # Vending Machine Functions # -------------------------------- #

# Deposit interface function
def depositInterface() :
    # Access user as a global variable
    global user

    # Access userCash as a global variable
    global userCash

    # Access userReceipt as a global variable
    global userReceipt

    # Log action as User
    logAction(user, "Depositing cash.")

    # Ask user cash input
    userInput = inputToFloat("\nEnter cash: ")

    # Insert cash
    userCash += userInput

    # Make a recent receipt
    recentReceipt = f"Deposited AED {userInput}."
    # Record recent receipt as list
    userReceipt += [recentReceipt]

    # Log action as User
    logAction(user, recentReceipt)

    # Announce amount deposited
    print("\n" + recentReceipt)

# Buy interface function
def buyInterface() :
    # Access user as a global variable
    global user

    # Access userCash as a global variable
    global userCash
    # Access machineProfit as a global variable
    global machineProfit

    # Access userReceipt as a global variable
    global userReceipt

    # Log action as User
    logAction(user, "Buying items.")

    # Run under an infnite loop until interface exit
    while True :
        # Ask user item ID input
        itemID = inputToInteger("\nEnter item ID: ")

        # Check if item ID does not exists
        if itemID not in range(len(itemStock)) :
            # Announce item ID does not exist
            print("\nItem ID does not exist.")
            # Reset loop
            continue

        # Ask user stock amount
        stock = inputToInteger("\nEnter item amount: ")

        # Check if item stock is insufficient
        if itemStock[itemID]["Stock"] < stock :
            # Announce insufficient item stock
            print("\nInsufficient item stock.")
            # Reset loop
            continue

        # Calculate total price by multiplying item price and stock
        totalPrice = itemStock[itemID]["Price"] * stock

        # Check if the user has insufficient funds.
        if totalPrice > userCash :
            # Announce insufficient cash
            print("\nInsufficient cash.")
            # Reset loop
            continue

        # If all checks are valid, subtract current cash by total price
        userCash -= totalPrice
        # Add total price to storePrice
        machineProfit += totalPrice

        # Subtract current stock by stock requested
        itemStock[itemID]["Stock"] -= stock

        # Make a recent receipt
        recentReceipt = f"Dispensed {stock} {itemStock[itemID]["Name"]} for AED {totalPrice} with AED {userCash} left in deposit."

        # Record recent receipt as list
        userReceipt += [recentReceipt]

        # Log action as User
        logAction(user, recentReceipt)

        # Announce recent receipt
        print("\n" + recentReceipt)

        # Ask if user wants to continue or press enter key to exit interface
        userInput = inputLower("\nType \"Continue/C\" to continue making purchases or press enter key to exit interface...")

        # Check if user types anything but continue
        if not userInput in ("continue", "c") :
            # Exit function
            return

# Receipt interface function
def receiptInterface() :
    # Access user as a global variable
    global user

    # Access userReceipt as a global variable
    global userReceipt

    # Log action as User
    logAction(user, "Viewing receipt.")

    # Get userReceipt length
    receiptLength = len(userReceipt)

    # Check if recentReceipt is empty
    if receiptLength == 0 :
        # Announce recentReceipt is empty
        print("\nReceipt is empty.")
        # Exit function
        return
    
    # Print new line for interface formatting sake,
    # print() by default prints a newline if the parameters are empty
    print()

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
    textAnimation("\nPress enter key to continue...")
    # This is for responding to prompt
    input()

# -------------------------------- # Vending Machine Interface # -------------------------------- #

# User interface function (otherwise known as the core of the program)
def userInterface() :
    # Access user as a global variable
    global user

    # Access userCash as a global variable
    global userCash

    # Access userReceipt as a global variable
    global userReceipt

    # Log action as User
    logAction(user, "Interface accessed.")

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

--------------------------------------------------------------------------------------------------------------------------------

Current cash: AED {userCash}
Receipt history: {len(userReceipt)}
            """
        )

        # Display stock
        displayStock()

        # Display available user options and ask user for input
        textAnimation("\nType \"Deposit/D\" to deposit cash, \"Buy/B\" to buy items, \"Receipt/R\" to open receipt, or \"Exit/E\" to exit machine.\n")

        # Set output string to all lowercase allowing for all selections will be case insensitive
        userInput = inputLower()

        # Check if user types "Deposit"
        if userInput in ("deposit", "d") :
            # Announce depositing cash
            print("\nDepositing cash...")
            # Enter deposit interface
            depositInterface()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "Buy"
        if userInput in ("buy", "b") :
            # Announce buying items
            print("\nBuying items...")
            # Enter buy interface
            buyInterface()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "Receipt"
        if userInput in ("receipt", "r") :
            # Announce opening reciept
            print("\nOpening receipt...")
            # Enter reciept interface
            receiptInterface()
            # Reset loop
            continue

        # Check if user types admin
        if userInput in ("admin", "a") :
            # Announce accessing admin
            print("\nAccessing admin...")
            # Enter admin access
            adminAccess()
            # Wait for a small duration
            loadingAnimation("\nLoading interface...", shortDuration)
            # Reset loop
            continue

        # Check if user types "Exit"
        if userInput in ("exit", "e") :
            # Announce program exit
            print("\nGoodbye and have a nice day!")
            # Announce ejecting cash
            textAnimation(f"\nDispensing AED {userCash} for {user}...", shortDuration)
            # Make a new line in console
            print()
            # Wait for a small duration
            loadingAnimation("\nExiting interface...", shortDuration)
            # Exit function, usually I'd use quit() to exit program immediately but this is for the sake logging user actions
            return
        
        # If for some reason all inputs are not one of the above, announce invalid input
        print("\nInvalid input.")
        # Wait for a small duration
        loadingAnimation("\nLoading interface...", shortDuration)

# -------------------------------- # Program Main # -------------------------------- #

# Core function
def mainSystem() :
    # Access user as a global variable
    global user

    # Run under an infnite loop until program exit
    while True :
        # Clear current console
        clearConsole()

        # Announce program via text animation
        textAnimation(
        """
--------------------------------------------------------------------------------------------------------------------------------

 _    __               ___                __  ___           __    _          
| |  / /__  ____  ____/ (_)___  ____ _   /  |/  /___ ______/ /_  (_)___  ___ 
| | / / _ \/ __ \/ __  / / __ \/ __ `/  / /|_/ / __ `/ ___/ __ \/ / __ \/ _ \\
| |/ /  __/ / / / /_/ / / / / / /_/ /  / /  / / /_/ / /__/ / / / / / / /  __/
|___/\___/_/ /_/\__,_/_/_/ /_/\__, /  /_/  /_/\__,_/\___/_/ /_/_/_/ /_/\___/ 
                             /____/
Version 4.0, by Eldeston

--------------------------------------------------------------------------------------------------------------------------------
        """
        )

        # Ask user for their name
        userInput = input("\nEnter username or enter a digit to exit.\n")

        # If user input is 0, exit funciton
        if userInput.isdigit() :
            # Exit function
            return

        # Set user as userInput
        user = userInput

        # Wait for a small duration
        loadingAnimation(f"\nLogging in as {user}...", shortDuration)

        # Log action as User
        logAction(user, f"Logged in as {user}.")

        # Load user interface
        userInterface()

        # Wait for a small duration
        loadingAnimation(f"\n{user} is logging out...", shortDuration)

        # Log action as System
        logAction(user, f"{user} logged out.")

# -------------------------------- # Program Main # -------------------------------- #

# Log action as System
logAction(system, "Booting system.")

# Core of the program
mainSystem()

# Log action as User
logAction(user, "Exiting main interface.")

# Log action as System
logAction(system, "Shutting down.")

# BASIC STRUCTURE
# - [x] Booting animation
# - [x] User sign in
# - [x] Main system
#     - [x] User interface
#         - [x] Deposit cash
#         - [x] Buy items
#         - [x] View receipt
#         - [x] Admin access (Secret trigger)
#             - [x] Enter password
#             - [x] Admin interface
#                 - [x] Withdraw profits
#                 - [x] Add stock
#                 - [x] Remove stock
#                 - [x] Change password
#                 - [x] Check logs
#                 - [x] Exit admin interface
#         - [x] Exit user interface
#     - [x] Exit main system

# OTHER IMPLEMENTED CHANGES:
# - [x] Code formatting
# - [x] Exception handling
# - [x] Implement a basic user interface
# - [x] Implement optional aliases for options
# - [x] Ask user if they want to make a second buy or implement an entire interface dedicated to buying additional items

# - [x] Implement a secret trigger to access admin interface:
#   - [x] Admin command to add new items
#   - [x] Admin command to remove items
#   - [x] Admin command to withdraw profits
#   - [x] Admin command to view system log
#   - [x] Admin command to change password

# DISCONTINUED CHANGES
# - [ ] Implement recommendation system using existing dictionary
# - [ ] Implement multiple categories of items using lists or dictionary

# - [ ] Implement accessibility features
#   - [ ] Keyboard navigation
#   - [ ] Text to speech
#   - [ ] Sound queues