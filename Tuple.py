"""
Python Tuple: Concepts, Methods, Examples, Mini-project, and Interview Q&A

Definition:
-----------
A tuple in Python is an immutable, ordered collection of elements. Elements can be of different data types and are defined by parentheses `()`. Once a tuple is created, its elements cannot be changed, added, or removed (immutability).

Tuple Methods and Concepts:
--------------------------
- Creation & Initialization
- Indexing & Slicing
- Concatenation (+), Repetition (*)
- Unpacking
- Immutability
- Built-in Functions: len(), tuple(), sum(), min(), max(), sorted() (returns a list), count(), index()
- Iterating Tuples
- Membership (`in`)
- Nested Tuples

Syntax:
-------
# Creating tuples
tup = (1, 2, 3)
empty = ()
single = (5,)   # note the trailing comma
tup2 = tuple([4, 5, 6])  # from list

# Indexing & Slicing
item = tup[0]
subset = tup[1:3]

# Concatenation & Repetition
tup3 = tup + tup2
rep = tup * 2

# Unpacking
a, b, c = tup   # a=1, b=2, c=3

-----------------------------------------------
Beginner Level Examples
-----------------------------------------------
"""

# Creation
tup1 = (10, 20, 30,-10)
print(tup1)                   # (10, 20, 30)

empty = ()
print(empty)                  # ()

single = (5,)
print(single)                 # (5,)

# Indexing
print(tup1[0])                # 10
print(tup1[-1])               # 30

# Slicing
print(tup1[1:3])              # (20, 30)
print(tup1[:2])               # (10, 20)

# Membership test
print(20 in tup1)             # True
print(40 not in tup1)         # True

# Immutability check (will raise an error if uncommented)
# tup1[0] = 100    # TypeError

"""
-----------------------------------------------
Intermediate Level Examples
-----------------------------------------------
"""

# Tuple concatenation and repetition
a = (1, 2)
b = (3, 4)
combined = a + b
print(combined)               # (1, 2, 3, 4)

repeated = ('Hi',) * 3
print(repeated)               # ('Hi', 'Hi', 'Hi')

# Tuple unpacking
coordinates = (5, 10, 15)
x, y, z = coordinates
print(x, y, z)                # 5 10 15

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1])              # (3, 4)
print(nested[1][0])           # 3

# Using built-in functions
nums = (2, 7, 1, 8, 2, 8)
print(len(nums))              # 6
print(sum(nums))              # 28
print(min(nums))              # 1
print(max(nums))              # 8
print(sorted(nums))           # [1, 2, 2, 7, 8, 8] (returns a list)

# Tuple methods: count and index
print(nums.count(2))          # 2
print(nums.index(8))          # 3 (first occurrence)

"""
-----------------------------------------------
Advanced Level Examples
-----------------------------------------------
"""

# Tuple comprehension does not exist, but you can use generator expressions and convert to tuple:
t = tuple(x*2 for x in range(4))
print(t)                      # (0, 2, 4, 6)

# Packing and unpacking with *
start, *middle, end = (10, 20, 30, 40, 50)
print(start)                  # 10
print(middle)                 # [20, 30, 40]
print(end)                    # 50

# Swapping variables with tuple unpacking
a, b = 1, 2
a, b = b, a
print(a, b)                   # 2 1

# Zipping and unzipping using tuples
names = ('Sai', 'Amy', 'Max')
scores = (90, 85, 88)
zipped = tuple(zip(names, scores))
print(zipped)                 # (('Sai', 90), ('Amy', 85), ('Max', 88))

unzipped = list(zip(*zipped))
print(unzipped)               # [('Sai', 'Amy', 'Max'), (90, 85, 88)]

# Tuples as dictionary keys (must be immutable type)
cities = {('Pune', 'IN'): 5_000_000, ('Paris', 'FR'): 2_100_000}
print(cities[('Paris', 'FR')])  # 2100000

"""
-----------------------------------------------
Mini Project: Tuple-Based Student Score Analyzer
-----------------------------------------------

Features:
- Accept list of tuples with (student_name, score).
- Print all entries.
- Find student(s) with highest and lowest score.
- Calculate average score.
- List students who scored above the average.

"""

def student_score_analyzer(records):
    print("All records (name, score):")
    for name, score in records:
        print(f"  {name:10s} : {score}")
    # Highest and lowest
    max_score = max(records, key=lambda x: x[1])[1]
    min_score = min(records, key=lambda x: x[1])[1]
    print("\nTop scorer(s):")
    for name, score in records:
        if score == max_score:
            print(f"  {name} : {score}")
    print("Lowest scorer(s):")
    for name, score in records:
        if score == min_score:
            print(f"  {name} : {score}")
    # Average and above average
    scores = tuple(score for _, score in records)
    avg = sum(scores) / len(scores)
    print(f"\nAverage score: {avg:.2f}")
    print("Above average:")
    for name, score in records:
        if score > avg:
            print(f"  {name} : {score}")

if __name__ == "__main__":
    students = (
        ("Sai", 90),
        ("Amy", 85),
        ("Max", 92),
        ("Tara", 88),
        ("John", 76)
    )
    student_score_analyzer(students)

'''
------------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (PYTHON TUPLE)
------------------------------------------------------------------

Q1: What is the difference between list and tuple in Python? When would you use a tuple instead of a list?
A1: Lists are mutable (can change/replace/add/remove elements), while tuples are immutable (cannot change after creation). Tuples are faster, safer for "write-protecting" data, and are hashable (usable as dictionary keys). Use tuples for fixed collections (e.g., geographic coordinates).

Q2: How does tuple packing and unpacking work? Give examples including *star unpacking.
A2:
Packing:
point = (10, 20)
Unpacking:
x, y = point  # x=10, y=20

*Star unpacking:
nums = (1,2,3,4,5)
first, *middle, last = nums  # first=1; middle=[2,3,4]; last=5

Q3: Can you have mutable objects inside a tuple? Demonstrate consequences.
A3: Yes, if the tuple contains e.g., a list, the tuple's reference is immutable but the list inside can be changed.
t = ([1,2,3], 4)
t[0].append(99)
print(t)  # ([1, 2, 3, 99], 4)

Q4: How can you count the number of times an element appears in a tuple? Find its index?
A4:
t = (1,2,2,3)
t.count(2)      # 2
t.index(3)      # 3

Q5: How would you convert a tuple to a list and vice versa? Why might you do this?
A5:
t = (1,2,3)
lst = list(t)      # [1,2,3]
tup2 = tuple(lst)  # (1,2,3)
This helps to edit a tuple (convert to list, modify, back to tuple).

Q6: What happens if you try to modify a tuple after creation?
A6: Raises a TypeError; tuples are immutable:
t = (1,2,3)
# t[0] = 99   # TypeError

Q7: How can you use tuples with dictionaries? Why can't lists be used as dict keys?
A7: Tuples (being immutable) can be used as dict keys:
locations = { (10,20): "A", (30,40): "B" }
Lists are mutable & unhashable, so can't be dict keys.

Q8: What's the output?
t = (1,2,3)
print(t*2)
A8: (1,2,3,1,2,3)

Q9: How can you "flatten" a tuple of tuples?
A9:
nested = ((1,2), (3,4))
flat = tuple(x for tup in nested for x in tup)   # (1,2,3,4)

Q10: Give a real-world scenario where tuples should be preferred over lists.
A10: When representing fixed-size, positionally-meaningful records such as (latitude, longitude), or RGB color triplets, since these should not be modified.

------------------------------------------------------------------
'''
