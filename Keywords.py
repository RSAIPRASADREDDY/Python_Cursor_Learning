# --- Python Keywords: Concepts, Syntax, Examples, Mini-Project, and Interview Q&A ---

# Definition:
# In Python, **keywords** are reserved words that have special meaning to the interpreter.
# They cannot be used as identifiers (variable names, function names, etc.).
# Python keywords define the language's syntax and structure, such as `if`, `else`, `for`, `def`, `class`, `import`, etc.

# Syntax:
# Attempting to use a keyword as a variable or function name will result in a SyntaxError.
# All keywords are case-sensitive (e.g., 'if' is a keyword, 'If' is not).

# To view all keywords in your current version of Python, you can use:
import keyword
print("Python Keywords:", keyword.kwlist)

# --- Beginner Level Examples: Python Keywords ---

#exit()
# Example 1: Using 'if', 'else', 'elif'
num = 10
if num > 0:
    print("Positive number")   # Uses 'if'
elif num == 0:
    print("Zero")              # Uses 'elif'
else:
    print("Negative number")   # Uses 'else'

# Example 2: Using 'for' and 'in'
for i in range(3):  # 'for', 'in'
    print("Loop iteration:", i)

# Example 3: Using 'def' to define a function
def greet():
    print("Hello from a function!")  # 'def'
greet()

# Example 4: Using 'True', 'False', and 'None'
is_active = True     # keyword True
has_value = False    # keyword False
empty = None         # keyword None
print(is_active, has_value, empty)

# --- Intermediate Level Examples: Using Multiple Keywords ---

# Example 1: Using 'while', 'break', 'continue'
counter = 0
while counter < 5:       # 'while'
    if counter == 3:
        counter += 1
        continue         # Skips printing 3
    if counter == 4:
        break            # Stops the loop at 4
    print("Counter:", counter)
    counter += 1

# Example 2: Using 'import', 'as', 'from'
import math as m     # 'import', 'as'
from math import sqrt    # 'from', 'import'
print("Square root of 16:", m.sqrt(16))
print("Square root via 'from math import sqrt':", sqrt(25))

# Example 3: 'pass' as a placeholder
def future_feature():
    pass  # Does nothing for now ('pass' is a keyword)

# Example 4: 'not', 'and', 'or' logical operators
x, y = 5, 10
print("not x == y:", not x == y)       # not
print("x < 10 and y > 5:", x < 10 and y > 5)  # and
print("x > 10 or y > 5:", x > 10 or y > 5)    # or

# --- Advanced Level Examples: Python Keywords in Action ---

# Example 1: 'try', 'except', 'finally', 'raise'
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero! (caught by except)")
finally:
    print("This runs no matter what (finally)")

# Example 2: 'lambda', 'with', 'as', 'open'
square = lambda n: n * n   # Anonymous function using 'lambda'
print("Square of 7:", square(7))

with open(__file__, "r") as file:   # 'with', 'as', 'open'
    first_line = file.readline()
    print("First line of this file:", first_line.strip())

# Example 3: 'class', 'self', 'return'
class Animal:     # 'class'
    def __init__(self, name):
        self.name = name   # 'self'
    def speak(self):
        return f"{self.name} says hello!"   # 'return'
dog = Animal("Buddy")
print(dog.speak())

# Example 4: Using 'assert', 'global', 'nonlocal', 'del'
count = 1

def counter_function():
    global count
    count += 1
    print("Global count incremented:", count)
    def inner():
        nonlocal_var = 5
        def deep_inner():
            nonlocal nonlocal_var
            nonlocal_var += 5
            return nonlocal_var
        return deep_inner()
    result = inner()
    print("Nonlocal example result:", result)
    del result  # Deletes the variable

counter_function()
assert count == 2, "Count should be incremented to 2"  # 'assert'

# Example 5: 'is', 'in' for identity and membership checks
mylist = [1, 2, 3]
print("2 in mylist?", 2 in mylist)
another = mylist
print("mylist is another?", mylist is another)

# --- Mini Project: Python Keyword Explorer ---

"""
Simple Project: Python Keyword Usage Explorer

* Shows the list of keywords
* Lets a user input a keyword name, and tells if it is a valid Python keyword
* Asks for a code line, and detects if the line contains any keywords
"""

def keyword_explorer():
    import keyword
    print("\n=== Python Keyword Explorer ===")
    print("Python Keywords List:")
    print(keyword.kwlist)
    user_input = input("\nEnter a word to check if it's a Python keyword: ").strip()
    if keyword.iskeyword(user_input):
        print(f"'{user_input}' is a Python keyword!")
    else:
        print(f"'{user_input}' is NOT a Python keyword.")

    print("\nLet's check if a code line uses any keywords.")
    code_line = input("Enter a line of Python code: ")
    used_keywords = [word for word in code_line.split() if keyword.iskeyword(word)]
    if used_keywords:
        print("Keywords found in line:", used_keywords)
    else:
        print("No keywords found in your line.")

# Uncomment to run the mini project:
# if __name__ == "__main__":
#     keyword_explorer()

'''
    # --- Interview Q&A: Python Keywords ---

    Q: What are Python keywords?
    A: Keywords are reserved words that have special meaning in Python; they define the syntax and cannot be used as identifiers.

    Q: How do you find the list of Python keywords in your Python environment?
    A: By importing the 'keyword' module and using 'keyword.kwlist'.

    Q: Can you use keywords as variable or function names?
    A: No, using a keyword as an identifier will result in a SyntaxError.

    Q: Name five commonly used Python keywords.
    A: if, else, for, def, return

    Q: Are keywords case-sensitive in Python?
    A: Yes, all keywords are lowercase and case-sensitive.

    Q: What is the purpose of the 'with' keyword?
    A: 'with' is used for context management (e.g., for safely opening files), ensuring that resources are properly cleaned up.

    Q: What is the difference between 'is' and '=='?
    A: 'is' checks identity (same object in memory); '==' checks value (equality of content).

    Q: What happens if you try to use a keyword as a variable name?
    A: Python raises a SyntaxError.

    Q: Is 'None' a keyword? What does it represent?
    A: Yes, 'None' is a keyword representing the absence of a value or a null value.

    Q: Explain the use of 'global' and 'nonlocal' keywords.
    A: 'global' declares that a variable inside a function refers to a global variable. 'nonlocal' is used in nested functions to refer to variables in the enclosing (but non-global) scope.

'''
