"""
Inheritance in Python
# ---------------------
Definition:
# -----------
Inheritance is an Object-Oriented Programming concept that allows a class (child/derived/subclass) to inherit 
attributes and methods from another class (parent/base/superclass), facilitating code reuse, extension, and maintenance.

Benefits:
# ---------
- Promotes code reusability.
- Supports extensibility and scalability.
- Implements hierarchical relationships.

Key Methods/Features:
# ---------------------
- super(): Calls methods/constructors of the parent class.
- Overriding: Redefining parent methods in a child class.
- Multiple Inheritance: Inheriting from multiple parents.
- Multilevel Inheritance: Deriving a class from another derived class.
- Hierarchical Inheritance: Multiple classes inherit from the same parent.

Syntax:
# -------
# Single Inheritance
class Parent:
    # parent members
    pass

class Child(Parent):
    # child members
    pass

# Multiple Inheritance
class A: ...
class B: ...
class C(A, B): ...

# Using super()
class Child(Parent):
    def __init__(self):
        super().__init__()

# -----------------------------
# Beginner Level Examples
# -----------------------------
"""

# Example 1: Basic Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()   # Output: Animal speaks

# Example 2: Overriding Parent Method
class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying low")

b = Bird()
s = Sparrow()
b.fly()   # Output: Bird is flying
s.fly()   # Output: Sparrow is flying low

# Example 3: Demonstrating super() and "reverse" calls

# Deep understanding with reverse methods in inheritance:
# Sometimes, you may want to call the parent (or even grandparent) method from the subclass,
# possibly executing child logic before/after the parent logic.
# Additionally, you may want to traverse the MRO (Method Resolution Order) "in reverse" (i.e., from child up), 
# especially in complex inheritance (like multiple inheritance).

class Base:
    def greet(self):
        print("Hello from Base")

class Middle(Base):
    def greet(self):
        print("Hello from Middle, before Base")
        super().greet()     # Calls up the chain (parent/Base)
        print("Hello from Middle, after Base")

class ChildMost(Middle):
    def greet(self):
        print("Hello from ChildMost, before Middle")
        super().greet()     # Calls Middle.greet
        print("Hello from ChildMost, after Middle")
        
cm = ChildMost()
cm.greet()
# Output:
# Hello from ChildMost, before Middle
# Hello from Middle, before Base
# Hello from Base
# Hello from Middle, after Base
# Hello from ChildMost, after Middle
# Error Handling Techniques in Inheritance Context

'''
#===ERROR HANDLING TECHNIQUES IN INHERITANCE CONTEXT===
# 1. Handling AttributeError when accessing non-existent attributes (common in inheritance when parents/children differ)
class Parent:
    def existing_method(self):
        print("Parent method.")

class Child(Parent):
    pass

child = Child()
try:
    child.non_existing_method()
except AttributeError as e:
    print("Caught AttributeError:", e)


# 2. Handling NotImplementedError in abstract-like methods
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement 'speak' method.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Fish(Animal):
    pass

dog = Dog()
dog.speak()  # Woof!
fish = Fish()
try:
    fish.speak()
except NotImplementedError as e:
    print("Caught NotImplementedError:", e)


# 3. Using try-except to handle issues in overridden methods
class FileParent:
    def open(self):
        print("Opening resource...")

class FileChild(FileParent):
    def open(self):
        try:
            # Simulate error (e.g., file not found)
            raise FileNotFoundError("File missing.")
        except FileNotFoundError as e:
            print("Handled in child:", e)
            super().open()  # Optionally fall back to parent implementation

fc = FileChild()
fc.open()


# 4. Ensuring correct argument passing with super(), raising TypeError if needed
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        try:
            super().__init__(name)  # Make sure this is passed!
            self.emp_id = emp_id
        except TypeError as e:
            print("Caught TypeError (incorrect constructor arguments):", e)

# Bad call, missing name
try:
    e = Employee(emp_id=101, name=None)  # name is None, not omitted, so works here, but demo for handling
except Exception as e:
    print("General Exception:", e)

# 5. Catching issues in method resolution order (rare, but possible in complicated inheritance)
class A:
    def do(self):
        print("A.do()")

class B(A):
    pass

class C(A):
    def do(self):
        print("C.do()")

class D(B, C):
    def do(self):
        try:
            super().do()
        except Exception as e:
            print("Error during super() resolution:", e)

d = D()
d.do()   # Should call C.do() because of MRO
'''
#exit()

#====REVERSE METHOD IN INHERITANCE CONTEXT====
'''
# "Reverse" method: calling all methods up the inheritance chain.
# Let's see the MRO for objects:
def print_mro(cls):
    print(f"MRO for {cls.__name__}:")
    for c in cls.__mro__:
        print(" ", c.__name__)

print_mro(ChildMost)
# Output will be: ChildMost, Middle, Base, object



# Suppose you want to explicitly call all greet() methods up the MRO
# (bypassing super and calling directly—generally not recommended, but useful to understand):

print("\nCalling all .greet() up the MRO (manually):")
instance = ChildMost()
for cls in ChildMost.__mro__:
    if 'greet' in cls.__dict__:
        cls.greet(instance)

# Output:
# Hello from ChildMost, before Middle
# Hello from Middle, before Base
# Hello from Base
# Hello from Middle, after Base
# Hello from ChildMost, after Middle

# Note: This is for learning. Normally, you would use super() and let MRO handle chained calls.

'''

