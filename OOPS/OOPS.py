"""
Object-Oriented Programming (OOPS) in Python
--------------------------------------------

Definition:
-----------
Object-Oriented Programming (OOPS) is a programming paradigm that uses "objects" to design software. Objects are instances of classes, containing both data (attributes) and methods (functions). OOPS enables code reusability, modularity, abstraction, encapsulation, inheritance, and polymorphism.

Key OOPS Concepts:
------------------
1. Class: Blueprint for creating objects.
2. Object: Instance of a class.
3. Encapsulation: Hiding internal data and methods, exposing only as necessary.
4. Abstraction: Hiding complexity by exposing only essential features.
5. Inheritance: Creating new classes from existing ones, inheriting attributes and methods.
6. Polymorphism: Ability to use a unified interface/functions for different data types.

-----------------------------------
Syntax of OOPS in Python
-----------------------------------

# Defining a class
class ClassName:
    def __init__(self, params):
        # constructor - initializes object
        self.attr = value

    def some_method(self, more_params):
        # method (function inside class)
        pass

# Creating an object (instance)
obj = ClassName(args)

# Inheritance Example
class ChildClass(ParentClass):
    def __init__(self, params):
        super().__init__(params)
        # more initialization

    # overriding method
    def some_method(self):
        pass

-----------------------------------
Beginner Level Examples
-----------------------------------

# Example 1: Simple Class and Object
class Dog:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

d = Dog("Rex", 3)
print(d.name)      # Output: Rex
d.bark()           # Output: Rex is barking!

# Example 2: Encapsulation with Attributes
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # private attribute: encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acct = BankAccount(100)
acct.deposit(50)
print(acct.get_balance())     # Output: 150

-----------------------------------
Intermediate Level Examples
-----------------------------------

# Example 3: Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Cat(Animal):  # Inheriting from Animal
    def speak(self):   # Method overriding (Polymorphism)
        print(f"{self.name} says Meow!")

c = Cat("Mittens")
c.speak()           # Output: Mittens says Meow!

# Example 4: Using super()
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)     # calling parent constructor
        self.model = model

    def info(self):
        print(f"Car: {self.brand} {self.model}")

car1 = Car("Toyota", "Camry")
car1.info()         # Output: Car: Toyota Camry

# Example 5: Class vs Instance Attributes
class Student:
    school = "ABC High School"     # class attribute

    def __init__(self, name):
        self.name = name           # instance attribute

s1 = Student("Riya")
s2 = Student("Rahul")
print(s1.school)    # Output: ABC High School
print(s1.name)      # Output: Riya

# Changing class attribute
Student.school = "XYZ School"
print(s2.school)    # Output: XYZ School

-----------------------------------
Advanced Level Examples
-----------------------------------

# Example 6: Abstraction using Abstract Base Classes (ABC)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print("Circle Area:", circle.area())  # Output: 78.5

# Example 7: Multiple Inheritance
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

child = Child()
child.skills()
# Output:
# Gardening, Programming
# Cooking, Art
# Sports

# Example 8: Operator Overloading (Polymorphism)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print("Added Points:", p3)         # Output: (4, 6)

# Example 9: Property Decorators (Encapsulation)
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

temp = Celsius()
temp.temperature = 25
print(temp.temperature)           # Output: 25
# temp.temperature = -300     # Raises ValueError

-----------------------------------
Interview Questions and Answers
-----------------------------------

Q1. What is OOPS? List the main principles.
A1. OOPS stands for Object-Oriented Programming System. Main principles: Encapsulation, Abstraction, Inheritance, and Polymorphism.

Q2. What is the difference between a class and an object?
A2. A class is a template or blueprint for creating objects. An object is an instance of a class, with real values stored in attributes.

Q3. How does Python support encapsulation?
A3. Python uses public, protected (_var), and private (__var) variable naming conventions. By prefixing an attribute with double underscore (__), it is "private" and can't be accessed directly outside the class.

Q4. What is inheritance? Give an example.
A4. Inheritance allows a class to acquire properties and methods from another. Example:
class Parent: ...  class Child(Parent): ...  # Child inherits from Parent.

Q5. What is method overriding?
A5. Method overriding occurs when a subclass defines a method with the same name as a method in its parent class, replacing the parent’s implementation.

Q6. Explain the use of super().
A6. The super() function allows you to call methods of the parent class, useful when overriding methods in a subclass.

Q7. What is polymorphism? How is it implemented in Python?
A7. Polymorphism allows objects of different classes to be treated as objects of a common superclass. In Python, this can be done with method overriding or operator overloading.

Q8. What are abstract base classes?
A8. Abstract base classes cannot be instantiated and often include one or more abstract methods that must be implemented by subclasses. Python has an abc module for this.

Q9. Can you explain multiple inheritance with an example?
A9. Multiple inheritance occurs when a class inherits from more than one parent class. Example:
class A: ...  class B: ...  class C(A, B): ...

Q10. How do you achieve data hiding in Python OOPS?
A10. By prefixing attribute names with double underscores (__), Python name-mangles the attribute making it harder to access from outside, thus achieving data hiding (encapsulation).

"""
