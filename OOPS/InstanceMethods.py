'''
Instance Methods in Python
-------------------------

Definition:
-----------
An instance method is a function defined inside a class that operates on the object instance (self) of that class. It can access and modify the object's attributes.

Syntax:
--------
class ClassName:
    def method_name(self, [args]):
        # method body

- The first argument is always 'self', which refers to the object instance calling the method.
- Called using: object.method_name([args])

Common Built-in Methods:
------------------------
- __init__(self, ...): Constructor, called when an object is created.
- __str__(self): String representation of the object.
- Any custom method defined with self as the first parameter.

'''

# Beginner Example: Defining and Using an Instance Method

class Person:
    def __init__(self, name):
        self.name = name         # Instance attribute

    def greet(self):             # Instance method
        print(f"Hello, my name is {self.name}")

p = Person("Alice")
p.greet()   # Output: Hello, my name is Alice

# Modifying instance attributes inside an instance method

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

acc = BankAccount(100)
acc.deposit(50)   # Deposited 50. New balance is 150

'''
Intermediate Example: Passing Parameters and Returning Values
------------------------------------------------------------
You can define instance methods with parameters and have them return values.
'''

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def resize(self, width, height):
        self.width = width
        self.height = height

r = Rectangle(10, 5)
print("Area:", r.area())  # Area: 50
r.resize(8, 4)
print("Resized Area:", r.area())  # Resized Area: 32

'''
Advanced Example: Instance Methods and Object Communication
----------------------------------------------------------
Multiple objects can interact and instance methods can receive objects as arguments.
'''

class Student:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, other_student):
        if isinstance(other_student, Student) and other_student is not self:
            self.friends.append(other_student)

    def show_friends(self):
        print(self.name + "'s friends:", ', '.join([f.name for f in self.friends]))

s1 = Student("Sam")
s2 = Student("Alex")
s3 = Student("Charlie")

s1.add_friend(s2)
s1.add_friend(s3)
s1.show_friends()  # Sam's friends: Alex, Charlie

'''
Override instance methods for polymorphism
-----------------------------------------

Instance methods can be overridden in derived (child) classes to provide specialized behavior (see method overriding).

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")

Dog().sound()  # Bark!
'''

# Mini Project: Library Book System using Instance Methods

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return f"You have borrowed '{self.title}'"
        else:
            return f"'{self.title}' is not available."

    def return_book(self):
        if not self.available:
            self.available = True
            return f"You have returned '{self.title}'"
        else:
            return f"'{self.title}' was not borrowed."

    def info(self):
        status = 'Available' if self.available else 'Not Available'
        print(f"{self.title} by {self.author} [{status}]")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added '{book.title}' to library.")

    def list_books(self):
        print("Library Catalog:")
        for book in self.books:
            book.info()

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                print(book.borrow())
                return
        print(f"No book titled '{title}' found.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                print(book.return_book())
                return
        print(f"No book titled '{title}' found.")

# Using the mini project
lib = Library()
b1 = Book("1984", "George Orwell")
b2 = Book("To Kill a Mockingbird", "Harper Lee")
lib.add_book(b1)
lib.add_book(b2)
lib.list_books()
lib.borrow_book("1984")
lib.list_books()
lib.return_book("1984")
lib.list_books()

'''
Interview Questions and Answers: Instance Method Deep Dive
---------------------------------------------------------

Q1. What is the difference between an instance method, a class method, and a static method in Python?
A1. 
- Instance methods take 'self' as the first parameter and can access/modify object state.
- Class methods take 'cls' as the first parameter and can access/modify the class state, but not object-specific data directly.
- Static methods don't take 'self' or 'cls' and behave like plain functions, but live in the class's namespace.

Q2. How can an instance method access and modify data in another instance?
A2.
By receiving another object as a parameter and accessing/modifying its attributes/methods.
Example:
    class User:
        def __init__(self, name): self.name = name

        def copy_name_from(self, other):
            self.name = other.name
            
    u1 = User("Alice")
    u2 = User("Bob")
    u1.copy_name_from(u2)
    print(u1.name)  # Output: Bob

Q3. What happens if you call an instance method from the class directly?
A3.
You must explicitly pass an object for self.
Example:
    class Foo:
        def bar(self): print("bar")
    obj = Foo()
    Foo.bar(obj)  # Output: bar

Q4. Can you call an instance method before initializing the object?
A4.
No, you must instantiate (create) the object first, otherwise you'll get a TypeError.

Q5. How does Python internally bind the 'self' argument to instance methods?
A5.
When you call obj.method(), Python behind the scenes does: Class.method(obj).
So 'self' refers to the object before the dot.

Q6. Can an instance method create new attributes for an object? Give example.
A6.
Yes, attributes can be set dynamically inside an instance method using 'self':
    class Car:
        def set_color(self, color):
            self.color = color
    c = Car()
    c.set_color("blue")
    print(c.color)  # blue

Q7. What would happen if you omitted 'self' in an instance method signature?
A7.
You'd get a TypeError on call (missing 1 required positional argument) because Python always passes the instance as the first argument to instance methods.

Q8. How do instance methods allow for polymorphic behavior in OOP?
A8.
By defining the same method name in parent and child classes, and relying on Python’s dynamic dispatch to call the correct implementation for each object, enabling runtime polymorphism.

Q9. Can you store references to instance methods? Why is this useful?
A9.
Yes, you can assign obj.method to a variable and call it later. This is useful for callbacks, event-driven code, or passing behavior as parameters.
Example:
    class Calc: 
        def double(self, x): return 2*x
    c = Calc()
    f = c.double
    print(f(4))  # 8

Q10. Real-world scenario: Why would you use an instance method over a static or class method?
A10.
When the logic depends on or modifies specific object data, e.g., updating a user's profile, processing a transaction in a bank account, or computing invoice values for an individual order—each object needs its own state to work with, so instance methods are necessary.

'''
