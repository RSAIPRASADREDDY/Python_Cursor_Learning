'''
Static Methods in Python
-------------------------
Definition:
------------
A Static Method is a method that belongs to a class but does NOT have access to the instance (`self`) or class (`cls`) variables/functions. 
It is defined using the `@staticmethod` decorator. Static methods behave just like plain functions, but belong to the class's namespace.

When to Use:
-------------
- When some functionality belongs to the class logically, but does not need class or instance data.
- Utility/helper methods, factory methods, or simple computations related to the class.

Methods We Can Use:
---------------------
- @staticmethod decorator to declare a static method
- Call it directly using ClassName.method() or instance.method()

Syntax:
--------
class MyClass:
    @staticmethod
    def my_static_method(args...):
        # code block

Examples from Beginner to Advanced
------------------------------------

'''

# Beginner Level Example: Static Method as a Utility

class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

print("Add 2 and 3:", MathUtils.add(2, 3))  # Output: 5

# Static methods can also be called from an instance
mu = MathUtils()
print("Add 5 and 7 using instance:", mu.add(5, 7))  # Output: 12

'''
Intermediate Example: Static Method vs Instance Method
-------------------------------------------------------
'''

class Demo:
    def instance_method(self):
        print("This is an instance method. self exists.")

    @staticmethod
    def static_method():
        print("This is a static method. No self or cls.")

demo_obj = Demo()
demo_obj.instance_method()   # This is an instance method. self exists.
Demo.static_method()         # This is a static method. No self or cls.

'''
Advanced Example: Static Methods for Data Validation
-----------------------------------------------------
'''

class Person:
    def __init__(self, name, age):
        if self.validate_age(age):
            self.name = name
            self.age = age
        else:
            raise ValueError("Invalid age! Must be between 0 and 150.")

    @staticmethod
    def validate_age(age):
        return 0 <= age <= 150

print("Is 35 a valid age?:", Person.validate_age(35))  # Output: True

# Valid person
p = Person("Alice", 26)
print("Person created:", p.name, p.age)

# Invalid person
try:
    q = Person("Bob", -10)
except ValueError as e:
    print("Error:", e)

'''
Advanced: Static Method as Factory without state
------------------------------------------------
'''

class Circle:
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius * self.radius

    @staticmethod
    def from_diameter(diameter):
        return Circle(diameter / 2)

c1 = Circle(10)
c2 = Circle.from_diameter(20)
print("c2.radius (from diameter):", c2.radius)  # Output: 10.0
print("c1 area:", c1.area())
print("c2 area:", c2.area())

'''
Mini Project: Student Management Utilities with Static Methods
--------------------------------------------------------------

Write a Student class to demonstrate:
- Validation with static methods
- Helper static methods
'''

class Student:
    def __init__(self, name, age, marks):
        if not Student.is_valid_name(name):
            raise ValueError("Invalid name!")
        if not Student.is_valid_age(age):
            raise ValueError("Invalid age!")
        if not Student.is_valid_marks(marks):
            raise ValueError("Invalid marks list or range!")

        self.name = name
        self.age = age
        self.marks = marks

    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 0

    @staticmethod
    def is_valid_age(age):
        return 5 <= age <= 100

    @staticmethod
    def is_valid_marks(marks):
        return isinstance(marks, list) and all(0 <= m <= 100 for m in marks)

    @staticmethod
    def calculate_grade(marks):
        avg = sum(marks) / len(marks)
        if avg >= 90:
            return 'A'
        elif avg >= 75:
            return 'B'
        elif avg >= 60:
            return 'C'
        else:
            return 'D'

    def get_grade(self):
        return Student.calculate_grade(self.marks)

# Create some students
try:
    stud1 = Student("Ram", 18, [92, 85, 88])
    stud2 = Student("Neha", 17, [76, 81, 79])
    stud3 = Student("Alex", 21, [54, 61, 59])
    students = [stud1, stud2, stud3]

    for s in students:
        print(f"{s.name}'s Grade: {s.get_grade()}")
except ValueError as ve:
    print("Student creation error:", ve)

'''
Interview Questions and Answers on Static Method
------------------------------------------------

Q1. What is a static method and when would you use it?
A1. A static method is a function inside a class that does not access instance (self) or class (cls) data. It is used for utility tasks related to the class, such as validation, data conversion, or factory logic, when no object or class state is needed.

Q2. Can static methods access or modify class or instance variables? Why or why not?
A2. No, static methods have no access to instance ('self') or class ('cls') variables because they are not passed any implicit parameters. They behave like a plain function scoped inside the class for organizational purposes.

Q3. How does a static method differ from a classmethod in Python?
A3. A static method receives no special first parameter. A classmethod receives the class itself as the first parameter ('cls'), so it can modify class state, create new instances, or access class variables. Static methods can't do this.

Example:
    class Demo:
        stat = 0
        @staticmethod
        def add(x,y): return x+y
        @classmethod
        def inc_stat(cls): cls.stat += 1

Q4. How do you call a static method? Does it require object instantiation?
A4. Call it using ClassName.method() or instance.method(). No instantiation is required since static methods don't need 'self' or 'cls'.

Example:
    MathUtils.add(1,2)         # preferred
    mu = MathUtils()
    mu.add(1,2)                # also works

Q5. Give a real-world scenario where staticmethods are necessary in Python OOP.
A5. Utility code for validation, conversion, or calculation that belongs to a class context but does not depend on any object/class state. E.g., validating date formats in a Date class, conversion helpers, or custom parsing inside a File utility class.

Q6. Can you override a static method in a child class? What happens?
A6. Yes, static methods can be overridden in subclasses. The child class's version will be invoked when called through the child class or its object.

Example:
    class Base:
        @staticmethod
        def foo(): print("Base foo")
    class Child(Base):
        @staticmethod
        def foo(): print("Child foo")
    Child.foo()  # Output: Child foo

Q7. Is there any performance or design impact in using @staticmethod versus using a function at the module level?
A7. Static methods are slightly slower than module-level functions (due to class lookup), but the organization and readability of grouping related logic under class scope trumps the negligible performance cost. Static methods promote cohesion in OOP design.

Q8. What happens if you try to access 'self' inside a static method, and why?
A8. It will result in a NameError, because no 'self' parameter is defined or passed inside a static method.

Q9. How are static methods used in conjunction with class inheritance?
A9. Static methods follow standard inheritance rules; a subclass inherits static methods from its parent, and can override them if desired.

Example:
    class Parent:
        @staticmethod
        def util(): print("Parent util")
    class Child(Parent):
        pass
    Child.util()           # Parent util

Q10. Can static methods be used as constructors?
A10. Not as primary constructors (__init__), but static methods can act as alternative object creators or 'pseudo-factories' that return customized instances, inside the class.

Example:
    class Person:
        def __init__(self, name):
            self.name = name
        @staticmethod
        def from_email(email):
            name = email.split('@')[0]
            return Person(name)
    p = Person.from_email("bob@gmail.com")
    print(p.name)
'''
