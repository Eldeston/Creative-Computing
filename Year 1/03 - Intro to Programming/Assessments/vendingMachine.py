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

itemPrice = {
    "Coca Cola" : "3",
    "Pepsi" : "3",
    "Water" : "1"
}

itemCount = {
    "Coca Cola" : "5",
    "Pepsi" : "5",
    "Water" : "5"
}

itemId = {
    "0" : "Coca Cola",
    "1" : "Pepsi",
    "2" : "Water"
}

amount = 0

selections = [
    ""
]

while True :
    while True :
        userInput = input(
            """
Please enter the id of your item. Type \"Purchase\" to proceed to purchase, or type \"Exit\" to exit program:
            """
        )

        if userInput.lower() == "exit" :
            quit()
        
        if userInput.lower() == "purchase" :
            break

        if userInput in itemId.keys() :
            currentSelection = itemId[userInput]
            selections.append(currentSelection)
            print(currentSelection, "added.")
            continue

        print("Invalid input.")
    
    while True :
        userInput = input(
            """
Please enter current amount. Type \"Confirm\" to proceed to purchase, type \"reset\" to reset program, or type \"Exit\" to exit program:
            """
        )

        if userInput.lower() == "exit" :
            quit()
        
        if userInput.lower() == "reset" :
            break
        
        if userInput.lower() == "confirm" :
            break

        print("Invalid input.")