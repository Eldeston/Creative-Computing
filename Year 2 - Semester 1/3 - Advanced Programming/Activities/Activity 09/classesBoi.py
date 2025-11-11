# Creates a class called "Animal"
class Animal :
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creates a class called "Cat" and inherits "Animal"
class Cat(Animal) :
    def info(self) :
        print(f"I'm a a cat. My name is {self.name}. I am {self.age} years old.")
    
    def makeSound(self) :
        print("Meow.")

# Creates a class called "Dog" and inherits "Animal"
class Dog(Animal) :
    def info(self) :
        print(f"I'm a a dog. My name is {self.name}. I am {self.age} years old.")
    
    def makeSound(self) :
        print("Woof.")

# Creates objects called cat0 and dog0
cat0 = Cat("Meowthra", 2.5)
dog0 = Dog("Bruce", 7.0)

# Runs both classes in a list via loop
for animal in (cat0, dog0) :
    animal.info()
    animal.makeSound()