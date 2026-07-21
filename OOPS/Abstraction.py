'''
Abstraction in Python
------------------------

Definition:
------------
Abstraction is an object-oriented programming principle that allows you to 
hide complex implementation details and only show the essential features of an object. 
It helps in focusing on what an object does instead of how it does it.

When to Use:
-------------
- When you want to hide complex logic from the user.
- When designing large systems for maintainability.
- When you want to enforce a contract/interface for subclasses.

How is Abstraction Achieved in Python?
--------------------------------------
1. Using Abstract Base Classes (ABC) and the @abstractmethod decorator from the 'abc' module.
2. Defining methods that must be implemented by subclasses.

Syntax:
---------
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass
'''

# Beginner Level Example: Simple Abstract Class and Implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car has started.")

c = Car()
c.start()  # Output: Car has started.

'''
Explanation:
- `Vehicle` is an abstract class with an abstract method `start`.
- `Car` inherits from `Vehicle` and implements the `start` method.
- You cannot instantiate Vehicle directly.
'''
# Error Handling & Deep Abstraction Example

from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def open(self, filepath):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def close(self):
        pass

class TextFileHandler(FileHandler):
    def __init__(self):
        self.file = None
        self._filepath = None

    def open(self, filepath):
        try:
            self.file = open(filepath, 'r')
            self._filepath = filepath
            print(f"Opened file: {filepath}")
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            self.file = None

    def read(self):
        if self.file:
            try:
                content = self.file.read()
                return content
            except Exception as e:
                print(f"Error while reading file: {e}")
        else:
            print("File not open. Cannot read.")
            return None

    def close(self):
        if self.file:
            try:
                self.file.close()
                print(f"Closed file: {self._filepath}")
                self.file = None
            except Exception as e:
                print(f"Error closing file: {e}")
        else:
            print("File already closed or was never opened.")

# Usage Example:
# tfh = TextFileHandler()
# tfh.open("test.txt")       # Handles file not found error
# content = tfh.read()       # Handles read error if file is not open
# tfh.close()                # Always safe to call

# Deep Abstraction: Layered Handler

class SafeFileHandler(TextFileHandler):
    """A TextFileHandler with deep error handling and logging."""

    def open(self, filepath):
        print("[SafeFileHandler] Attempting to open file...")
        super().open(filepath)

    def read(self):
        print("[SafeFileHandler] Attempting to read...")
        content = super().read()
        if content is None:
            print("[SafeFileHandler] Read failed.")
        return content

    def close(self):
        print("[SafeFileHandler] Attempting to close file...")
        super().close()

# Usage Example:
# sfh = SafeFileHandler()
# sfh.open("no_such_file.txt")
# data = sfh.read()
# sfh.close()

'''
Explanation:
- FileHandler is an abstract base class enforcing open/read/close contract.
- TextFileHandler implements file handling with error checks.
- SafeFileHandler deepens abstraction with user-friendly messages and extra error visibility.
- Methods always handle possible user mistakes (opening non-existent files, reading before open, double close).
'''



# Intermediate Level Example: Abstract Class with Multiple Methods

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def eat(self):
        print("Dog eats bones.")

    def sound(self):
        print("Dog barks: Woof!")

dog = Dog()
dog.eat()   # Dog eats bones.
dog.sound() # Dog barks: Woof!

'''
Explanation:
- Abstract class can have multiple abstract methods.
- Each method must be implemented by subclass.
'''

