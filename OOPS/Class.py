"""
Classes in Python
-----------------

Definition:
-----------
A class in Python is a blueprint for creating objects (instances). 
Classes encapsulate data for the object and define behaviors through methods.

Key Methods and Usages:
-----------------------
- __init__(self, ...): Constructor/initializer
- self: Represents the instance of the class
- Instance methods: Functions defined with 'self' as the first argument
- Class methods: Use @classmethod decorator, receive 'cls'
- Static methods: Use @staticmethod decorator, do not receive instance/class as first arg
- __str__, __repr__: String representations
- __del__: Destructor
- __eq__, __lt__, __add__...: Operator overloading

Syntax:
-------
# Class definition
class ClassName:
    def __init__(self, params):
        self.attr = value  # instance variable

    def method(self, params):
        # method body
        pass

# Creating object
obj = ClassName(args)
obj.method(args)
"""

# ----------------------------------------------
# Beginner Level Examples
# ----------------------------------------------

# Example 1: Basic Class and Object
from tkinter import S


class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}.")

# p = Person("Alice",20)
# p.say_hello()  # Output: Hello, my name is Alice.
# print(p.age)  # Output: 20


# Example: Common Errors When Creating Classes and Objects

# 1. Typo in Class Name (case-sensitive)
# Uncomment to see the error:
#p = person("Bob", 25)  # NameError: name 'person' is not defined (should be 'Person')

# 2. Missing Required Arguments
# Uncomment to see the error:
#p = Person("Bob")  # TypeError: __init__() missing 1 required positional argument: 'age'

# 3. Forgetting 'self' in Method Definition
# This will raise an error when calling say_hello
# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def speak(Self):  # Missing 'self'
#         print(f"Meow! {Self.name}")

# c = Cat("Tom")
# c.speak()  # TypeError: speak() takes 0 positional arguments but 1 was given

# 4. Accessing Nonexistent Attributes
# p = Person("Eve", 35)
# print(p.height)  # AttributeError: 'Person' object has no attribute 'height'

# 5. Instantiating a Class Without Parentheses
# obj = Person  # This only assigns the class, doesn't create an object
# print(type(obj))    # <class '__main__.Person'>

# # Do this instead:
# obj2 = Person("Raj", 28)
# print(obj2.name)  # Raj

# You can experiment with the above examples by uncommenting each section one at a time
# to observe the types of errors that occur. This will help reinforce good class/object practices.



# Example 2: Assigning and Accessing Attributes
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def windows(self):
        windows = 4
        print(f"Brand: {self.brand} car is having a {windows} windows in year {self.year}")

# my_car = Car("Toyota", 2020)
# print(my_car.brand)  # Output: Toyota
# print(my_car.year)   # Output: 2020
# my_car.windows()


# ----------------------------------------------
# Intermediate Level Examples
# ----------------------------------------------

# Example 3: Class Variables vs Instance Variables
class Student:
    school = "ABC High School"  # Class variable
    
    def __init__(self, name):
        self.name = name      # Instance variable

    def display(self):
        self.school="ZP high school"
        location="kowthalam"
        print(f"Name: {self.name} and School: {self.school} in {location}")

s1 = Student("sai")
s2 = Student("Shrihansh")
# print(s1.name, s1.school)  # John ABC High School
# print(s2.name, s2.school)  # Jane ABC High School
# s1.display()
# s2.display()


# Intentionally trigger and observe common class/instance pitfalls:

print("\n--- Reverse/Error triggering for learning ---")

# 1. Accessing class variable via instance and via class
# print(Student.school)     # OK: access via class

# try:
#     print(s1._school)    # AttributeError: _school does not exist (typo); should be school
# except AttributeError as e:
#     print("Error:", e)


# 2. Assign and check class variable shadowing
# s1.school = "New School"       # This creates/assigns an instance attribute
# print("s1.school (instance):", s1.school)    # New School
# print("s2.school (class):", s2.school)       # ABC High School - still from class
# print("Student.school (class):", Student.school) # ABC High School


# 3. Delete an attribute
#del s1.school   # deletes instance variable "school" from s1
#print("After deleting s1.school, accessing s1.school:", s1.school)  # Falls back to class variable



# 4. Call display() on a string (not an instance)
# try:
#     Student.display()  #This will raise an error because display is an instance method and not a class method
#     #Student.display(s1)
# except Exception as e:
#     print("Error (calling instance method with wrong type):", e)



# 5. Calling display with missing argument
# try:
#     s1.display("extra_arg")
# except TypeError as e:
#     print("TypeError (too many arguments):", e)


# 6. Calling constructor with missing arguments
# try:
#     bad_student = Student()
# except TypeError as e:
#     print("TypeError (missing arguments):", e)


# 7. Accessing attribute before assignment
# class Test:
#     def show(self):
#         print(self.x)

# try:
#     t = Test()
#     #t.x="1"
#     t.show()
# except AttributeError as e:
#     print("AttributeError (attribute not set):", e)



