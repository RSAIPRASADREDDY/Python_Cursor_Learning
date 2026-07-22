'''
Overloading in Python
--------------------
Definition:
------------
Overloading is a concept in object-oriented programming where two or more methods in the same scope have the same name but different signatures (i.e., parameter types, numbers, or both). Python does not support traditional method overloading (like Java or C++), but provides flexibility via default arguments, variable arguments, and special (magic/dunder) methods for operator overloading.

Types of Overloading in Python:
-------------------------------
1. Function/Method Overloading: 
   - Multiple ways of initializing or calling the same method with different parameters.
   - Achieved using default values or *args and **kwargs.
2. Operator Overloading:
   - Defining custom behavior for operators (+, -, *, etc.) for user-defined objects via special methods like __add__, __mul__, __str__, etc.

Syntax and Methods:
-------------------
- Use *args and **kwargs to write flexible functions/methods.
- Use default arguments in methods.
- Redefine special methods like __add__, __eq__, etc., for operator overloading.

'''

# Method Overloading Example (Beginner Level)
print("---- Method Overloading using default args ----")
class Greet:
    def hello(self, name=None):
        if name is not None:
            print("Hello, " + name)
        else:
            print("Hello, Guest")

g = Greet()
g.hello()
g.hello("Alice")

# Method Overloading using *args (Intermediate Level)
print("\n---- Method Overloading using *args ----")
class Sum:
    def total(self, *args):
        return sum(args)
s = Sum()
print(s.total(3, 4))
print(s.total(1, 2, 3, 4))
print(s.total())  # 0 if no args

# Operator Overloading (Beginner to Advanced)
'''
Operator overloading allows custom objects to interact with built-in operators.
'''
print("\n---- Operator Overloading (Addition) ----")
class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        return Book(self.pages + other.pages)
    def __str__(self):
        return f"Book with {self.pages} pages"
b1 = Book(100)
b2 = Book(150)
b3 = b1 + b2
print(b3)  # Book with 250 pages

print("\n---- Operator Overloading (Comparison) ----")
class Employee:
    def __init__(self, salary):
        self.salary = salary
    def __gt__(self, other):
        return self.salary > other.salary
e1 = Employee(50000)
e2 = Employee(60000)
print(e1 > e2)  # False

# Advanced Example: Vector Class with Multiple Operator Overloads
print("\n---- Advanced: Operator Overloading for a 2D vector ----")
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
v4 = v2 - v1
v5 = v1 * 5
print(v3)   # Vector(5, 7)
print(v4)   # Vector(1, 1)
print(v5)   # Vector(10, 15)
print(v1 == v2)  # False

# Mini Project: Shopping Cart with Operator Overloading
'''
Mini Project: Shopping Cart
--------------------------
You can use overloading to add two Cart objects together (combining their items) or compare their total value.
'''
print("\n---- Mini Project: Shopping Cart with Operator Overloading ----")
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name}: ${self.price}"

class Cart:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def __add__(self, other):
        new_cart = Cart()
        new_cart.items = self.items + other.items
        return new_cart
    def total(self):
        return sum(item.price for item in self.items)
    def __gt__(self, other):
        return self.total() > other.total()
    def __str__(self):
        return "\n".join([str(item) for item in self.items]) + f"\nTotal: ${self.total()}"

cart1 = Cart()
cart1.add_item(Item("Book", 12))
cart1.add_item(Item("Pen", 3))
cart2 = Cart()
cart2.add_item(Item("Laptop", 900))
cart2.add_item(Item("Mouse", 20))
cart3 = cart1 + cart2
print("Combined Cart:\n", cart3)
print("cart1 > cart2? ", cart1 > cart2)

'''
Interview Questions and Answers - Overloading in Python
------------------------------------------------------

Q1. What is method overloading? Does Python support it directly?
A1. Method overloading allows multiple methods with the same name but different parameter lists in the same scope. Python does not support method overloading in the classical sense—if you define a method twice, only the latest definition is used. However, you can mimic overloading using default arguments, *args, or **kwargs.

Example:
    class Demo:
        def show(self, x=None, y=None):
            if x and y:
                print(x, y)
            elif x:
                print(x)
            else:
                print("empty")
    Demo().show(10)  # Output: 10

Q2. What is operator overloading? Give a practical example in Python.
A2. Operator overloading enables defining custom behavior for operators when applied to user-defined objects. For example, two Box objects can use the '+' operator to sum their volumes.

    class Box:
        def __init__(self, w, h, d):
            self.volume = w * h * d
        def __add__(self, other):
            return Box(1,1,self.volume + other.volume)
    b1 = Box(2,2,2); b2 = Box(2,3,4)
    b3 = b1 + b2  # b3.volume = 8 + 24 = 32

Q3. Can you overload all operators in Python? Mention any restrictions.
A3. Most operators (+, -, *, /, ==, >, <, etc.) can be overloaded using special methods (__add__, __eq__, ...). However, some operators like logical 'and', 'or', 'not', and conditional expressions cannot be user-overloaded.

Q4. How would you design a math library object that supports both addition with numbers and with its own type?
A4. By implementing both __add__ and __radd__ magic methods:
    class Number:
        def __init__(self, value): self.value = value
        def __add__(self, other):
            if isinstance(other, Number):
                return Number(self.value + other.value)
            elif isinstance(other, (int, float)):
                return Number(self.value + other)
            else:
                return NotImplemented
        __radd__ = __add__
    print(Number(5) + 10)   # 15
    print(10 + Number(5))   # 15

Q5. In python, if you want to simulate function overloading for validation functions, how would you do it?
A5. Use *args or **kwargs to detect the type/number of arguments at runtime and branch logic accordingly.

    def validate(*args):
        if len(args) == 1 and isinstance(args[0], str):
            print("Validating string")
        elif len(args) == 2:
            print("Validating two args")
        else:
            print("Unknown validation")
    validate("abc")   # Validating string

Q6. What are the drawbacks of using operator overloading improperly?
A6.
    - Code becomes less readable if operator meaning is not intuitive.
    - Can lead to unexpected bugs if overloading doesn't follow Python's operator semantics.
    - Too much custom behavior can confuse other developers.

Q7. How does operator overloading relate to polymorphism and inheritance?
A7. Operator overloading is a form of compile-time (static) polymorphism—same operator acts differently on different types. Inheritance allows you to override/extend the overloaded operators further in derived classes for more complex behaviors.

Q8. Why can't you overload methods based only on type of arguments in Python?
A8. Because Python uses dynamic typing: at runtime, only the latest method definition is used. It does not enforce argument type signatures like Java/C++.

Q9. How do *args and **kwargs enable flexible pseudo-overloading patterns?
A9. They allow you to accept an arbitrary number of positional and keyword arguments, enabling method logic to branch and "act overloaded" based on argument presence, count, order, or types.

Q10. Give a real-world scenario where overloading adds value to application code.
A10. In a data analytics library, you might want vectors/matrices to be addable/multipliable via operators, lists to be appended like v1 + v2, customizing sorting, summing, etc., all via operator overloading for intuitive code.

'''
