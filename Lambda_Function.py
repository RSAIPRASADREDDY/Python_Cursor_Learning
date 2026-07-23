"""
Python Lambda Functions: Definition, Methods, Syntax, Examples (Beginner to Advanced), Mini-Project, and Interview Q&A

Definition:
-----------
A lambda function in Python is a small anonymous function, defined with the lambda keyword, that can have any number of arguments but only one expression. It is commonly used for short, throwaway functional tasks, especially as an argument to higher-order functions like map(), filter(), or sorted().

Methods/Use:
------------
- Used wherever function objects are required, especially for:
    - Functional programming constructs: map(), filter(), reduce(), sorted(), etc.
    - Callback functions
    - Event-handling, GUI programming
    - Inline, throwaway function definitions

Syntax:
-------
lambda arguments: expression
    # returns the value of the expression

# Example:
square = lambda x: x**2
print(square(5))        # 25

# (A regular function for comparison)
def square(x):
    return x**2
"""

# -----------------------------------------------
# Beginner Level Examples for Lambda Functions
# -----------------------------------------------

# Example 1: Single argument lambda (double a number)
double = lambda x: x * 2
print(double(4))  # 8

# Example 2: Lambda with zero arguments
greet = lambda : "Hello, Lambda!"
print(greet())  # Hello, Lambda!

# Example 3: Lambda with two arguments (sum of two numbers)
add = lambda a, b: a + b
print(add(3, 9))  # 12

# Example 4: Using lambda inside map() to square numbers
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, nums))
print(squares)  # [1, 4, 9, 16]

# -----------------------------------------------
# Intermediate Level Examples for Lambda Functions
# -----------------------------------------------

# Example 5: Using lambda in filter() to keep even numbers
evens = list(filter(lambda x: x % 2 == 0, range(10)))
print(evens)    # [0, 2, 4, 6, 8]

# Example 6: Sorting a list of tuples by second element using lambda as key
pairs = [(1, 3), (3, 2), (5, 1)]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # [(5, 1), (3, 2), (1, 3)]

# Example 7: Lambda that returns a function (higher-order function)
def make_multiplier(n):
    return lambda x: x * n

doubler = make_multiplier(2)
tripler = make_multiplier(3)
print(doubler(5))  # 10
print(tripler(4))  # 12

# Example 8: Conditional logic inside a lambda (ternary)
f = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f(7))  # Odd
print(f(10)) # Even

# -----------------------------------------------
# Advanced Level Examples for Lambda Functions
# -----------------------------------------------

# Example 9: Lambda with multiple arguments in map()
list1 = [1, 2, 3]
list2 = [4, 5, 6]
summed = list(map(lambda x, y: x + y, list1, list2))
print(summed)  # [5, 7, 9]

# Example 10: Nested lambda (lambda inside lambda)
nested = lambda x: lambda y: x + y
add5 = nested(5)
print(add5(10))    # 15

# Example 11: Using lambda in sorted() for string sorting by length
words = ['python', 'is', 'awesome']
sorted_words = sorted(words, key=lambda s: len(s))
print(sorted_words)  # ['is', 'python', 'awesome']

# Example 12: Lambda with map and dictionary items
d = {'a': 2, 'b': 5, 'c': -1}
vals_squared = list(map(lambda x: (x[0], x[1]**2), d.items()))
print(vals_squared)  # [('a', 4), ('b', 25), ('c', 1)]

# Example 13: Lambda as an inline callback
def compute(x, func):
    return func(x)

result = compute(7, lambda x: x**3)
print(result)   # 343

# Example 14: Using lambda and reduce to aggregate data
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x*y, nums)
print(product)  # 24

# -----------------------------------------------
# Mini-Project: Text Analytics Helper with Lambda
# -----------------------------------------------