# Example 4: Using __str__ Method
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

# b = Book('Python Basics')
# print(str(b))  # Output: Book: Python Basics





# Example 5: Class Method and Static Method
class MathOps:
    base = 10

    @classmethod
    def get_base(cls):
        return cls.base

    @staticmethod
    def add(x, base):
        return x + base

# print(MathOps.get_base())      # Output: 10
# print(MathOps.add(5, MathOps.base))      # Output: 12





# ----------------------------------------------
# Advanced Level Examples
# ----------------------------------------------

# Example 6: Inheritance
class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# d = Dog()
# d.speak()  # Output: Woof!


# Example 7: Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"<{self.x}, {self.y}>"

v1 = Vector(1, 2)
print(str(v1))
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: <4, 6>

# Example 8: Private Attributes and Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Bob", 1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
# print(acc.__balance)   # Error: AttributeError

# Example 9: Abstract Base Classes (abc module)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

c = Circle(5)
print(c.area())  # Output: 78.5

# Example 10: Multiple Inheritance
class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Art")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

kid = Child()
kid.skills()
# Output:
# Gardening, Programming
# Cooking, Art
# Sports

# ----------------------------------------------
# Mini Project: Simple Library Management System using Classes
# ----------------------------------------------

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book_title):
        self.books.append(book_title)
        print(f"Book '{book_title}' added to library.")

    def remove_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
            print(f"Book '{book_title}' removed from library.")
        else:
            print(f"Book '{book_title}' not found.")

    def display_books(self):
        print(f"Books in {self.name}:")
        for b in self.books:
            print("-", b)

# Usage
lib = Library("Town Library")
lib.add_book("Python Programming")
lib.add_book("Data Structures")
lib.display_books()
lib.remove_book("Python Programming")
lib.display_books()

'''
----------------------------------------------------------
Interview Questions and Answers (Deep, Logical, Realtime)
----------------------------------------------------------

Q1. What is the difference between a class variable and an instance variable? Give an example where their behavior differs.
A1. A class variable is shared by all instances of the class, while an instance variable is specific to the object. Example:
    class Example:
        class_var = 0
        def __init__(self):
            self.inst_var = 1

    e1 = Example()
    e2 = Example()
    e1.class_var += 1; e1.inst_var += 1
    print(e2.class_var, e2.inst_var) # Output: 0 1 (class_var is shadowed in instance)

Q2. How is data encapsulation achieved in Python? Can you bypass it? Is it secure?
A2. Encapsulation is done by prefixing attributes with '__' (private). Python uses name mangling, so it's not strictly private.
    class Demo:
        def __init__(self):
            self.__x = 10
    d = Demo()
    # print(d.__x)      # Fails
    print(d._Demo__x)  # 10   (bypassed using name mangling)

Q3. When and why do you use @staticmethod and @classmethod? Illustrate with an example.
A3. @staticmethods don't access class or instance; use for utility functions. @classmethods receive the class itself as first parameter:
    class Demo:
        count = 0
        @classmethod
        def increment(cls): cls.count += 1
        @staticmethod
        def greeting(): print("Hi!")

Q4. How does Python implement operator overloading? Show a practical example.
A4. By defining magic methods like __add__, __eq__, etc.
    class Point:
        def __init__(self, x): self.x = x
        def __add__(self, o): return Point(self.x + o.x)
    p1, p2 = Point(2), Point(3)
    p3 = p1 + p2
    print(p3.x)  # 5

Q5. What is an abstract base class? Why is it useful?
A5. Abstract base class (ABC) can't be instantiated. It defines a common interface with abstract methods that derived classes must implement, enforcing design contracts, e.g.:
    from abc import ABC, abstractmethod
    class Animal(ABC):
        @abstractmethod
        def sound(self): pass

Q6. What happens if object reference is deleted in Python? When is __del__ called?
A6. If no references remain, Python’s garbage collector destroys the object and calls its __del__ destructor (not deterministic timing).

Q7. How do you create an immutable class in Python?
A7. By overriding __setattr__, or using __slots__, or making attributes read-only:
    class Const:
        def __init__(self, val): self.__val = val
        @property
        def val(self): return self.__val
        @val.setter
        def val(self, value): raise AttributeError("Read-only")

Q8. Can you use objects as dictionary keys? What is required?
A8. Only hashable (immutable & implements __hash__ and __eq__). By default, user objects are hashable unless __eq__ is overridden.

Q9. How do you implement polymorphism with classes in Python?
A9. By method overriding (same method, different class) or duck typing.
    class A:
        def show(self): print("A")
    class B:
        def show(self): print("B")
    for obj in [A(), B()]:
        obj.show()

Q10. Give a real project scenario where Python classes enabled modular, scalable design.
A10. In a web application, different types of users (Admin, Customer, Guest) can be implemented as classes inheriting from a User base class with shared and overridden methods, enabling role-based access and extensibility.
'''
