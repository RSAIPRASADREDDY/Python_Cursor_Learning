'''
Polymorphism in Python
------------------------

Definition:
-------------
Polymorphism is an OOPS concept where objects of different classes can be treated as 
objects of a common superclass, primarily by sharing the same interface/method names. 
It allows functions or methods to process objects differently based on their data type or class.

Benefits:
-------------
- Code becomes more flexible and extensible.
- Supports “write once, use anywhere” paradigm.
- Reduces code duplication.
- Simplifies interface for dealing with different object types.

Methods/Mechanisms of Achieving Polymorphism:
---------------------------------------------
1. Method Overriding
2. Duck Typing
3. Operator Overloading
4. Built-in Functions Supporting Polymorphism (e.g., len(), +, etc.)

Syntax of Polymorphism:
-----------------------

# 1. Function expecting any object with a .speak() method
def intro(animal):
    animal.speak()

# 2. Method Overriding
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

# 3. Operator Overloading
class MyNum:
    def __add__(self, other):
        return "Added!"

'''

# ---------------------
# Beginner Examples
# ---------------------

# Example 1: Duck Typing
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()

d = Dog()
c = Cat()
d.speak()
c.speak()
animal_sound(d)   # Output: Woof!
animal_sound(c)   # Output: Meow!

'''
# Understanding Polymorphism Better: Triggering Errors & Implementing Reverse Methods

# Example 1b: What happens if a required method is missing? (Triggering AttributeError)
class Human:
    def talk(self):
        print("Hello, I am a human.")

def intro_v2(animal):
    # Expects 'speak' method (duck typing)
    animal.speak()

h = Human()
try:
    intro_v2(h)   # This will raise an AttributeError
except AttributeError as e:
    print("Error:", e)
# Output: Error: 'Human' object has no attribute 'speak'

# Example 1c: Using hasattr for safer polymorphic code
def safe_intro(animal):
    if hasattr(animal, "speak"):
        animal.speak()
    else:
        print("This object can't speak.")

safe_intro(h)      # Output: This object can't speak.
safe_intro(d)      # Output: Woof!
safe_intro(c)      # Output: Meow!

# Example 1d: Implementing a 'reverse' method in different classes, showing polymorphism

class Word:
    def __init__(self, s):
        self.s = s
    def reverse(self):
        return self.s[::-1]

class Numbers:
    def __init__(self, nums):
        self.nums = nums
    def reverse(self):
        return self.nums[::-1]

w = Word("python")
n = Numbers([1, 2, 3, 4])

def show_reverse(obj):
    print(obj.reverse())

show_reverse(w)   # Output: nohtyp
show_reverse(n)   # Output: [4, 3, 2, 1]

'''


# Example 2: Built-in Function Polymorphism
print(len([1, 2, 3]))      # Output: 3
print(len("Hello"))        # Output: 5
print(len({'a':10, 'b':20})) # Output: 2

# -----------------------------
# Intermediate Level Examples
# -----------------------------

# Example 3: Method Overriding (Compile-time polymorphism doesn't exist in Python, but dynamic overriding does)
class Shape:
    def area(self):
        print("No area formula defined.")

class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def area(self):
        print("Area of circle:", 3.14 * self.radius * self.radius)

class Square(Shape):
    def __init__(self, s):
        self.side = s
    def area(self):
        print("Area of square:", self.side * self.side)

shapes = [Circle(2), Square(3), Shape()]
for shp in shapes: 
    #print(type(shp).__name__)
    shp.area()

# Output:
# Area of circle: 12.56
# Area of square: 9
# No area formula defined.



# Example 4: Operator Overloading

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        if isinstance(other, Book):
            print(1)
            return Book(self.pages + other.pages)
        return NotImplemented

    def __str__(self):
        print(2)
        return f"Book({self.pages} pages)"

b1 = Book(100)
b2 = Book(200)
b3 = b1 + b2
print(b3)   # Output: Book(300 pages)


# -----------------------------
# Advanced Level Examples
# -----------------------------

# Example 5: Polymorphism via Abstract Base Classes

from abc import ABC, abstractmethod

from numpy.testing import print_assert_equal

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started.")

class Bike(Vehicle):
    #pass
    def start(self):
        print("Bike started with a kick.")

vehicles = [Car(), Bike()]
for v in vehicles:
    v.start()
# Output:
# Car engine started.
# Bike started with a kick.


#exit()
# Example 6: Custom Polymorphic Collection

class PayPal:
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

def process_payment(payment_method, amount):
    payment_method.pay(amount)