def text_analytics():
    """
    Mini-Project: Count, filter, and transform words in a sentence using lambda functions.
    """
    print(">>> Mini-Project: Text Analytics Helper <<<")
    sentence = input("Enter a sentence: ")
    words = sentence.split()

    # 1. Count words starting with a vowel
    vowel_count = len(list(filter(lambda w: w[0].lower() in 'aeiou', words)))
    print("Number of words starting with a vowel:", vowel_count)
    
    # 2. List of word-lengths (using map+lambda)
    lengths = list(map(lambda w: (w, len(w)), words))
    print("Word lengths:", lengths)

    # 3. Convert all words to uppercase
    uppers = list(map(lambda w: w.upper(), words))
    print("Uppercase words:", uppers)

    # 4. Filter words longer than 4 letters
    long_words = list(filter(lambda w: len(w) > 4, words))
    print("Words longer than 4 letters:", long_words)

# Uncomment below to run the mini-project:
# text_analytics()

'''
------------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS - PYTHON LAMBDA FUNCTIONS
------------------------------------------------------------------

Q1: What are lambda functions and why are they called "anonymous"?
A1: Lambda functions are small, inline, one-expression functions defined using the lambda keyword, without necessarily being bound to a name. They are "anonymous" because they're typically used without assigning them a regular function name, especially as arguments to higher-order functions.

Example:
list(map(lambda x: x*2, [1, 2, 3]))   # [2, 4, 6]

Q2: Where are lambda functions most commonly used in Python?
A2: Lambda functions are widely used:
   - As arguments to map(), filter(), and reduce()
   - As sort or sorted key functions
   - In places requiring short, disposable (throwaway) transformations or decision logic
   - As callbacks/functions in functional programming patterns

Example:
names = ['Bob', 'Anna', 'Cecilia']
sorted_by_last = sorted(names, key=lambda s: s[-1])
print(sorted_by_last)  # ['Anna', 'Cecilia', 'Bob']

Q3: Can lambda functions have multiple expressions? Can they contain statements like if, for, or print?
A3: No. Lambdas can contain only a single expression (which can be a conditional/ternary), and cannot contain statements (such as for, while, print as a statement, assignment, etc.).

Wrong:
lambda x: for i in range(x): print(i)    # Not allowed

Right:
lambda x: x+1   # Only an expression

Q4: How would you use a lambda to reverse sort a list of tuples by the second element?
A4: Pass lambda to sorted as the key:

tuples = [(4, 2), (1, 9), (6, 5)]
sorted_t = sorted(tuples, key=lambda t: t[1], reverse=True)
print(sorted_t)   # [(1, 9), (6, 5), (4, 2)]

Q5: What's the difference between a lambda and a def function?
A5: Both produce functions, but:
   - def functions can have a name, multiple statements, and docstrings.
   - Lambdas are anonymous, concise, one-line expressions only.

def add(x, y):    # Can have statements, docstring
    """Adds two"""
    return x+y

lambda x, y: x+y   # Just the expression

Q6: What pitfalls are there with lambda functions, especially regarding closure and scope?
A6: Lambda captures variables by reference, not by value — can create bugs in loops.

Example:
funcs = [lambda x: x*i for i in range(3)]    # All use final i = 2!
print([f(2) for f in funcs])   # [4, 4, 4] (NOT [0, 2, 4])

To fix:
funcs = [lambda x, i=i: x*i for i in range(3)]
print([f(2) for f in funcs])   # [0, 2, 4]

Q7: How do you use a lambda function to apply different operations (add, subtract, multiply) based on string input?
A7:
ops = {
    "add": lambda x, y: x+y,
    "sub": lambda x, y: x-y,
    "mul": lambda x, y: x*y
}
print(ops["mul"](3, 4))   # 12

Q8: When would you avoid using lambda functions?
A8: Avoid for complex logic, situations needing reuse/documentation, or where readability is more important than brevity.

Q9: Can you return a lambda from another function? Give an example.
A9: Yes, lambdas are first-class objects.

def power(n):
    return lambda x: x**n

cube = power(3)
print(cube(2))   # 8

Q10: Real-world use case: How might you use lambda in data processing pipelines?
A10: Often used in data wrangling to transform, filter, sort rows, e.g.:

data = [{"name": "Sai", "marks": 90}, {"name": "Amy", "marks": 80}]
top = list(filter(lambda d: d["marks"] > 85, data))
print(top)   # [{'name': 'Sai', 'marks': 90}]

------------------------------------------------------------------
'''
