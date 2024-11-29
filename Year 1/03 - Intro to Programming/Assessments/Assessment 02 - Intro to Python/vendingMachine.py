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

def displayStock() :
    for index, properties in enumerate(itemStock) :
        print(f"ID: {index}, Name: {properties["Name"]}, Stock: {properties["Stock"]}, Price: {properties["Price"]}")

def purchaseStock(id, cash) :
    for index, properties in enumerate(itemStock) :
        if index == id and properties["Price"] >= cash :
            print("Purchased item:", properties["Name"])
            properties["Stock"] -= 1

purchaseStock(0, 10.0)

displayStock()