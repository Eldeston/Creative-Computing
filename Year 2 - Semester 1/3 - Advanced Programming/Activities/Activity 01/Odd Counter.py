iteration = 0

while iteration <= 10 :
    print(iteration)
    iteration += 2

# Syntax is:
#   range(end) # Starts at 0 by default
#   range(start, end)
#   range(start, end, increment)
numSeq = range(10, 20, 1)

print(numSeq)

snaccs = ["Snickers", "Oreo", "SkyFlakes", "Mars", 'Doritos', "Coke"]

snaccs.pop(-1)
snaccs.pop(0)
snaccs.sort()

print(snaccs)

user = {
    "username" : "Eldeston",
    "uuid" : 129835
}

print(user.items())
print(user.keys())
print(user.values())

# Adds
user["creation_date"] = 2011
# Modify
user["uuid"] = 999999
# Removes
user.pop("username")

print(user.items())

year1 = (1987, 1985, 1981, 1996)
year2 = (2002, 2017, 2018, 2021)

year1, year2 = year2, year1

print(year1)
print(year2)

def getStudentInfo(name, id) :
    return f"Student's name is {name}. Their ID is {id}."

print(getStudentInfo("Frem", 12828))