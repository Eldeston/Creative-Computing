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

itemList = [
    {
        "Item Name" : "Coca Cola",
        "Item Count" : 10,
        "Item Price" : 3
    },

    {
        "Item Name" : "Pepsi",
        "Item Count" : 10,
        "Item Price" : 3
    },

    {
        "Item Name" : "Water",
        "Item Count" : 10,
        "Item Price" : 1
    }
]

def displayItems() :
    iterate = 0

    for itemData in itemList :
        print(f"ID: {iterate}, Item Data: {itemData}")

        iterate += 1

def getItemID(cart) :
    while True :
        userInput = input(
            """
Enter item ID to make your selection(s).
Or type "Check out" to proceed to purchase or to skip this section.
            """)
        
        if userInput.lower() == "check out" : return

        if userInput.isdigit() : continue

        cart.append(int(userInput))

def getPurchase(cash) :
    while True :
        userInput = input(
            """
Enter cash amount.
Or type "Check out" to proceed to purchase or to skip this section.
            """)

        if userInput.lower() == "check out" : return

        if userInput.isdigit() : continue

        cart.append(int(userInput))

while True :
    displayItems()

    userCash = 0.0
    userCart = []

    getItemID(userCart)

    getPurchase(userCash)