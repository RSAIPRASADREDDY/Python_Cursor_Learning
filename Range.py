"""
Python Range, max(), min(), sum(), sorted(), and all Other Built-in Value Functions
---------------------------------------------------------------------------------
Definition:
-----------
- `range()`: Generates a sequence of numbers, commonly used for looping a specific number of times.
- `max(iterable, *[, default=obj, key=func])`: Returns the largest item from an iterable or two or more arguments.
- `min(iterable, *[, default=obj, key=func])`: Returns the smallest item from an iterable or two or more arguments.
- `sum(iterable[, start])`: Sums items of an iterable, optionally starting from a specified value.
- `sorted(iterable, key=None, reverse=False)`: Returns a new sorted list from the items in iterable.
- (There are many other "value functions": all(), any(), abs(), pow(), etc. See below for core usage.)

Methods/Usages:
---------------
1. `range(stop)`                 # 0 up to stop-1
2. `range(start, stop[, step])`  # start up to stop-1, with step increments
3. `max(iterable)` / `max(arg1, arg2, ...)`
4. `min(iterable)` / `min(arg1, arg2, ...)`
5. `sum(iterable[, start])`
6. `sorted(iterable, key=None, reverse=False)`
7. `abs(x)`, `pow(x, y)`, `all(iterable)`, `any(iterable)`, `reversed(seq)`, etc.

Syntax:
-------
# range()
range(stop)
range(start, stop)
range(start, stop, step)

# max() and min()
max(iterable)
max(arg1, arg2, ...)
min(iterable)
min(arg1, arg2, ...)

# sum()
sum(iterable[, start])

# sorted
sorted(iterable, key=None, reverse=False)

# Example usages are below

"""

# -----------------------------------------------
# Beginner Level Examples
# -----------------------------------------------

# Example 1: Using range() in a simple for loop
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
print()

# Example 2: range() with start and stop
for n in range(2, 7):
    print(n, end=" ")  # Output: 2 3 4 5 6
print()

# Example 3: range() with step
evens = list(range(0, 10, 2))
print(evens)  # Output: [0, 2, 4, 6, 8]

# Example 4: Find maximum and minimum in a list using max() and min()
numbers = [9, 2, 15, -3, 42]
print("Max:", max(numbers))  # Output: Max: 42
print("Min:", min(numbers))  # Output: Min: -3

# Example 5: Sum all numbers using sum()
print("Sum:", sum(numbers))  # Output: Sum: 65

# Example 6: Simple sorting using sorted()
unordered = [3, 1, 4, 1, 5, 9, 2]
print(sorted(unordered))  # Output: [1, 1, 2, 3, 4, 5, 9]

# -----------------------------------------------
# Intermediate Level Examples
# -----------------------------------------------

# Example 7: range() to iterate in reverse
for i in range(10, 0, -2):
    print(i, end=" ")  # Output: 10 8 6 4 2
print()

# Example 8: max() and min() with multiple arguments
print(max(3, 6, 1, 8, 2))  # Output: 8
print(min(3, 6, 1, 8, 2))  # Output: 1

# Example 9: Getting maximum based on key (length of strings)
names = ["Alice", "Bob", "Christina", "Ed"]
longest = max(names, key=len)
print("Longest name:", longest)  # Output: Christina

# Example 10: sorted() with reverse order and custom key
words = ["data", "science", "python", "range"]
alpha = sorted(words, reverse=True)
print(alpha)  # Output: ['science', 'range', 'python', 'data']

by_length = sorted(words, key=len)
print(by_length)  # Output: ['data', 'range', 'python', 'science']

# Example 11: sum() with start value
expenses = [100, 250, 400]
total = sum(expenses, 50)  # start from 50
print("Total with initial:", total)  # Output: 800

# Example 12: abs(), pow(), all(), any()
negative = -12
print(abs(negative))  # Output: 12

print(pow(2, 5))  # Output: 32

bools = [True, False, True]
print(all(bools))  # Output: False
print(any(bools))  # Output: True

# -----------------------------------------------
# Advanced Level Examples
# -----------------------------------------------

# Example 13: Nested range() in list comprehensions
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Example 14: max()/min() among tuples with custom key
points = [(3, 4), (1, 9), (10, -2)]
highest_y = max(points, key=lambda x: x[1])
print("Point with max y:", highest_y)  # Output: (1, 9)

# Example 15: sorted() with objects and key function
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def __repr__(self):
        return f"{self.name} ({self.marks})"

students = [Student("Sai", 85), Student("Amy", 92), Student("Bob", 77)]
topper = max(students, key=lambda s: s.marks)
print("Topper:", topper)  # Output: Amy (92)

sorted_students = sorted(students, key=lambda s: s.marks)
print("Sorted by marks:", sorted_students)  # Output: [Bob (77), Sai (85), Amy (92)]

