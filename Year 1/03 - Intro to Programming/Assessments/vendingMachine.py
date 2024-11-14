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
    "Coca Cola" : 3,
    "Pepsi" : 3,
    "Water" : 1
}

itemId = {
    0 : "Coca Cola",
    1 : "Pepsi",
    2 : "Water"
}

while True :
    coins = 0

    while True :
        userInput = input()

        if userInput.lower() == "exit" :
            quit()

        if userInput.lower() == "payment" :
            break
        
        if not userInput.isdigit() :
            print("Invalid input.")
            continue

        coins += int(userInput)
    
    while True :
        userInput = input(
            f"""
----------------------------------------------------------------

Inserted amount: {coins}
Choose an Item:
0 {itemId[0]}
1 {itemId[1]}
2 {itemId[2]}

----------------------------------------------------------------
            """
        )

        if userInput.lower() == "exit" :
            quit()
        
        if not userInput.isdigit() :
            print("Invalid input.")
            continue