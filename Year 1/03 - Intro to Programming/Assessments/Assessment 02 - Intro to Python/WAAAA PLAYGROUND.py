def display() :
    print(insertInterface)

categories = {
    "Drinks" : [
        {
            "Name" : "Cola",
            "Price" : 10.0
        },
        {
            "Name" : "Pepse",
            "Price" : 20.0
        }
    ]
}

categories["Drinks"][0]["Price"] == 10.0

def selection() :
    inputCategory = input("What category").lower()

    inputID = int(input("What item ID"))

    categories[inputCategory][inputID]["Price"] == 10.0
    categories[inputCategory][inputID]["Name"] == "Cola"

    print(f"You bought {categories[inputCategory][inputID]["Name"]} for AED {categories[inputCategory][inputID]["Price"]}")

def userInterface() :
    display()

    usernput = input()

    if usernput == "insert" :
        insertCash()

    if usernput == "purchase" :
        purchaseItems()

    if usernput == "exit" :
        exitInterface()

userinterface()