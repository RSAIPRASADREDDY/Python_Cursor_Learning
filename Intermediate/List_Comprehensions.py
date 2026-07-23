"""
List Comprehensions in Python
-----------------------------
Definition:
-----------
A list comprehension provides a concise (one-line) way to create lists in Python 
by applying an expression to each element in an iterable (like a list, tuple, string, etc.), 
possibly filtering elements with conditions.

Benefits:
---------
- Less code and more readable than traditional loops.
- Returns a new list.
- Can be combined with conditions and even nested.

Syntax:
-------
# General syntax:
[expression for item in iterable]

# With condition:
[expression for item in iterable if condition]

# Nested comprehensions (for matrix, etc):
[expression for inner_item in outer for outer in outer_iterable]

Common Methods / Uses:
----------------------
- Generating a list from another iterable (like mapping)
- Filtering elements (conditional selection)
- Transforming elements (applying functions)
- Flattening nested lists
"""

# -----------------------------------------------
# Beginner Level Examples
# -----------------------------------------------

# Example 1: Square numbers in a list
from numpy.strings import lower


numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
sq=[n+1 for n in numbers]
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]
print("Squares:", sq)


# Example 2: Convert strings to uppercase
words = ["python", "List", "comprehension"]
uppercase_words = [word.upper() for word in words]
lowercase_words = [word.lower() for word in words]
print("Uppercase:", uppercase_words)
print("Lowercase:", lowercase_words)
# Example 2a: Capitalize each word (first letter uppercase, rest lower)
capitalized_words = [word.capitalize() for word in words]
print("Capitalized:", capitalized_words)

# Example 2b: Swap the case of each word (upper -> lower, lower -> upper)
swapped_words = [word.swapcase() for word in words]
print("Swapcase:", swapped_words)

# Example 2c: Title case (first letter of each word, for phrases)
phrases = ["hello world", "python programming"]
titlecase_phrases = [phrase.title() for phrase in phrases]
print("Title case:", titlecase_phrases)

# Example 2d: Reverse all words
reversed_words = [word[::-1] for word in words]
print("Reversed words:", reversed_words)

# Example 2e: Pad words to length 12 with underscores
padded_words = [word.ljust(12, "_") for word in words]
print("Padded words:", padded_words)


# Example 3: Create a list of characters from a string
chars = [char for char in "hello"]
print("Characters:", chars)

# -----------------------------------------------
# Intermediate Level Examples
# -----------------------------------------------

# Example 4: Filter even numbers
evens = [n for n in range(10) if n % 2 == 0]
print("Even numbers 0-9:", evens)

# Example 5: Get lengths of words, but only if > 4 letters
words = ["apple", "hi", "banana", "cat", "watermelon"]
lengths = [len(word) for word in words if len(word) > 4]
print("Lengths (>4 letters):", lengths)

# Example 6: Apply a function (stripping whitespace)
lines = ["  line 1  ", "\tline 2", "line 3\n"]
clean_lines = [line.strip() for line in lines]
print("Stripped lines:", clean_lines)

# Example 7: Nested Loops - Create pairs (Cartesian product)
colors = ['red', 'blue']
objects = ['car', 'bike']
pairs = [(color, obj) for color in colors for obj in objects]
print("Pairs:", pairs)


# -----------------------------------------------
# Advanced Level Examples
# -----------------------------------------------

# Example 8: Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print("Flattened matrix:", flat)

# Example 9: Conditional expression in comprehension
numbers = range(10)
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("Even/Odd labels:", labels)

# Example 10: List comprehension with enumerate (index, value)
words = ["zero", "one", "two"]
indexed = [f"{i}:{word}" for i, word in enumerate(words)]
print("Indexed words:", indexed)


# Example 11: Dictionary comprehension from list comprehension
names = ["alice", "bob", "carol"]
scores = [85, 90, 95]
name_score = list(zip(names, scores))
print("Name to score:", name_score)
score_dict = {name: score for name, score in zip(names, scores)}
print("Name to score:", score_dict)

# Example 12: Set comprehension to remove duplicates and capitalize
names_with_dupes = ["ALICE", "Bob", "bob", "carol", "ALICE"]
unique_cap_names = {name.capitalize() for name in names_with_dupes}
print("Unique (case-insensitive) Names:", unique_cap_names)

# -----------------------------------------------
# Mini Project: Word Frequency Counter Using List Comprehensions
# -----------------------------------------------

# Goal: Given a text, count frequency of each unique word (ignoring case and punctuation) using list and dict comprehensions

text = "Python is fun. Python is powerful! Programming in python is productive and fun."
# Step 1: Normalize text to lowercase, remove punctuation (keep only words)
import string
words = [word.strip(string.punctuation).lower() for word in text.split()]
# Step 2: Get unique words
unique_words = set(words)
# Step 3: Create dictionary: word -> frequency
freq = {word: words.count(word) for word in unique_words}
print("---Word Frequencies---")
print(freq)

'''
Interview Questions and Answers - List Comprehensions in Python
--------------------------------------------------------------

Q1: What is a list comprehension? Show equivalent 'for loop' code for [x*x for x in range(5)].

A1:
A list comprehension is a concise way to construct lists from iterables. It can include transformations and conditions.
Equivalent code:
result = []
for x in range(5):
    result.append(x*x)

Q2: How would you filter all odd numbers from a list using list comprehension?

A2:
odds = [n for n in mylist if n % 2 != 0]

Q3: Can you explain how to flatten a nested list using a list comprehension? Give an example.

A3:
Yes. For a 2D list like [[1,2],[3,4]], you can use:
flat = [item for sublist in matrix for item in sublist]
Example:
matrix = [[1, 2], [3, 4]]
flat = [item for sublist in matrix for item in sublist]  # [1,2,3,4]

Q4: Is it possible to include an if-else condition inside a list comprehension? Illustrate.

A4:
Yes, with this syntax:
result = ["even" if n%2==0 else "odd" for n in range(4)]
Output: ['even', 'odd', 'even', 'odd']

Q5: Write a comprehension to produce all 2-letter lowercase combinations from "abc" and "de".

A5:
res = [a+b for a in "abc" for b in "de"]
Output: ['ad', 'ae', 'bd', 'be', 'cd', 'ce']

Q6: What are potential pitfalls or performance considerations with list comprehensions?

A6:
- Using them with very large data can consume much memory.
- Complex logic (like deeply nested comprehensions) hurts readability.
- If you don't need a list, consider generator expressions to save memory.

Q7: How would you use a comprehension to remove duplicates and normalize case in a list of strings?

A7:
s = ["ALICE", "Bob", "bob", "alice"]
unique = {word.lower() for word in s}
# Or for a deduped, normalized list:
unique_list = list({word.lower() for word in s})

Q8: How can you create a dictionary with keys as numbers 1..n and values as their squares, using comprehension?

A8:
n = 5
d = {x: x**2 for x in range(1, n+1)}
Result: {1:1, 2:4, 3:9, 4:16, 5:25}

Q9: Explain the difference between a list comprehension and a generator expression.

A9:
A list comprehension [expr for x in iterable] creates the entire list in memory immediately.
A generator expression (expr for x in iterable) creates a generator object that computes each value lazily, when iterated, using less memory for large data.

Q10: How would you use a list comprehension to select file names ending with ".py" from a list of strings?

A10:
files = ["test.py", "hello.txt", "main.py"]
py_files = [f for f in files if f.endswith(".py")]
Result: ['test.py', 'main.py']

'''