# -----------------------------
# Intermediate Level Examples
# -----------------------------

# Example 3: super() to Call Parent Method
class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car started")

c = Car()
c.start()
# Output:
# Vehicle starting...
# Car started

# Example 4: Multilevel Inheritance
class Grandparent:
    def feature(self):
        print("Feature from Grandparent")

class Parent(Grandparent):
    def feature(self):
        print("Feature from Parent")

class Child(Parent):
    def feature(self):
        print("Feature from Child")

c = Child()
c.feature()         # Output: Feature from Child
super(Child, c).feature()  # Output: Feature from Parent

# Example 5: Hierarchical Inheritance
class Shape:
    def area(self):
        print("Shape area")

class Rectangle(Shape):
    def area(self):
        print("Rectangle area = length * breadth")

class Circle(Shape):
    def area(self):
        print("Circle area = π * r^2")

shapes = [Rectangle(), Circle()]
for shape in shapes:
    shape.area()
# Output:
# Rectangle area = length * breadth
# Circle area = π * r^2

# -----------------------------
# Advanced Level Examples
# -----------------------------

# Example 6: Multiple Inheritance and MRO
class Father:
    def skills(self):
        print("Father: Gardening, Programming")

class Mother:
    def skills(self):
        print("Mother: Cooking, Art")

class Child(Father, Mother):
    def skills(self):
        super().skills()
        print("Child: Sports")

c = Child()
c.skills()
# Output:
# Father: Gardening, Programming
# Child: Sports

# Example 7: Diamond Problem in Multiple Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()
# Output: B   (B comes before C in D's MRO)

print(D.mro())  # Print Method Resolution Order

# Example 8: Using isinstance and issubclass
print(isinstance(c, Child))        # True
print(isinstance(c, Father))       # True
print(issubclass(Child, Father))   # True

# -----------------------------
# Mini Project: Employee Management System with Inheritance
# -----------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, prog_lang):
        super().__init__(name, salary)
        self.prog_lang = prog_lang

    def show(self):
        print(f"Developer: {self.name}, Salary: {self.salary}, Language: {self.prog_lang}")

class Manager(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team  # a list of Employees

    def show(self):
        print(f"Manager: {self.name}, Salary: {self.salary}, Team Size: {len(self.team)}")
        print("Team Members:")
        for emp in self.team:
            emp.show()

# Example Usage
dev1 = Developer("Alice", 85000, "Python")
dev2 = Developer("Bob", 90000, "Java")
mgr = Manager("Charlie", 120000, [dev1, dev2])
mgr.show()
# Output:
# Manager: Charlie, Salary: 120000, Team Size: 2
# Team Members:
# Developer: Alice, Salary: 85000, Language: Python
# Developer: Bob, Salary: 90000, Language: Java

'''
---------------------------------------------
Interview Questions and Answers - Inheritance
---------------------------------------------

Q1. What is inheritance in Python and why is it useful?
A1. Inheritance lets a class acquire methods and properties of another class. It promotes code reusability, makes code extensible, and supports hierarchical class relationships, e.g., multiple types of users or objects that share common functionality.

Q2. What types of inheritance does Python support? Give examples.
A2. Python supports Single, Multiple, Multilevel, Hierarchical, and Hybrid inheritance.
- Single: class B(A): ...
- Multiple: class C(A, B): ...
- Multilevel: class C(B), B(A): ...
- Hierarchical: Many classes inherit from same parent.
Example for Multiple:
    class A: ...
    class B: ...
    class C(A, B): ...

Q3. How does Python resolve method calls in multiple inheritance (the diamond problem)?
A3. Python uses the Method Resolution Order (MRO) which follows the C3 linearization algorithm. `super()` uses MRO to determine call order. Example:
    class A: def show(self): print("A")
    class B(A): def show(self): print("B")
    class C(A): def show(self): print("C")
    class D(B, C): pass
    D().show()  # Output: B

Q4. Explain the use and importance of the `super()` function in inheritance.
A4. `super()` allows you to call methods from a parent or sibling class dynamically, avoiding hard-coding the parent class name and supporting MRO in multiple inheritance scenarios. It is especially useful to properly initialize parent classes in subclass constructors.

Q5. What happens if a child class does not override a method from the parent class?
A5. The method from the parent class is inherited and used as-is. If the child class defines a method with the same name, it overrides the parent method.

Q6. How can you check if an object is an instance or subclass of another class?
A6. Use `isinstance(obj, Class)` to check object type, and `issubclass(Sub, Super)` to check class relationship.

Q7. Can a child class access private members of its parent class?
A7. No, private members (prefixed with __) are name-mangled and not accessible directly. They can be accessed indirectly if the parent provides protected/public methods.

Q8. Can you give a real-world scenario where inheritance is advantageous?
A8. In a company, you might have a base `Employee` class and derived classes like `Developer`, `Manager`, etc., that share common attributes and override role-specific behaviors.

Q9. What are abstract base classes, and how do they relate to inheritance?
A9. Abstract base classes (ABCs) define methods that must be implemented by subclasses, enforcing interface contracts. Python's abc module is used for ABCs. They use inheritance to force derived classes to implement certain methods.

Q10. How does Python’s MRO differ from C++/Java’s method resolution in multiple inheritance?
A10. Python’s MRO uses C3 linearization algorithm which provides a deterministic order for method lookup, while C++ uses depth-first and Java doesn’t support multiple inheritance for classes (only interfaces).
'''
