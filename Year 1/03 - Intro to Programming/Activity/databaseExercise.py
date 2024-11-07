import sqlite3
import sys

sqliteDatabase = sqlite3.connect("metaverse.db")

def insertData(name, age, city) :
    query = "Insert into metaverse(name, age, city) values(?, ?, ?)"
    sqliteDatabase.execute(query, (name, age, city))
    sqliteDatabase.commit()
    print("Insert successful")

print(
    """
Welcome to Metaverse database, type "Exit," or enter the following commands:
1. select
2. insert
3. update
4. delete
    """
)

while True :
    userInput = input("Enter a digit")

    if userInput == "exit" :
        print("Goodbye and have a nice day!")
        sys.exit()

    if userInput == "1" :
        print("Select data")
        continue
    
    if userInput == "2" :
        print("Insert data")
        name = input("Enter first name: ")
        age = input("Enter age: ")
        city = input("Enter city: ")
        insertData(name, age, city)
        continue
    
    if userInput == "3" :
        print("Update data")
        continue
    
    if userInput == "4" :
        print("Delete data")
        continue

    print("Invalid input, please enter a digit")