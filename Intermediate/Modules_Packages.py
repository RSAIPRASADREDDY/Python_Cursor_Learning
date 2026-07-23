"""
Modules & Packages in Python

Definition:
-----------
- Module: A Python file (.py) containing definitions, statements, functions, classes, etc. that can be reused in other code.
- Package: A directory with an __init__.py file (can be empty or have code), that can contain multiple modules or subpackages. 
            Packages allow hierarchical structuring of modules.

Benefits:
---------
- Organize code into reusable, manageable files.
- Avoid name conflicts with namespaces.
- Distribute, share, and maintain code easily.

Key Methods:
------------
- import modulename
- from modulename import something
- import packagename.modulename
- as aliasing (import xyz as something)
- __init__.py (for packages)
- sys.path (search path)

Syntax:
-------
# Importing a whole module
import math

# Importing specific attributes
from math import sqrt, pi

# Importing a module from a package
import mypackage.mymodule

# Aliasing a module
import numpy as np

# Creating a package (directory with __init__.py)
"""

# -----------------------------------------------
# Beginner Level Examples
# -----------------------------------------------

# Example 1: Creating and Importing a Module
# Suppose you have a file named mymodule.py with a function:
# def greet(name): return f"Hello, {name}!"

# In another file, you can do:
# import mymodule
# print(mymodule.greet('Alice'))  # Output: Hello, Alice!

# Example 2: Importing Specific Function
# from mymodule import greet
# print(greet("Bob"))  # Output: Hello, Bob!

# Example 3: Aliasing
import math as m

# You can use the built-in dir() function to list all attributes (including methods) in the math module.
# print("Number of methods in math module:", len(dir(m)))
# print("First 10 math module attributes:", dir(m)[:10])
# How can you understand what each method or attribute in a module does?
# There are several tools and techniques in Python for introspection and help:
#
# 1. Use the built-in help() function:
print("Help on 'math.sqrt':")
help(m.sqrt)  # Prints the docstring for math.sqrt (what it does, parameters, etc.)


# # 2. Use the __doc__ attribute of functions and modules:
# print("Docstring for math.pow:", m.pow.__doc__)

# # 3. Use dir() to list all attributes in a module:
# print("All math module attributes:", dir(m))

# 4. Use help() on the whole module:
# help(m)  # Uncomment to see documentation for the entire math module

# 5. For IPython/Jupyter, use ? and ?? after the method or module name:
# m.sqrt?     # Show docstring
# m.sqrt??    # Show docstring and source if available

# 6. For modules you've written, always write good docstrings so users can find help!

# Example:
# for attr in dir(m)[:5]:  # Show help for first 5 math attributes
#     print(f"\nHelp for math.{attr}:")
#     help(getattr(m, attr))



# print(m.sqrt(16))  # Output: 4.0

# -----------------------------------------------
# Intermediate Level Examples
# -----------------------------------------------

# Example 4: Importing a Package and Module
# Suppose folder structure:
# mypackage/
#    __init__.py
#    utils.py (def add(a,b): return a+b)

# In your script:
# import mypackage.utils
# print(mypackage.utils.add(2, 3))  # Output: 5

# Example 5: Selective Import with Alias
# from mypackage.utils import add as add_func
# print(add_func(10, 5))  # Output: 15

# Example 6: Using Built-in Modules
import random
print(dir(random))
nums = [random.randint(1, 10) for _ in range(5)]
# choice = [random.choice(2) for _ in range(5)]
# choices = [random.choices(1, 10) for _ in range(5)]
# random = [random.random(1, 10) for _ in range(5)]
# gauss = [random.gauss(1, 10) for _ in range(5)]
# print("Random numbers:", nums)
# print("Choice:", choice)
# print("Choices:", choices)
# print("Random:", random)
# print("Gauss:", gauss)




# -----------------------------------------------
# Advanced Level Examples
# -----------------------------------------------

