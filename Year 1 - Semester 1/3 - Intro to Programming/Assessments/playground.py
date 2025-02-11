# -- coding: utf-8 --
"""
Created on Fri Nov 29 13:00:38 2024

@author: Christian James
"""

import time
print ("Welcome to the Python Vending Machine.")

# Asking the user how much money they wish to enter.
number_of_Aed = int(input("How many Aed would you like to insert? "))
while number_of_Aed < 0:
    number_of_Aed = int(input("Please enter a positive number."))

# Creating a variable to store the total amount of money inserted into the vending machine.
change = round(((number_of_Aed * 1)),2)

# Informing the user how much they have entered in total.
print ("\nIn total you have entered Aed", change)
time.sleep(2)
# Creating variables for the 5 products and their respective prices. 
product_1, product_1_price = "Kitkat", 2
product_2, product_2_price = "Coke", 5
product_3, product_3_price = "Mountain Dew", 4
product_4, product_4_price = "Water Bottle", 1
product_5, product_5_price = "Red Bull", 7

# Creating variables to track the number of each items bought,
Kitkat_bought = 0
Coke_bought = 0
MountainDew_bought = 0
Water_bottle_bought = 0
Red_Bull_bought = 0

# Informing the user of the choices available and the prices that of each item.
print ("There are 5 products available to pick from;\n")
time.sleep(2)
print ("Item: {}, Price {} ".format(product_1, product_1_price))
print ("Item: {}, Price {} ".format(product_2, product_2_price))
print ("Item: {}, Price {} ".format(product_3, product_3_price))
print ("Item: {}, Price {} ".format(product_4, product_4_price))
print ("Item: {}, Price {} ".format(product_5, product_5_price))
print ("")

# Asking the user to make a selection.
while change > 0:
    customer_choice = input("What would you like to buy? Type N when you are finished \n")
    if customer_choice == "Kitkat" and change >= product_1_price:
        print ("You have chosen a", product_1, "these cost", product_1_price, "each,")
        change = round((change - product_1_price),2)
        Kitkat_bought = (Kitkat_bought + 1)
        print ("You have this much money remaining: Aed", change)

    elif customer_choice == "Coke" and change >= product_2_price:
        print ("You have chosen a", product_2, "these cost", product_2_price, "each,")
        change = round((change - product_2_price),2)
        Coke_bought = (Coke_bought + 1)
        print ("You have this much money remaining: Aed", change)

    elif customer_choice == "Mountain Dew" and change >= product_3_price:
        print ("You have chosen a", product_3, "these cost", product_3_price, "each,")
        change = round((change - product_3_price),2)
        MountainDew_bought = (MountainDew_bought + 1)
        print ("You have this much money remaining: Aed", change)

    elif customer_choice == "Water Bottle" and change >= product_4_price:
        print ("You have chosen a", product_4, "these cost", product_4_price, "each,")
        change = round((change - product_4_price),2)
        Water_bottle_bought = (Water_bottle_bought + 1)
        print ("You have this much money remaining: Aed", change)

    elif customer_choice == "Red Bull" and change >= product_5_price:
        print ("You have chosen a", product_5, "these cost", product_5_price, "each,")
        change = round((change - product_5_price),2)
        Red_Bull_bought = (Red_Bull_bought + 1)
        print ("You have this much money remaining: Aed", change)

    elif customer_choice == "n":
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (product_1, "x", Kitkat_bought)
        print (product_2, "x", Coke_bought)
        print (product_3, "x", MountainDew_bought)
        print (product_4, "x", Water_bottle_bought)
        print (product_5, "x", Red_Bull_bought)
        print ("You have Aed", change, "remaining.")
        break

    elif change <= 0:
        print ("You have run out of money.")
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (product_1, "x", Kitkat_bought)
        print (product_2, "x", Coke_bought)
        print (product_3, "x", MountainDew_bought)
        print (product_4, "x", Water_bottle_bought)
        print (product_5, "x", Red_Bull_bought)
        break

    else:
        print ("There has been an error or you may not have enough credit.")