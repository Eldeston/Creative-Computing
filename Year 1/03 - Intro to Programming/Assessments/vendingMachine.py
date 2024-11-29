print(
    """
----------------------------------------------------------------

Vending Machine
Version 1.0

Insert amount, or type "payment" to enter item selection.
Type "exit" to close program.

----------------------------------------------------------------
    """
)

# Set item list
itemList = [
    {
        "Item Name" : "Coca Cola",
        "Item Count" : 10,
        "Item Price" : 3.0
    },

    {
        "Item Name" : "Pepsi",
        "Item Count" : 10,
        "Item Price" : 3.0
    },

    {
        "Item Name" : "Water",
        "Item Count" : 10,
        "Item Price" : 1.0
    }
]

# Display function
def displayItems() :
    iterate = 0

    for itemData in itemList :
        print(f"ID: {iterate}, Item Data: {itemData}")

        iterate += 1

# Get user cart function
def getCart(cart, price) :
    while True :
        userInput = input(
            f"""
Enter valid item ID to add to your cart.
Or type "Check out" to proceed to purchase or to skip this section.
Current cart: {cart}
            """)
        
        if userInput.lower() == "check out" :
            print("Proceeding to check out...")
            return

        if not userInput.isdigit() :
            print("Invalid input.")
            continue

        userItemID = int(userInput)

        if userItemID >= len(itemList) :
            print("Item is not on the list.")
            continue
    
        price += itemList[userItemID]["Item Price"]

        print("Item ID:", userItemID, "added.")
        cart.append(userItemID)

# Get user cash function
def getCash(cash, price) :
    while True :
        userInput = input(
            f"""
Enter valid cash amount.
Or type "Check out" to proceed to purchase or to skip this section.
Current cash: {cash}
            """)

        if userInput.lower() == "check out" :
            if cash < price :
                print("Incufficient cash. Proceed to checkout?")
                continue
            else :
                print("Proceeding to check out...")
                return

        if not userInput.isdigit() :
            print("Invalid input.")
            continue

        print("Cash amount:", userInput, "inserted.")
        cash += float(userInput)

userCart = []
userCash = 0.0
cartPrice = 0.0

while True :
    displayItems()

    getCart(userCart, cartPrice)

    getCash(userCash, cartPrice)

    # getPurchaseAmount(userCart, userCash)