# Advanced Level Example: Partial Implementation and Abstract Properties

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def sides(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @property
    def sides(self):
        return 4

r = Rectangle(3, 5)
print(f"{r.name} has area {r.area()} and {r.sides} sides.")  # Rectangle has area 15 and 4 sides.

'''
Advanced Explanation:
- Abstract classes can have constructors and concrete methods/attributes.
- You can enforce properties as abstract.
- Subclasses must implement all abstract methods/properties.
'''

# Example: Restricting Instantiation

try:
    v = Vehicle()
except TypeError as e:
    print(e)  # Can't instantiate abstract class Vehicle with abstract method start

# Example: Abstract Method can be called via super() in Subclasses

class FourWheeler(Vehicle):
    def start(self):
        super().start()   # Does nothing but shows design extension, not an error
        print("Four-wheeler started.")

fw = FourWheeler()
fw.start()

# MiniProject: Payment Processing System using Abstraction

'''
MiniProject: Payment Processing System

Requirement:
- Design a payment system that supports multiple payment types (CreditCard, PayPal, UPI).
- System should process payments via a unified interface using abstraction.

'''

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

def process_payment(payment_method: PaymentMethod, amount):
    payment_method.pay(amount)

# Usage:
cards = [CreditCard(), PayPal(), UPI()]
for c in cards:
    process_payment(c, 500)

'''
Output:
Paid 500 using Credit Card.
Paid 500 using PayPal.
Paid 500 using UPI.

Explanation:
- All payment types inherit from PaymentMethod (abstract class) and implement the `pay` method.
- process_payment() uses abstraction to process any payment method.
'''

# ----------------------
# Interview Questions and Answers - Abstraction
# ----------------------

'''
Q1. What is abstraction in Python? How is it achieved?
A1. Abstraction is the process of hiding internal details and showing only the required functionalities. It is achieved using Abstract Base Classes (`ABC`) and `@abstractmethod` from the abc module. Abstract classes cannot be instantiated and require subclasses to implement abstract methods.

Q2. Can you instantiate an abstract class in Python? Justify.
A2. No, you cannot instantiate an abstract class directly. Attempting to do so raises a TypeError. This is to ensure that all abstract methods are implemented by a concrete subclass.

Example:
    class A(ABC):
        @abstractmethod
        def foo(self): pass
    # a = A() --> Raises TypeError

Q3. What happens if a subclass does not implement all abstract methods from the parent abstract class?
A3. The subclass also becomes abstract and cannot be instantiated until it implements all inherited abstract methods.

Example:
    class A(ABC):
        @abstractmethod
        def foo(self): pass
    class B(A):
        pass
    # b = B() --> Raises TypeError

Q4. Can abstract classes have concrete (regular) methods or properties?
A4. Yes, abstract classes can have both abstract and concrete methods/properties. Concrete methods can provide default/shared functionality.

Example:
    class Base(ABC):
        @abstractmethod
        def foo(self): pass
        def bar(self): print('Concrete bar')
    class Child(Base):
        def foo(self): print('foo impl')
    c = Child(); c.bar() # Concrete bar

Q5. How does abstraction help in large projects or frameworks?
A5. Abstraction:
    - Forces consistent interfaces across different implementations.
    - Enables code extensibility and plug-in architectures.
    - Maintains code security and reduces coupling.
    - Allows working with objects at a high interface (not specific implementations).

Example: In a payment gateway, you can process multiple payment types via an abstract "PaymentMethod" interface, without knowing concrete logic.

Q6. Can abstraction be implemented without the 'abc' module in Python? If yes, how safe is it?
A6. Yes, you can use "raise NotImplementedError()" in base class methods as a way to enforce interface, but this is only detected at runtime, not class creation. Using 'abc' with @abstractmethod is preferred for compile-time safety.

Example:
    class Base:
        def foo(self):
            raise NotImplementedError

Q7. Realtime: How would you design a plugin system for file export (PDF, CSV, XLSX) using abstraction?
A7. 
    - Create an abstract base class Exporter with abstract method export(data).
    - Implement concrete classes PDFExporter, CSVExporter, etc.
    - The plugin loader will only expect the 'export' method, not bothering with implementation.

    Example:
    class Exporter(ABC):
        @abstractmethod
        def export(self, data): pass
    class PDFExporter(Exporter):
        def export(self, data): print("Exporting PDF")

Q8. Can abstract methods have code in them? Give an example.
A8. Technically, you can put code in an abstract method, but it's not common. If you do, subclasses can call super().method().

Example:
    class A(ABC):
        @abstractmethod
        def foo(self):
            print("Shared logic")
    class B(A):
        def foo(self):
            super().foo()
            print("B specific")
    B().foo() # Shared logic\nB specific

Q9. What's difference between abstraction and encapsulation conceptually and in Python code?
A9.
    - Abstraction hides implementation complexity and only shows interface.
    - Encapsulation hides internal state (data) and restricts direct modification/access.
    - In Python, abstraction uses ABCs/abstract methods; encapsulation uses access modifiers (__var, _var).

Q10. What are the risks of not properly using abstraction in enterprise codebases?
A10.
    - Inconsistent interfaces.
    - Code duplication and tight coupling.
    - Difficult to extend or maintain systems.
    - Difficult to enforce contracts, leading to runtime errors.
    - Abstraction enables robust plugin/extension architecture, critical for scalable projects.

'''
