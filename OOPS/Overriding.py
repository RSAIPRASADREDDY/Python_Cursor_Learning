'''
Overriding in Python
----------------------

Definition:
------------
Method Overriding is an OOPS concept where a subclass provides a specific implementation for a method that is already defined in its parent class. 
It allows Python to support run-time polymorphism. The method in the child class must have the same name, parameters, and signature as in its parent.

Why Use Overriding?
---------------------
- To provide a different implementation for inherited methods.
- To extend or completely replace base class functionality.

How to Override a Method in Python:
------------------------------------
- Define a method with the same name and signature in the subclass.
- Optionally, call the superclass method using super().
- Use class inheritance.

Syntax:
---------
class Parent:
    def foo(self):
        print("Parent foo")

class Child(Parent):
    def foo(self):       # This overrides Parent.foo
        print("Child foo")

obj = Child()
obj.foo()   # Output: Child foo

'''

# Beginner Level Example

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()   # Output: Dog barks


# Example: Accessing Parent Method Using super()

class Vehicle:
    def start(self):
        print("Starting vehicle")

class Car(Vehicle):
    def start(self):
        print("Turning on Air Conditioning")
        super().start()

car = Car()
car.start()
# Output:
# Turning on Air Conditioning
# Starting vehicle


# Intermediate Example: Extra Parameters or Behavior

class Employee:
    def get_role(self):
        print("General Employee")

class Manager(Employee):
    def get_role(self):
        super().get_role()
        print("Manager")

m = Manager()
m.get_role()
# Output:
# General Employee
# Manager


# Advanced Example: Overriding __str__ and Polymorphism

class Shape:
    def area(self):
        raise NotImplementedError("Area not implemented")

    def __str__(self):
        return "This is a shape"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def __str__(self):
        return f"Circle with area: {self.area()}"

s = Circle(5)
print(s)
# Output: Circle with area: 78.5


# Advanced Example: Method Overriding with Multiple Inheritance

class Printer:
    def print_document(self):
        print("Printing from Printer")

class Scanner:
    def print_document(self):
        print("Printing from Scanner (scanned image)")

class MultiFunctionDevice(Printer, Scanner):
    def print_document(self):
        print("Printing from Multifunction Device")
        super().print_document()

mfd = MultiFunctionDevice()
mfd.print_document()
# Output:
# Printing from Multifunction Device
# Printing from Printer
# (Because of Python's MRO, Printer comes before Scanner)


# Mini Project: Library Management - Overriding Borrow Logic

'''
Mini Project: Simple Library System demonstrating Method Overriding

Requirements:
    - LibraryItem (base class) with borrow() and return_item()
    - Book and DVD (child) classes with custom borrow limits
    - Demonstrate overriding, super() usage, and polymorphism
'''

class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"{self.title} borrowed!")
        else:
            print(f"{self.title} is already borrowed.")

    def return_item(self):
        if self.borrowed:
            self.borrowed = False
            print(f"{self.title} returned!")
        else:
            print(f"{self.title} was not borrowed.")

class Book(LibraryItem):
    def borrow(self):
        if self.borrowed:
            print(f"{self.title} (Book) is already borrowed.")
        else:
            print(f"Books can only be borrowed for 14 days.")
            super().borrow()

class DVD(LibraryItem):
    def borrow(self):
        if self.borrowed:
            print(f"{self.title} (DVD) is already borrowed.")
        else:
            print(f"DVDs can only be borrowed for 3 days.")
            super().borrow()

# Usage
library_items = [Book("1984"), DVD("Inception"), Book("Python Guide")]

for item in library_items:
    item.borrow()
    item.borrow()
    item.return_item()

'''
Output:
Books can only be borrowed for 14 days.
1984 borrowed!
1984 (Book) is already borrowed.
1984 returned!
DVDs can only be borrowed for 3 days.
Inception borrowed!
Inception (DVD) is already borrowed.
Inception returned!
Books can only be borrowed for 14 days.
Python Guide borrowed!
Python Guide (Book) is already borrowed.
Python Guide returned!
'''


# Interview Questions and Answers – Overriding in Python
# ----------------------------------------------------------

'''
Q1. What is method overriding in Python? 
A1. Method overriding allows a subclass to provide a specific implementation of a method already defined by its parent. This enables dynamic polymorphism and changing or extending base class behavior.

Example:
    class A:
        def f(self): print("A")
    class B(A):
        def f(self): print("B")
    B().f() # Output: B

Q2. How is method overriding different from method overloading?
A2. Method overriding changes implementation in subclass(same name, same parameters); method overloading means multiple methods with the same name but different parameters. Python does not support method overloading directly but supports overriding.

Q3. How can you access the overridden method in the parent class from child?
A3. Using super():

    class A:
        def greet(self): print("Hello from A")
    class B(A):
        def greet(self):
            print("Hi from B")
            super().greet()
    B().greet()
    # Output: Hi from B\nHello from A

Q4. What happens if you don't override a method in subclass?
A4. The method in the parent class will be used.

Q5. Can you override special methods (like __str__, __len__) in Python? Why would you?
A5. Yes, these are called "dunder" methods. Overriding them lets you customize how objects behave with built-in functions:

    class MyList(list):
        def __str__(self):
            return "Custom List: " + super().__str__()
    print(MyList([1,2,3]))
    # Output: Custom List: [1, 2, 3]

Q6. What is the effect of method overriding in multiple inheritance scenarios? Who gets called first?
A6. Python uses the Method Resolution Order (MRO), which means the leftmost parent in the inheritance list gets called first, unless overridden in the child class.

Q7. Can you prevent a child class from overriding a method in Python?
A7. Python does not natively prevent overriding, but you can:
    - Raise NotImplementedError or custom Exception in sub-class
    - Use documentation to warn users
    - Use @final decorator (Python 3.8+) to signal intent (won't enforce at runtime by default)

Q8. Give a real-world use-case where method overriding is critical in system design.
A8. GUI widget libraries: The base Widget class defines render(). Each custom widget/button overrides render() to display uniquely. Extending/executing custom UI is only possible through overriding.

Q9. What are the risks of improper method overriding?
A9.
    - Breaking parent functionality if super() is not called when needed.
    - Incorrect method signatures (missing/extra parameters) causing runtime errors.
    - Unexpected behavior if the parent logic relied upon by other code.

Q10. How does overriding relate to runtime polymorphism?
A10. Overriding enables runtime polymorphism: references to base class objects can invoke child class implementations, letting us write generic code that adapts to the object type at runtime.

Example:
    class Payment:
        def pay(self): print("Base Payment")
    class Card(Payment):
        def pay(self): print("Card Payment")
    def process(p: Payment): p.pay()
    process(Card()) # Output: Card Payment

'''
