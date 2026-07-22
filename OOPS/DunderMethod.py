'''
Dunder Methods in Python (Magic Methods)
----------------------------------------
Definition:
-----------
Dunder (double underscore) methods, also called magic methods, 
are special methods with names starting and ending with double underscores (e.g., __init__, __str__). 
Python uses them to provide built-in behavior to objects, such as initialization, representation, arithmetic operations, and more.

Why Use Dunder Methods?
-----------------------
- To customize the behavior of objects (object creation, printing, arithmetic, comparisons, etc.)
- To make classes interact naturally with Python's built-in functions and syntax (like len(), print(), +, ==, etc.).
- To implement operator overloading.

Commonly Used Dunder Methods:
-----------------------------
__init__(self, ...):          Object initialization (constructor)
__str__(self):                Informal string representation (for print())
__repr__(self):               Official string representation
__len__(self):                Length using len(obj)
__add__(self, other):         Overload the + operator
__eq__(self, other):          Overload the == operator
__lt__(self, other):          Overload the < operator
__getitem__(self, key):       obj[key] support
__setitem__(self, key, val):  obj[key] = val support
__call__(self, ...):          Allows instances to be called as functions

Syntax Example:
---------------
class ClassName:
    def __init__(self, ...):
        # Initialization logic
    def __str__(self):
        # Return printable string

'''

# Beginner Level Example - __init__ and __str__ 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"

p = Person("Alice", 25)
print(p)   # Output: Alice (25)

'''
Explanation:
------------
- __init__ initializes object attributes.
- __str__ provides a user-friendly representation for print().
'''

# Intermediate Example - Operator Overloading with __add__ and __eq__

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(5, 6)
v3 = v1 + v2
print(v3)             # Output: Vector(7, 10)
print(v1 == Vector(2, 4))  # Output: True

'''
Explanation:
-------------
- __add__ allows v1 + v2.
- __eq__ allows comparison (==) between Vector objects.
'''

# Advanced Example - Creating Custom Container using __getitem__, __setitem__, __len__, __repr__

class CustomList:
    def __init__(self, items):
        self._items = items
        
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
        
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return f"CustomList({self._items})"

clist = CustomList([1, 2, 3])
print(clist[1])       # Output: 2
clist[1] = 100
print(clist)          # Output: CustomList([1, 100, 3])
print(len(clist))     # Output: 3

'''
Explanation:
-------------
- __getitem__ allows indexing and slicing.
- __setitem__ allows assignment via index.
- __len__ allows using len().
- __repr__ provides an official string representation, e.g., in the interpreter.
'''

# Example - __call__: Making Objects Callable

class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

a = Adder(10)
print(a(5))   # Output: 15

'''
Explanation:
------------
- __call__ allows object a to be called like a function.
'''

# Advanced Example - Custom Sorting with __lt__

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __lt__(self, other):
        return self.salary < other.salary
    
    def __repr__(self):
        return f"{self.name}:{self.salary}"

e1 = Employee("Amit", 50000)
e2 = Employee("Bina", 60000)
e3 = Employee("Chad", 40000)
emp_list = [e1, e2, e3]
emp_list.sort()
print(emp_list)  # Output: [Chad:40000, Amit:50000, Bina:60000]

'''
Explanation:
-------------
- __lt__ enables comparison for sorting custom objects.
'''

# Mini Project: MathSet Class with Dunder Methods

class MathSet:
    def __init__(self, items):
        self.items = set(items)
    
    def __str__(self):
        return "{" + ", ".join(str(i) for i in sorted(self.items)) + "}"
    
    def __add__(self, other):
        return MathSet(self.items.union(other.items))
    
    def __sub__(self, other):
        return MathSet(self.items.difference(other.items))
    
    def __contains__(self, item):
        return item in self.items
    
    def __len__(self):
        return len(self.items)
    
    def __eq__(self, other):
        return self.items == other.items
    
    def __getitem__(self, idx):
        try:
            return list(sorted(self.items))[idx]
        except IndexError:
            raise IndexError("Index out of range")
    