# Example 7: Importing All from a Module (not recommended in practice)
# from math import *
# print(sin(pi / 2))  # Output: 1.0

# Example 8: Inspecting Module Attributes
import os
print("OS module attributes (first 5):", dir(os)[:5])

# Example 9: Dynamic Import Using __import__
mod = __import__('math')
print("Dynamic sqrt:", mod.sqrt(81))  # Output: 9.0

# Example 10: Understanding sys.path (module search path)
import sys
print("Python search path:", sys.path)

# Example 11: Importing Subpackages
# Suppose: package/
#   __init__.py
#   subpkg/
#      __init__.py
#      submodule.py (def info(): print("inside subpackage"))
# from package.subpkg import submodule
# submodule.info()  # Output: inside subpackage

# -----------------------------------------------
# Mini-Project: Directory Package Example (Calculator)
# -----------------------------------------------

# Suppose you have this folder structure:
# calculator/
#   __init__.py
#   add.py        (def add(a, b): return a + b)
#   subtract.py   (def subtract(a, b): return a - b)
#   multiply.py   (def multiply(a, b): return a * b)
#   divide.py     (def divide(a, b): return a / b)
#
# Usage in your main script:

# from calculator import add, subtract, multiply, divide

# print("2 + 3 =", add.add(2, 3))
# print("10 - 4 =", subtract.subtract(10, 4))
# print("6 * 7 =", multiply.multiply(6, 7))
# print("20 / 4 =", divide.divide(20, 4))

# Output:
# 2 + 3 = 5
# 10 - 4 = 6
# 6 * 7 = 42
# 20 / 4 = 5.0

'''
-----------------------------------------------
Interview Q&A: Python Modules & Packages
-----------------------------------------------

Q1: What is a module and how is it different from a package?
A1: A module is a single Python file (with .py extension) containing Python definitions and code. A package is a directory of Python modules plus (optionally) subpackages, defined by the presence of an __init__.py file.

Q2: Explain 'from module import *'. Is it good practice?
A2: It imports all public names from a module into the current namespace. Not recommended generally, as it may lead to namespace confusion and overwriting of variable names.

Example:
from math import *
print(sqrt(16)) # 4.0

Q3: How does Python know where to look for modules?
A3: The interpreter searches for modules in the directories specified in sys.path — it includes the script directory, installed packages, and PYTHONPATH.

Example:
import sys
print(sys.path)

Q4: What happens if a module is re-imported? Is it executed again?
A4: No. Once a module is imported, it is cached in sys.modules and not re-executed on subsequent imports within the same session.

Q5: Can you import a module dynamically at runtime?
A5: Yes, using __import__(module_name) or importlib.import_module(module_name).

Example:
mod = __import__('math')
print(mod.factorial(5))

Q6: How do you structure a package to have subpackages? Give an example.
A6:
Structure:
mypkg/
    __init__.py
    core.py
    helpers/
        __init__.py
        tool.py

Usage:
from mypkg.helpers import tool

Q7: What is the role of __init__.py file?
A7: It marks a directory as a Python package; without it, Python does not recognize the directory as containing modules. It also runs initialization code for the package (if any).

Q8: How can you expose only certain functions for "from xyz import *"?
A8: Define a list named __all__ in the module. Only the names inside __all__ will be imported.

Example:
__all__ = ['foo', 'bar']

Q9: What is relative import and when is it useful?
A9: Relative imports use dot notation to import from sibling or parent modules/packages (e.g., from .helpers import foo). Useful inside packages to organize large codebases.

Q10: Write a small package example that demonstrates two modules, with one importing from the other using a relative import.

A10:
Structure:
shapes/
    __init__.py
    circle.py   (def area(r): return 3.14 * r * r)
    square.py   (from .circle import area as circle_area)

# In square.py:
from .circle import area as circle_area

# In __main__ script:
from shapes import square
print(square.circle_area(2))

-- End of Q&A --
'''
