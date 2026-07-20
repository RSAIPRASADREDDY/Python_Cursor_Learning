"""
Object in Python: Concepts, Methods, Syntax, Examples, Mini-project, and Interview Q&A

Definition:
-----------
An Object in Python is an instance of a class. 
Objects are the fundamental building blocks in Object-Oriented Programming (OOPS). 
Each object contains both data (attributes) and behavior (methods). 
Objects are created from classes and represent real-world or abstract entities.

Methods We Can Use:
-------------------
- __init__() constructor: Initializes object attributes.
- Access attribute: obj.attr
- Call method: obj.method()
- hasattr(obj, 'attr'): Checks if object has an attribute.
- getattr(obj, 'attr'): Gets the value of an attribute.
- setattr(obj, 'attr', value): Sets an attribute.
- delattr(obj, 'attr'): Deletes an attribute.
- isinstance(obj, Class): Checks if obj is instance of Class.
- type(obj): Returns the type of the object.
- id(obj): Returns the unique identity of object.

Syntax:
-------
# Define a class
class MyClass:
    def __init__(self, value):
        self.attr = value

    def some_method(self):
        print(self.attr)

# Create an object
obj = MyClass(5)

# Access attributes and methods
print(obj.attr)         # Output: 5
obj.some_method()       # Output: 5
"""

# -----------------------------------------------
# Beginner Level Examples
# -----------------------------------------------

# Example 1: Basic Object Creation and Attribute Access
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Alice")
print("Student's Name:", student1.name)  # Output: Student's Name: Alice

# Example 2: Using Methods in an Object
class Car:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print(f"{self.brand} says Honk!")

car1 = Car("Toyota")
car1.honk()  # Output: Toyota says Honk!

# -----------------------------------------------
# Intermediate Level Examples
# -----------------------------------------------

# Example 3: Dynamic Attribute Addition
class Empty:
    pass

obj = Empty()
obj.x = 10
obj.y = 20
print("x + y =", obj.x + obj.y)  # Output: x + y = 30

# Example 4: Using Built-in Functions with Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Bob", 32)
print("Has attribute 'age'?", hasattr(p, 'age'))  # True
setattr(p, 'gender', 'Male')
print("Gender:", getattr(p, 'gender'))            # Male


#exit()
# Example 5: Multiple Objects from Same Class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(4, 5)
print("p1:", p1.x, p1.y)  # p1: 1 2
print("p2:", p2.x, p2.y)  # p2: 4 5

# -----------------------------------------------
# Advanced Level Examples
# -----------------------------------------------

# Example 6: Objects as Function Arguments and Return Values
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def area(rect):
    return rect.width * rect.height

rect1 = Rectangle(6, 7)
print("Area of rect1:", area(rect1))  # Output: Area of rect1: 42

# Example 7: Comparing Objects
class User:
    def __init__(self, username):
        self.username = username

user1 = User("alice")
user2 = User("alice")
print("user1 == user2?", user1 == user2)           # Output: False (different objects)
print("user1 username == user2 username?", user1.username == user2.username)  # True

# Example 8: Objects with __str__ and __repr__
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book('{self.title}')"

b = Book("Python Basics")
print(str(b))   # Output: Book: Python Basics
print(repr(b))  # Output: Book('Python Basics')

# Example 9: Deep Copy vs Shallow Copy With Objects
import copy
class Data:
    def __init__(self, numbers):
        self.numbers = numbers

data1 = Data([1,2,3])
data2 = copy.copy(data1)
data3 = copy.deepcopy(data1)
data1.numbers[0] = 99
print("Shallow copy:", data2.numbers)      # [99, 2, 3]
print("Deep copy:", data3.numbers)         # [1, 2, 3]

# Example 10: Checking Object Type and Identity
class Animal:
    pass

dog = Animal()
cat = Animal()
print("Is dog Animal?", isinstance(dog, Animal))  # True
print("dog and cat identical?", dog is cat)       # False

