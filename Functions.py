"""
Python Functions: Concepts, Methods, Syntax, Examples, Mini-Project, and Interview Q&A

Definition:
-----------
A function in Python is a block of organized, reusable code that is used to perform a single, related action. Functions help break our program into smaller and modular chunks, improving readability and reusability.

Methods and Usage:
------------------
- Use the `def` keyword to define a function.
- Call a function using its name and parentheses, possibly with arguments/parameters.
- Can have parameters, return values, default arguments, variable-length arguments, keyword arguments, docstrings, and more.
- Supports recursion, lambda (anonymous) functions, and higher-order functions.

Syntax:
-------
'''

def function_name(parameters):
 #   Optional docstring
    statements
    return value

# To call:
#function_name(arguments)
'''
"""

# -----------------------------------------------
# Beginner Level Function Examples
# -----------------------------------------------

# Example 1: Simple function to add two numbers
def add(a, b):
    return a + b

print(add(2, 3))  # 5

# Example 2: Function with no arguments
def say_hello():
    print("Hello!")

say_hello()  # Hello!

# Example 3: Function with a default argument
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Sai")   # Hello, Sai!
greet()        # Hello, Guest!

# Example 4: Returning multiple values (tuple)
def swap(x, y):
    return y, x

a, b = swap(10, 20)
print(a, b)  # 20 10

# -----------------------------------------------
# Intermediate Level Function Examples
# -----------------------------------------------

# Example 5: Variable-length arguments (*args)
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(2, 3, 4))  # 24

# Example 6: Keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Amy", age=23)

# Example 7: Function with a docstring and type hints
def square(n: int) -> int:
    """
    Returns the square of a number.
    """
    return n * n

print(square(5))  # 25

# Example 8: Recursive function (factorial)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120

# Example 9: Function as first-class object (passing as argument)
def apply_twice(func, val):
    return func(func(val))

def increment(x): return x + 1
print(apply_twice(increment, 3))  # 5

# Example 10: Lambda (anonymous) function
double = lambda x: x * 2
print(double(6))  # 12

# -----------------------------------------------
# Advanced Level Function Examples
# -----------------------------------------------

# Example 11: Nested (inner) functions
def outer(msg):
    def inner():
        print(f"Message: {msg}")
    inner()

outer("Hello from outer!")  # Message: Hello from outer!

# Example 12: Higher-order functions (returning a function)
def power_func(n):
    def power(x):
        return x ** n
    return power

cube = power_func(3)
print(cube(2))  # 8

# Example 13: Decorators
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@simple_decorator
def greet_user(name):
    print(f"Hi, {name}!")

greet_user("Sai")
# Before call
# Hi, Sai!
# After call

# Example 14: Using functions with map/filter/reduce
from functools import reduce

nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
sum_all = reduce(lambda x, y: x + y, nums)

print(doubled)  # [2, 4, 6, 8]
print(evens)    # [2, 4]
print(sum_all)  # 10

# Example 15: Function annotations & introspection
def greet_formal(name: str, age: int) -> str:
    """Returns a formal greeting."""
    return f"Hello, {name}. You are {age} years old."

print(greet_formal.__annotations__)  # {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
print(greet_formal("Amy", 30))       # Hello, Amy. You are 30 years old.

# -----------------------------------------------
# Mini-Project: Basic Calculator using Functions
# -----------------------------------------------

def calculator():
    """
    A simple calculator using Python functions.
    """
    print("=== Simple Calculator ===")
    print("Available operations: add, subtract, multiply, divide")
    
    def add(x, y): return x + y
    def subtract(x, y): return x - y
    def multiply(x, y): return x * y
    def divide(x, y):
        if y == 0:
            return "Cannot divide by zero!"
        return x / y

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    op = input("Enter operation: ").strip().lower()
    if op not in operations:
        print("Unsupported operation.")
        return
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number(s).")
        return
    
    result = operations[op](x, y)
    print(f"Result: {result}")

# Uncomment to run the calculator mini-project:
# calculator()


'''
------------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (PYTHON FUNCTIONS)
------------------------------------------------------------------

Q1: How does Python determine default argument values in functions? Give an example of a pitfall.
A1: Default argument values are evaluated at function definition time, not at function call time. This can lead to bugs when using mutable defaults.

Example:
def append_num(num, nums=[]):
    nums.append(num)
    return nums

print(append_num(1))  # [1]
print(append_num(2))  # [1, 2]   (Unexpected: nums persists!)

To avoid:
def append_num(num, nums=None):
    if nums is None:
        nums = []
    nums.append(num)
    return nums

Q2: What's the difference between parameters and arguments?
A2: Parameters are variables listed in a function definition. Arguments are the actual values passed to a function when calling it.

def f(x):    # x = parameter
    pass
f(3)        # 3 = argument

Q3: Explain the use of *args and **kwargs in functions. When would you use each?
A3: *args packs extra positional arguments into a tuple; **kwargs packs extra keyword arguments into a dict. Use *args for variable-length argument lists and **kwargs when you want to accept (and forward) arbitrary keyword arguments.

def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo(1, 2, a=3, b=4)
# (1, 2)
# {'a': 3, 'b': 4}

Q4: Can a function return multiple values? How does this work?
A4: Yes, a function can return multiple values by separating them with commas. Python actually returns a tuple of the results.

def minmax(iterable):
    return min(iterable), max(iterable)

low, high = minmax([3, 1, 7])
print(low, high)  # 1 7

Q5: What is recursion? Provide an example and its drawbacks.
A5: Recursion is when a function calls itself to solve a problem. Useful for tasks that can be broken into similar subproblems (like tree traversal). Drawbacks: can hit recursion limits and be less efficient than iterative solutions.

Example:
def countdown(n):
    if n == 0:
        print("Go!")
    else:
        print(n)
        countdown(n-1)

countdown(3)  # 3 2 1 Go!

Q6: How is a lambda function different from a def function? When would you use one over the other?
A6: Lambdas are anonymous one-line expressions with no statements or docstrings; defs can be multi-line and named. Use lambdas for short, throwaway functions often passed as arguments (e.g., key functions), and defs for anything more complex or that requires clarity.

Q7: What is function scope, and how does the LEGB rule apply in Python?
A7: Scope defines where variables can be accessed. LEGB stands for Local, Enclosing, Global, Built-in. Python resolves names by searching these scopes in order.

Q8: What are decorators in Python? How do they work? Give a simple custom decorator example.
A8: Decorators are functions that modify the behavior of other functions. They take a function as input and return a new function.

Example:
def upper_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result).upper()
    return wrapper

@upper_decorator
def greet():
    return "hello"

print(greet())  # HELLO

Q9: Can functions be assigned to variables, stored in collections, or nested? Give an example.
A9: Yes, functions are first-class citizens in Python and support these usages.

Example:
def f(x): return x*2
funcs = [f, lambda x: x**2]
print([fn(5) for fn in funcs])  # [10, 25]

Q10: How can you document a function? What is the __doc__ attribute?
A10: Use a docstring as the first statement in a function. It's accessible via the function's __doc__ attribute.

def foo():
    """This function does nothing."""
    pass

print(foo.__doc__)  # This function does nothing.

------------------------------------------------------------------
'''
