# Required to access SQLite database
import sqlite3

# Access database via variable
sqliteDB = sqlite3.connect("Year 1/03 - Intro to Programming/Activity/metaverse.db")

# Announce program
print(
    """
Welcome to Metaverse database, type "Exit," or enter the following commands:
1. Select data
2. Insert data
3. Update data
4. Delete data
    """
)

# Define function for select data
def selectData() :
    query = "select * from metaverse;"
    queryResult = sqliteDB.execute(query)

    for x in queryResult :
        print(x)

    print("Selected data")

# Define function for inserting data
def insertData(name, age, city) :
    query = "insert into metaverse(name, age, city) values(?, ?, ?);"
    sqliteDB.execute(query, (name, age, city))
    sqliteDB.commit()
    print("Inserted data")

# Define function for updating data
def updateData(id, name, age, city) :
    query = "update metaverse set name = ?, age = ?, city = ? where id = ?;"
    sqliteDB.execute(query, (name, age, city, id))
    sqliteDB.commit()
    print("Updated data")

# Define function for deleting data
def deleteData(id) :
    query = "delete from metaverse where id = ?;"
    sqliteDB.execute(query, (id))
    sqliteDB.commit()
    print("Deleted data")

# While the program is running
while True :
    # Check for user input every loop
    userInput = input("Enter a digit: ")

    # If the input is "exit," say goodbye and exit program
    if userInput == "exit" :
        print("Goodbye and have a nice day!")
        quit()

    # User selects data
    if userInput == "1" :
        print("1. Select data")

        # Display database
        selectData()
    # User inserts data
    elif userInput == "2" :
        print("2. Insert data")

        # Take user input for name, age, and city
        name = input("Enter first name: ")
        age = int(input("Enter age: "))
        city = input("Enter city: ")

        # Update database
        insertData(name, age, city)
    # User updates data
    elif userInput == "3" :
        print("3. Update data")

        # Take user input for id and updated name, age, and city
        id = input("Enter your id: ")
        name = input("Enter updated first name: ")
        age = int(input("Enter updated age: "))
        city = input("Enter updated city: ")

        # Update database
        updateData(id, name, age, city)
    # User deletes data
    elif userInput == "4" :
        print("4. Delete data")

        # Take user input for id
        id = input("Enter your id: ")

        # Update database
        deleteData(id)
    # User makes an invalid input
    else :
        print("Invalid input, please enter one of the available commands in digits")