# Example 16: Using all() and any() with comprehensions
scores = [75, 80, 92, 61]
passed = all(mark >= 60 for mark in scores)
print("All passed?", passed)  # Output: True

some_high = any(mark > 90 for mark in scores)
print("Anyone above 90?", some_high)  # Output: True

# Example 17: Working with reversed() and range()
for i in reversed(range(5)):
    print(i, end=" ")  # Output: 4 3 2 1 0
print()

# Example 18: max() and min() with default for empty iterables
empty_list = []
print(max(empty_list, default="No Data"))  # Output: No Data
print(min(empty_list, default="No Data"))  # Output: No Data

# -----------------------------------------------
# Mini-Project: Score Analyzer
# -----------------------------------------------

def score_analyzer():
    """
    Mini-project: Collect student's scores, analyze statistics with built-in functions.
    """
    print("=== Score Analyzer ===")
    data = input("Enter scores (comma-separated): ")
    scores = [int(x.strip()) for x in data.split(",") if x.strip().isdigit()]
    
    if not scores:
        print("No valid scores entered!")
        return
    
    print(f"Scores entered: {scores}")
    print(f"Highest Score: {max(scores)}")
    print(f"Lowest  Score: {min(scores)}")
    print(f"Total      : {sum(scores)}")
    print(f"Average    : {sum(scores)/len(scores):.2f}")
    print(f"Scores sorted ascending : {sorted(scores)}")
    print(f"Scores sorted descending: {sorted(scores, reverse=True)}")
    print(f"All Passed (>=60)      : {all(s >= 60 for s in scores)}")
    print(f"Anyone with distinction (>=90): {any(s >= 90 for s in scores)}")
    
# Uncomment to test the mini-project:
# score_analyzer()

'''
------------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (Python Range, max, min, sum, sorted, etc.)
------------------------------------------------------------------

Q1: What does the 'range' function return in Python 3? How is it different from using a list?
A1: In Python 3, range() returns a range object, which is an immutable sequence type and does NOT actually generate a list in memory. It's memory-efficient for large ranges. You can convert it to a list if needed: list(range(1000000)).

Example:
r = range(5)
print(r)  # range(0, 5)
print(list(r))  # [0, 1, 2, 3, 4]

Q2: How do you find both the minimum and maximum value in a single pass of a list?
A2: Use the built-in min() and max() functions separately (each traverses the data), or use the 'reduce' technique/custom logic to get both in one iteration for very large data for efficiency.

Example:
nums = [13, 7, 9, 21]
print(min(nums), max(nums))   # 7 21

Q3: What does the 'key' argument in max(), min(), and sorted() do? Give an example.
A3: The key argument is a function that transforms each element before comparison/sorting. It allows custom sorting/max/min logic.

Example:
words = ["cat", "elephant", "dog"]
print(max(words, key=len))  # 'elephant'
print(sorted(words, key=len))  # ['cat', 'dog', 'elephant']

Q4: How would you sum only the positive numbers in a list using built-in functions?
A4: Use a generator with sum():

nums = [-3, 5, 9, -2]
print(sum(x for x in nums if x > 0))  # 14

Q5: Explain how 'sorted' differs from the list.sort() method.
A5: sorted(iterable) returns a new sorted list from any iterable and leaves the original unchanged. list.sort() sorts a list in-place and returns None.

lst = [4, 1, 2]
print(sorted(lst))    # [1, 2, 4]
print(lst)            # [4, 1, 2]

lst.sort()
print(lst)            # [1, 2, 4]

Q6: How do you handle max()/min() if the data may be empty? Why is this useful?
A6: Use the 'default' keyword argument which returns a fallback value if the iterable is empty. Prevents ValueError for empty collections.

print(max([], default=-1))   # -1

Q7: How can you use range() to count backwards or create a descending sequence?
A7: by specifying a negative step: range(start, stop, -1)

for i in range(10, 0, -2):
    print(i)  # 10 8 6 4 2

Q8: What is the output of all([]) and any([])? Why?
A8: all([]) returns True (vacuous truth: no element is False), any([]) returns False (no element is True).

Q9: How would you sort a list of dictionaries by a value in each dict?
A9: Use sorted() and a lambda key.

data = [{'name': 'A', 'age': 25}, {'name': 'B', 'age': 20}]
sorted(data, key=lambda d: d['age'])  # [{'name': 'B', 'age': 20}, {'name': 'A', 'age': 25}]

Q10: Give a real-world scenario where sum(), min(), max(), sorted() can all be leveraged together.
A10: Analyzing a sales data list to find total revenue (sum), the lowest/highest single sale (min/max), and ranking sales across months (sorted).

sales = [1200, 3400, 1800, 900]
print("Total:", sum(sales))
print("Best:", max(sales))
print("Worst:", min(sales))
print("Sorted:", sorted(sales))
------------------------------------------------------------------
'''
