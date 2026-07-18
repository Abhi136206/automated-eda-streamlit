#Create a Python program with a base class Vehicle that has attributes brand and speed. 
# Create a derived class Car that inherits from Vehicle and adds an attribute fuel_type.
# Implement a method display_info() in both classes to print the details.

class vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        
    def display_info(self):
        print(f"brand : {self.brand}, speed : {self.speed} km/h")
        
class car(vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type
        
    def display_info(self):
        print(f"brand : {self.brand}, speed : {self.speed} km/h, fuel type : {self.fuel_type}")
        
car1 = car("Toyota", 108, "Petrol")
car1.display_info()
        
#Polymorphism
#Create two classes, Dog and Cat, both having a method speak().
#The Dog class should return "Woof! Woof!" when speak() is called.
#The Cat class should return "Meow! Meow!" when speak() is called.
#Write a function animal_sound(animal) that takes an object (either Dog or Cat) and calls its speak() method.       
        
class dog:
    def speak(self):
        return "woof! woof!"
    
class cat:
    def speak(self):
        return "Meow! Meow!"
    
def animal_sound(animal):
    print(animal.speak())
    
dog1 = dog()
cat1 = cat()

animal_sound(dog1)
animal_sound(cat1)

#Encapsulation
#Create a class BankAccount with the following:
#A private attribute _balance (use encapsulation).
#A constructor that initializes _balance with a given amount.
#A method deposit(amount) to add money to the account.
#A method withdraw(amount) that withdraws money only if the balance is sufficient.
#A method get_balance() that returns the current balance.
class Bannkaccount:
    def__init__(self, intial_balance):
        
        self._balance = intial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"deposited: {amount}")
        else:
            print("deposit amount must be positive")