for method in [PayPal(), CreditCard()]:
    process_payment(method, 50)

# Output:
# Paid 50 using PayPal.
# Paid 50 using Credit Card.

# -----------------------------
# Mini Project: Polymorphic Drawing Application
# -----------------------------
'''
Mini Project: Drawing Shapes with Polymorphism
-------------------------------------

Requirements:
- Create classes for different shapes: Rectangle, Circle, Triangle.
- Each must implement a common interface to calculate area and draw itself.
- Use polymorphism to process a list of shapes without knowing their concrete types.

'''

from abc import ABC, abstractmethod

class DrawingShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Rectangle(DrawingShape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def draw(self):
        print(f"Drawing Rectangle of width {self.w} and height {self.h}")

class Circle(DrawingShape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
    def draw(self):
        print(f"Drawing Circle of radius {self.r}")

class Triangle(DrawingShape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return 0.5 * self.b * self.h
    def draw(self):
        print(f"Drawing Triangle with base {self.b} and height {self.h}")

shapes = [Rectangle(4, 5), Circle(3), Triangle(6, 2)]

total_area = 0
for shape in shapes:
    shape.draw()
    a = shape.area()
    print(f"Area: {a}")
    total_area += a

print(f"Total Area of all shapes: {total_area}")

# Sample Output:
# Drawing Rectangle of width 4 and height 5
# Area: 20
# Drawing Circle of radius 3
# Area: 28.26
# Drawing Triangle with base 6 and height 2
# Area: 6.0
# Total Area of all shapes: 54.26

# -----------------------------
# Interview Questions and Answers - Polymorphism
# -----------------------------

'''
Q1. What is polymorphism in Python and why is it important?
A1. Polymorphism means "many forms". In Python, it allows objects of different classes to be treated as objects of a common superclass, mainly by sharing method names. It's important for code extensibility, simplicity, and for writing code that can process a variety of data types using a shared interface.

Q2. Explain method overriding with an example.
A2. Method overriding occurs when a derived class defines a method with the same name as a parent class. Example:
    class Animal:
        def speak(self): print("Animal speaks")
    class Dog(Animal):
        def speak(self): print("Bark")
    Dog().speak() # Output: Bark

Q3. Give a real-world scenario where duck typing enables polymorphism.
A3. Example: A payment system that allows different classes such as PayPal, CreditCard, UPI, etc., which all have a pay(amount) method. The system calls pay(amount) without caring about the concrete class, only trusting the method exists. This is duck typing: "If it quacks like a duck...".

Q4. What is operator overloading and how does it relate to polymorphism?
A4. Operator overloading allows us to redefine how operators work for user-defined types (classes). By implementing special methods like __add__, __mul__, etc., objects of a class can support operators, e.g., Book + Book could sum pages. This is a form of compile-time polymorphism.

Q5. How do abstract base classes (ABC) support polymorphism?
A5. ABCs define a set of methods that must be implemented by subclasses, enforcing an interface that enables polymorphism; we know that every subclass will provide those methods, so we can process ABC references without knowing the concrete class.

Q6. What will happen if two unrelated classes implement the same method name? Does Python consider it polymorphism?
A6. Yes, due to duck typing, as long as the method exists, Python can process any object with that method (e.g., .sound()). This is polymorphism in Python via duck typing.

Q7. Is Python's polymorphism static or dynamic? Explain with an example.
A7. Python supports dynamic (runtime) polymorphism: method resolution occurs at runtime, not compile time. For example, in a loop over objects of different classes with the same .draw() method, the resolution of which draw() to call happens when the line is run.

Q8. Can you restrict the type of objects that participate in polymorphism in Python?
A8. By convention, you can, but Python is generally dynamically typed, so it doesn't enforce restrictions. However, you can use ABCs/metaclasses or isinstance checks to restrict or validate the interface.

Q9. Show an example where using polymorphism reduces code duplication.
A9.
    class Email:
        def send(self): print("Email sent")
    class SMS:
        def send(self): print("SMS sent")

    def notify(channel):
        channel.send()

    for c in [Email(), SMS()]:
        notify(c)
    # Without polymorphism, you'd have to write separate if-else logic for sending via Email or SMS.

Q10. How can polymorphism be abused, and what should a developer be careful about?
A10. If you rely on duck typing, but methods are missing, you get runtime errors. So, document interfaces clearly or use ABCs. You should also ensure objects provided as arguments actually have the needed methods to avoid AttributeErrors at runtime.

'''