# Usage of MathSet mini-project
s1 = MathSet([1, 2, 3, 4])
s2 = MathSet([3, 4, 5])
print("s1:", s1)                           # s1: {1, 2, 3, 4}
print("s2:", s2)                           # s2: {3, 4, 5}
print("s1 + s2:", s1 + s2)                 # Union: {1, 2, 3, 4, 5}
print("s1 - s2:", s1 - s2)                 # Difference: {1, 2}
print("Length of s1:", len(s1))            # 4
print("Is 3 in s1?", 3 in s1)              # True
print("First element of s1:", s1[0])       # 1

'''
Mini Project Explanation:
-------------------------
- Demonstrates dunder methods: __str__, __add__, __sub__, __contains__, __len__, __eq__, __getitem__.
- s1 + s2 returns a set union.
- s1 - s2 returns set difference.
- len(s1) returns number of elements.
- 3 in s1 checks membership.
- s1[0] gets the smallest element (sorted order).
'''

'''
Interview Questions and Answers: Dunder(Magic) Methods
------------------------------------------------------

Q1. What are dunder methods? Why are they called so?
A1. Dunder methods (double underscore methods) are special methods in Python with names starting and ending with '__'. They're called so because of "double underscores," e.g., __init__, __add__. They let objects integrate with Python’s language features, like printing, arithmetic, comparisons, etc.

Q2. How does __str__ differ from __repr__? Give a usage example.
A2. __str__ is for a user-friendly print output; __repr__ is for an official string (should be valid code if possible) for debugging and development. If __str__ is not defined, print() uses __repr__ as fallback.

Example:
    class X:
        def __repr__(self): return "X()"
        def __str__(self): return "Instance of X"
    x = X()
    print(x)        # Output: Instance of X
    print([x])      # Output: [X()]

Q3. What happens if you define __add__, but not __iadd__?
A3. __add__ handles x + y; __iadd__ handles x += y. If __iadd__ is missing, x += y falls back to x = x + y (using __add__). However, __iadd__ can be used for in-place addition.

Q4. Can you make your class callable like a function? How?
A4. Yes, by implementing __call__, you can call instances as functions.

Example:
    class Foo:
        def __call__(self, val): print("Called with", val)
    f = Foo()
    f(123)    # Output: Called with 123

Q5. How would you implement custom logic for "in" keyword (membership test) on your class?
A5. Define the __contains__ method.

Example:
    class Bag:
        def __init__(self, l): self.l = l
        def __contains__(self, item): return item in self.l
    b = Bag([10, 20, 30])
    print(20 in b)     # Output: True

Q6. Explain how operator overloading allows custom objects to behave like numbers.
A6. By implementing dunder methods like __add__, __sub__, __mul__, __truediv__, etc., you can use custom objects with +, -, *, / just like built-in numbers; this lets you extend natural syntax to, e.g., vectors, fractions, matrices.

Q7. Give an example where not implementing a suitable dunder method causes unexpected behavior in a custom container class.
A7. If you forget to implement __len__, calling len(obj) raises TypeError. Similarly, not implementing __getitem__ means obj[i] will not work, making the object less compatible with Python conventions.

Q8. How can you influence sorting of custom objects?
A8. By defining __lt__ (less than), __gt__, __eq__, etc., you enable list.sort() and sorted() to compare objects as per your business logic.

Q9. Can __new__ and __init__ be used together? Explain difference.
A9. Yes. __new__ is a static method for creating a new instance (used rarely, e.g., for immutable types or metaclasses); __init__ initializes the instance after it's created. Both can be used, e.g., when subclassing immutable types like tuple or str.

Q10. Write a class that supports: printing, indexing, and "in" keyword. (Implement required dunder methods)
A10. 
    class MySeq:
        def __init__(self, seq): self.seq = seq
        def __str__(self): return str(self.seq)
        def __getitem__(self, i): return self.seq[i]
        def __contains__(self, x): return x in self.seq
    ms = MySeq([1,2,3])
    print(ms)       # [1, 2, 3]
    print(ms[1])    # 2
    print(3 in ms)  # True

'''
