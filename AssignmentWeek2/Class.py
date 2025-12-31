# 1. Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(f"Name: {person.name}, Age: {person.age}")



# 2. Problem: Write a Python class named BankAccount with attributes like account_number, balance, 
# and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")
    
    def check_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.balance}")
        return self.balance

# Example usage:
account = BankAccount("12345", "John Doe", 1000.0)
account.deposit(500)
account.withdraw(200)
account.check_balance()



# 3. Create a class Book with a class method from_string() that creates a Book instance from a string. 
# And print both attributes of the class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    @classmethod
    def from_string(cls, book_string):
        title, author = book_string.split(", ")
        return cls(title, author)
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

book = Book.from_string("Python Programming, John Doe")
print(f"Title: {book.title}")
print(f"Author: {book.author}")



# 4. Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides 
# the sound() method and call those methods.
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow! Meow!"

# Create instances and call methods
dog = Dog()
cat = Cat()
print(f"Dog says: {dog.sound()}")
print(f"Cat says: {cat.sound()}")



# 5. Write a code to perform multiple inheritance.
class Flyable:
    def fly(self):
        return "Flying high in the sky"

class Swimmable:
    def swim(self):
        return "Swimming in the water"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return f"{self.name} says: Quack! Quack!"

# Create an instance of Duck which inherits from both Flyable and Swimmable
duck = Duck("Donald")
print(duck.quack())
print(duck.fly())
print(duck.swim())

