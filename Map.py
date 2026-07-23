"""
Python Map Function: Concept, Methods, Syntax, Examples, Mini-Project, and Interview Q&A

Definition:
-----------
The `map()` function in Python allows you to apply a function to every item of an iterable (like a list, tuple, etc.) and returns a map object (an iterator) of the results. It's particularly useful when you want to transform data in a collection without explicit loops.

Methods and Usage:
------------------
- `map(function, iterable, ...)` – Apply the given function to each item of one or more iterables.
- Can be used with built-in or user-defined functions, including lambda functions.
- The result must often be converted to a list/tuple: `list(map(...))` or `tuple(map(...))` for Python 3.x.

Syntax:
-------
# With single iterable
map(function, iterable)

# With multiple iterables
map(function, iterable1, iterable2, ...)

# Example: Convert all elements to integers
list(map(int, ['1', '2', '3']))   # [1, 2, 3]
"""

# -----------------------------------------------
# Beginner Level Examples for map()
# -----------------------------------------------

# Example 1: Using map() with a built-in function
nums = ['1', '2', '3', '4']
ints = list(map(int, nums))
print(ints)  # [1, 2, 3, 4]

# Example 2: Using map() with a user-defined function
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Example 3: Using map() with a lambda expression
doubles = list(map(lambda x: x * 2, numbers))
print(doubles)  # [2, 4, 6, 8, 10]

# -----------------------------------------------
# Intermediate Level Examples for map()
# -----------------------------------------------

# Example 4: map() with multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
summed = list(map(lambda x, y: x + y, a, b))
print(summed)   # [11, 22, 33]

# Example 5: map() for string processing (uppercase)
names = ['alice', 'bob', 'charlie']
upper_names = list(map(str.upper, names))
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# Example 6: map() with different types
floats = ['3.14', '2.78', '42']
as_float = list(map(float, floats))
print(as_float)  # [3.14, 2.78, 42.0]

# Example 7: map() with None function (identity map)
# (valid in Python 2; in Python 3 use a lambda)
items = [1, 2, 3]
identity = list(map(lambda x: x, items))
print(identity)  # [1, 2, 3]

# -----------------------------------------------
# Advanced Level Examples for map()
# -----------------------------------------------

# Example 8: Using map() with complex functions
def parse_and_process(s):
    # e.g., "X:9" => X*2: 9+5
    label, val = s.split(':')
    return (label*2, int(val) + 5)

data = ['A:5', 'B:7', 'Z:12']
results = list(map(parse_and_process, data))
print(results)  # [('AA', 10), ('BB', 12), ('ZZ', 17)]

# Example 9: map() with tuples and unpacking
coordinates = ['3,6', '2,8', '1,0']
coords = list(map(lambda s: tuple(map(int, s.split(','))), coordinates))
print(coords)  # [(3, 6), (2, 8), (1, 0)]

# Example 10: Combining map() with other functions
words = "hello world python map function".split()
lengths = list(map(len, words))
print(lengths)  # [5, 5, 6, 8]

# Example 11: map() for nested collections
nested = [[1, 2], [3, 4], [5, 6]]
flattened = list(map(lambda pair: pair[0] + pair[1], nested))
print(flattened)  # [3, 7, 11]

# Example 12: Chaining map() and filter()
nums = [1, 2, 3, 4, 5, 6]
even_squared = list(map(lambda x: x*x, filter(lambda n: n % 2 == 0, nums)))
print(even_squared)  # [4, 16, 36]

# -----------------------------------------------
# Mini-Project: Student Grade Calculator using map()
# -----------------------------------------------

def grade_report():
    """
    Simple mini-project that calculates student grades using map().
    """
    print("=== Student Grade Calculator ===")
    names = input("Enter student names (comma-separated): ").split(",")
    marks = input("Enter marks (comma-separated, in order): ").split(",")

    # Convert marks to int using map
    mark_list = list(map(int, map(str.strip, marks)))

    # Grade function
    def compute_grade(m):
        if m >= 90:
            return "A"
        elif m >= 80:
            return "B"
        elif m >= 70:
            return "C"
        elif m >= 60:
            return "D"
        else:
            return "F"

    grades = list(map(compute_grade, mark_list))

    # Report each student with grade
    print("\n--- Report ---")
    for name, m, g in zip(map(str.strip, names), mark_list, grades):
        print(f"{name}: {m} -> {g}")

# Uncomment to run the mini-project:
# grade_report()


'''
------------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (PYTHON MAP FUNCTION)
------------------------------------------------------------------

Q1: What is the `map()` function in Python, and how does it differ from a for loop?
A1: `map()` applies a function to each item in an iterable (or items from multiple iterables) and returns an iterator of the results. Unlike a for loop, which is explicit and can contain complex logic, `map()` is more concise and functional. `map()` is often faster and more expressive for simple transformations.

Example:
nums = [1, 2, 3]
doubles = list(map(lambda x: x*2, nums))
# vs
doubles = []
for x in nums:
    doubles.append(x*2)

Q2: Can you use `map()` with more than one iterable? Explain with an example.
A2: Yes. If the function takes multiple arguments, `map()` can pass one value from each iterable per invocation. Iteration stops at the shortest iterable.

Example:
a = [1, 2, 3]
b = [4, 5, 6]
sums = list(map(lambda x, y: x + y, a, b))  # [5, 7, 9]

Q3: What will be the output of the following code?
list(map(str.upper, ['a', 'b', 'c']))
A3: ['A', 'B', 'C']

Q4: What happens if the function passed to `map()` returns None? Why can this cause confusion?
A4: The map object will contain `None` for every element. This often happens if you pass a function that prints or modifies in-place rather than returns a value.

Example:
def print_item(x): print(x)
nums = [1, 2, 3]
result = list(map(print_item, nums))  
# Output: Prints 1, 2, 3 (but result is [None, None, None])

Q5: How can `map()` be used to process and clean up data loaded from a file?
A5: You can use `map()` to strip whitespace, convert types, or parse lines.

Example:
lines = [' alice\\n', 'bob\\n', '  charlie\\n']
clean = list(map(str.strip, lines))  # ['alice', 'bob', 'charlie']

Q6: How is `map()` different from `filter()` and `reduce()`?
A6:
- `map()`: Transforms every item.
- `filter()`: Selects items matching a predicate.
- `reduce()`: Aggregates items to a single result.

Example:
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))     # [1,4,9,16]
evens = list(filter(lambda x: x%2==0, nums)) # [2,4]

Q7: Can you write a one-line statement to extract the lengths of all words in a sentence using `map()`?
A7:
sentence = "hello world from python"
lengths = list(map(len, sentence.split()))  # [5, 5, 4, 6]

Q8: What are some caveats and pitfalls when using `map()` in Python 3?
A8: In Python 3, `map()` returns a lazy map object (iterator), not a list. To access all results at once, you must convert with `list()` or `tuple()`.

nums = [1,2,3]
result = map(lambda x: x+1, nums)
print(result)           # <map object at ...>
print(list(result))     # [2, 3, 4]

Q9: Give a real-world scenario where `map()` shines over a for-loop.
A9: When transforming large datasets (like parsing logs, converting data arrays, etc.), `map()` is concise, potentially faster, and often used with lambda/functions for clean, readable code.

Q10: How can you use `map()` to process more complex data, like extracting fields from CSV lines?
A10:
lines = ["Amy,21", "Bob,23", "Cat,19"]
records = list(map(lambda line: line.split(','), lines))
print(records)   # [['Amy', '21'], ['Bob', '23'], ['Cat', '19']]

------------------------------------------------------------------
'''
