try :
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
    print("Division Result:", c)
except Exception as errorString :
    print("Error caused by:", errorString)

try :
    print(a)
except NameError:
    print("Error caused by: name error")

print("Womp womp")