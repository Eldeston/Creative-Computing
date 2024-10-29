# -------- Activity 15 --------

# Initializing lists, notice all of them are not tuples
emptyList = []
intList = [1, 2, 3]
mixedList = [1, 2.0, "Three"]

nestedList = [
    [1, 2, 3],
    ["Iron Man", "Captain America", "Thor"],
    [3.1415, 1.4145, 6.2821]
]

print(
    f"""
Empty List
{emptyList}

Single Data Type List
{intList}

Mixed Data Type List
{mixedList}

Nested List
{nestedList}
    """
)

print(
    f"""
Positive Indexing, Output: 2.0
{mixedList[1]}

Negative Indexing, Output: Three
{mixedList[-1]}
    """
)

primeNumbers = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print(
    f"""
List Slicing, Output: 3, 5, 7
{primeNumbers[2 : 5]}

List Omitting (End of List), Output: 19, 23, 29
{primeNumbers[8:]}

List Omitting (Beginning of List), Output: 1, 2, 3
{primeNumbers[:3]}
    """
)

# Undo the reversed list
primeNumbers.sort(reverse = True)

print(
    f"""
List Sorting (Reversing)
{primeNumbers}
    """
)

# Reverse the list to original
primeNumbers.sort(reverse = False)

# Change a list value
primeNumbers[1] = 0

print(
    f"""
List Value Swapping, Output: 0
{primeNumbers[1]}
    """
)

# Undo the list value
primeNumbers[1] = 2

# Appending a list
primeNumbers.append(31)

print(
    f"""
Appending List, New Value: 31
{primeNumbers}
    """
)

# Extending a list
primeNumbers.extend([37, 41, 43])

print(
    f"""
Extended List, New Values: 37, 41, 43
{primeNumbers}
    """
)

# Extending a list via adding
print(
    f"""
Extended List (Adding), New Values: 47, 53, 59
{primeNumbers + [47, 53, 59]}
    """
)

# Inserting a new value
mixedList.insert(2, True)

print(
    f"""
Inserting Value, New Values: True
{mixedList}
    """
)

# Replacing new values using slicing
mixedList[2 : 4] = ["3", "Four"]

print(
    f"""
Replacing Values (Slicing), New Values: "3", "Four"
{mixedList}
    """
)

# Deleting value in a list
del primeNumbers[14]

print(
    f"""
Deleting value in a list, Deletes 43
{primeNumbers}
    """
)

# Deleting multiple values in a list
del primeNumbers[10 :]

print(
    f"""
Deleting multiple values in a list, Deletes 29, 31, 37
{primeNumbers}
    """
)

# Initialize a dictionary
familyMembers = {
    "Frem" : 19,
    "Maudric" : 18,
    "Faith" : 12,
    "Mikhyla" : 5
}

print(
    f"""
Display (Current) Dictionary
{familyMembers}
    """
)

# Add 2 more keys with values
familyMembers["Milfred"] = 42
familyMembers["Mechan"] = 43

print(
    f"""
Display (Added) Dictionary
{familyMembers}
    """
)

# Modify existing values
familyMembers["Frem"] = 20
familyMembers["Maudric"] = 19
familyMembers["Faith"] = 13

print(
    f"""
Display (Modified) Dictionary
{familyMembers}
    """
)

# Delete existing keys and values
del familyMembers["Milfred"]
del familyMembers["Mechan"]

print(
    f"""
Display (Deleted) Dictionary
{familyMembers}
    """
)

familyData = [
    {
        "Name" : "Mechan",
        "Age" : 43,
        "Role" : "Mom"
    },
    {
        "Name" : "Milfred",
        "Age" : 42,
        "Role" : "Dad"
    },
    {
        "Name" : "Frem",
        "Age" : 20,
        "Role" : "Firstborn"
    },
    {
        "Name" : "Maudric",
        "Age" : 19,
        "Role" : "Middle"
    },
    {
        "Name" : "Faith",
        "Age" : 13,
        "Role" : "Middle"
    },
    {
        "Name" : "Mikhyla",
        "Age" : 5,
        "Role" : "youngest"
    }
]

print("Display Dictionary Values in a List")

i = 0
while i < 6 :
    print(familyData[i])
    i += 1


# Add a new key and value with a new dictionary
newMembers = {
    "Wilfred" : 61,
    "Melchura" : 60,
    "Milfred" : 42,
    "Mechan" : 43
}

familyMembers.update(newMembers)

print(
    f"""
Display (Updated) Dictionary
{familyMembers}
    """
)