# -----------------------------------------------
# Mini-Project: Library Book Lending System
# -----------------------------------------------

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_lent = False

    def lend(self):
        if not self.is_lent:
            self.is_lent = True
            print(f"Lending out '{self.title}' by {self.author}")
        else:
            print(f"'{self.title}' is already lent!")

    def return_book(self):
        if self.is_lent:
            self.is_lent = False
            print(f"Returned '{self.title}' by {self.author}")
        else:
            print(f"'{self.title}' was not lent out")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to library.")

    def lend_book(self, title):
        for book in self.books:
            if book.title == title:
                book.lend()
                return
        print("Book not found in library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print("Book not found in library.")

    def show_books(self):
        print("Books in library:")
        for book in self.books:
            status = "Available" if not book.is_lent else "Lent"
            print(f"- {book.title} by {book.author} [{status}]")

# Demo for Mini-project
lib = Library()
book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("Python Programming", "Author X")
lib.add_book(book1)
lib.add_book(book2)
lib.show_books()
lib.lend_book("The Alchemist")
lib.show_books()
lib.return_book("The Alchemist")
lib.show_books()

'''
-----------------------------------
Interview Questions and Answers: Object in Python
-----------------------------------

Q1. What is an object in Python? How is it different from a class?  
A1. An object is an instance of a class; it represents specific data and can use methods defined in the class. A class is just a blueprint, while an object is a real, usable entity:
    class Fruit: pass
    apple = Fruit()  # apple is an object (instance), Fruit is a class.

Q2. How do you add, access, modify and delete an attribute in a Python object at runtime?  
A2. Use setattr() to add/modify, getattr() to access, and delattr() to delete.
    class Foo: pass
    f = Foo()
    setattr(f, 'bar', 100)    # Add/Modify
    print(getattr(f, 'bar'))  # 100
    delattr(f, 'bar')         # Delete

Q3. How does Python determine if two objects are equal or identical? What's the difference between == and "is"?
A3. '==' checks value equality (via __eq__ method), "is" checks identity (same memory location).
    a = [1,2]
    b = [1,2]
    print(a == b)  # True (values equal)
    print(a is b)  # False (different objects)

Q4. How can Python objects be used to achieve data encapsulation?  
A4. By defining attributes as private (prefix '__'), direct access is restricted:
    class A:
        def __init__(self):
            self.__secret = 42
        def get_secret(self):
            return self.__secret
    a = A()
    # a.__secret -> AttributeError
    print(a.get_secret())  # 42

Q5. What is the __init__ method? Is it a constructor?  
A5. __init__ is an initializer called after object creation to assign initial values to attributes. It's not a true constructor (object already exists), but is conventionally used as one in Python.

Q6. Can you use objects as dictionary keys?  
A6. Only if they are hashable (i.e., if the class implements __hash__ and __eq__ appropriately). Immutable built-in types (like str, tuple) are hashable.

Q7. What happens if you assign an object to another variable?  
A7. Both variables reference the same object (shallow copy):
    a = [10]
    b = a
    b.append(20)
    print(a)  # [10, 20]

Q8. Explain __str__ and __repr__ methods in object context.
A8. __str__ defines human-readable string representation; __repr__ is for unambiguous representation (for debugging).
    class C:
        def __str__(self): return "Nice!"
        def __repr__(self): return "C()"
    c = C(); print(c)      # Nice!
    print(repr(c))         # C()

Q9. How do you copy objects in Python?  
A9. The copy module allows for shallow (copy.copy) and deep copy (copy.deepcopy). Shallow copy duplicates object reference level, deep copies nested objects.

Q10. Give a real-world example of using objects in a large project.
A10. In a banking app, 'Account' objects represent user accounts, each with attributes (balance, id, owner) and methods (deposit, withdraw). Functionality is implemented by creating and interacting with such objects through business logic.

'''
