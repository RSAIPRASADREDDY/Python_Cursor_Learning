"""
Python List: Concepts, Methods, Examples, Mini-project, and Interview Q&A

Definition:
-----------
A list in Python is an ordered, mutable (changeable) collection of elements. Lists can store items of mixed data types (integers, strings, floats, even other lists).

List Methods and Concepts:
--------------------------
- Creation & Initialization
- Indexing & Slicing
- Concatenation (+), Repetition (*)
- Built-in Functions: len(), list(), sum(), min(), max(), sorted(), etc.
- List Methods: .append(), .extend(), .insert(), .remove(), .pop(), .clear(), .index(), .count(), .reverse(), .sort(), .copy()
- Iterating Lists
- Membership, List Comprehensions
- Nested Lists (2D lists/matrices)
- List unpacking

Syntax:
-------
"""
# Creation
from copy import deepcopy


lst = [1, 2, 3, 'Sai']
empty = []
#print(lst,type(lst))
#print(empty,type(empty))



# Indexing
item = lst[0]
item = lst[-1]
#print(item)


# Slicing
sublist = lst[1:3]

# Adding
lst.append(4)   # At end
lst.extend([5, 6])
#print(lst)
lst.insert(2, 'hello')
lst.insert(-2, 2)
#print(lst)

# Removing
lst.remove(2)
#print(lst)
val = lst.pop()    # Remove last
#print(lst)
#print(val)
#lst.clear()        # Empty list
#print(lst)

# Length
len(lst)


# Iteration
for x in lst:
    print(x)


# Membership
if 3  in lst:
    print("Yes")

"""
-----------------------------------------------
Beginner Level Examples
-----------------------------------------------
"""

# Creating a list
nums = [10, 20, 30, 40]
print(nums)                 # [10, 20, 30, 40]
#exit()
# Mixed data types
mixed = [1, "Sai", 2.5, False]
print(mixed)

# Indexing
print(nums[0])              # 10
print(nums[-1])             # 40

# Slicing
print(nums[1:3])            # [20, 30]
print(nums[:2])             # [10, 20]

# List concatenation & repetition
l1 = [1,2]
l2 = [3,4]
print(l1 + l2)              # [1, 2, 3, 4]
print(l1 * 3)               # [1, 2, 1, 2, 1, 2]

# Adding elements
colors = ['red', 'green']
colors.append('blue')
print(colors)               # ['red', 'green', 'blue']

# Removing elements
colors.remove('green')
print(colors)               # ['red', 'blue']

# Popping elements
last = colors.pop()
print(last)                 # 'blue'
print(colors)               # ['red']

# Checking membership
print('red' in colors)      # True
print('green' not in colors) # True

"""
-----------------------------------------------
Intermediate Level Examples
-----------------------------------------------
"""

# Using extend and insert
fruits = ['apple', 'banana']
fruits.extend(['cherry', 'date'])
print(fruits)   # ['apple', 'banana', 'cherry', 'date']

fruits.insert(1, 'orange')
print(fruits)   # ['apple', 'orange', 'banana', 'cherry', 'date']

# Counting and finding index
nums = [1, 2, 2, 3, 2, 4]
print(nums.count(2))        # 3
print(nums.index(3))        # 3 (first occurrence)

# Sorting and reversing
nums = [5, 2, 9, 1]
nums.sort()
print(nums)                 # [1, 2, 5, 9]
nums.reverse()
print(nums)                 # [9, 5, 2, 1]
#exit()
# List comprehension (squares of numbers 0-4)
squares = [x*x for x in range(5)]
print(squares)              # [0, 1, 4, 9, 16]

# Filtering even numbers
evens = [x for x in nums if x % 2 == 0]
print(evens)

# Copying lists (shallow copy)
a = [1, 2, 3]
b = a.copy()
#diffirence of copy and  deepcopy
from copy import deepcopy

# Difference of copy() and deepcopy():
# - copy() creates a shallow copy of the list: it copies the outer list object, 
#   but if the list contains any mutable objects (like another list), 
#   both the original and the copy refer to the same inner objects.
# - deepcopy() creates a deep copy, copying not just the outer list but also recursively copies all objects inside.

# Demonstration:
shallow = [[1, 2], [3, 4]]
copy1 = shallow.copy()         # Shallow copy
copy2 = deepcopy(shallow)      # Deep copy

shallow[0][0] = 999
print(shallow)    # [[999, 2], [3, 4]]
print(copy1)      # [[999, 2], [3, 4]]   # changed, because the inner lists are shared!
print(copy2)      # [[1, 2], [3, 4]]     # not changed, because deepcopy copied the inner lists


a.append(4)
print(a)                    # [1, 2, 3, 4]
print(b)                    # [1, 2, 3]

# Nested lists (matrix)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])         # 6

"""
-----------------------------------------------
Advanced Level Examples
-----------------------------------------------
"""

# Flattening a list of lists
nested = [[1,2], [3,4], [5,6]]
flat = [item for sublist in nested for item in sublist]
'''
flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)
'''
print(flat)                 # [1, 2, 3, 4, 5, 6]

# Using enumerate during iteration
lst = ['R', 'E', 'D','D','Y']
for idx, val in enumerate(lst):
    #print(len(lst))
    #neg_i = idx - len(lst)
    print(idx, val)
#exit()
# Unpacking lists
x, y, z = [1, 2, 3]
print(x, y, z)
#exit()

# Using * to grab rest of the items
first, *middle, last = [10, 20, 30, 40, 50]
print(first)    # 10
print(middle)   # [20, 30, 40]
print(last)     # 50
#exit()
# Set operations on lists (removing duplicates)
nums = [1,2,2,3,3,3]
unique = list(set(nums))
print(unique)

# List comprehensions with conditionals
words = ['hello', 'sai', 'python', 'madam']
#print(words[::-1])
palindromes = [w for w in words if w == w[::-1]]
print(palindromes)          # ['madam']
#exit()


# Zipping lists together
names = ['Sai', 'Amy']
scores = [85, 90]
combined = list(zip(names, scores))
print(combined)             # [('Sai', 85), ('Amy', 90)]

# Using map and filter
nums = [1,2,3,4,5]
doubled = list(map(lambda x: x*2, nums))
print(doubled)

filtered = list(filter(lambda x: x%2==0, nums))
print(filtered)
#exit()


# Deleting elements with del
lst = [0, 1, 2, 3, 4]
del lst[2]
print(lst)                  # [0, 1, 3, 4]

# Generating a 2D array (matrix) using list comprehension
matrix = [[col for col in range(4)] for row in range(3)]
print(matrix)
#exit()
"""
-----------------------------------------------
Mini Project: Basic List Organizer
-----------------------------------------------

Features:
- Allow user to enter a list of items (comma-separated input).
- Print: original list, sorted list (A-Z), reversed list, without duplicates.
- Add & remove items dynamically.
- Count occurrences of a given value.
- Display stats (length, unique count, top-3 frequent items).

"""

from collections import Counter

def list_organizer():
    raw = input("Enter items, separated by commas: ")
    lst = [x.strip() for x in raw.split(',') if x.strip()]
    if not lst:
        print("No input! Using demo list.")
        lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print("\nOriginal List:", lst)
    print("Sorted (A-Z):", sorted(lst))
    print("Reversed:", list(reversed(lst)))
    unique = list(set(lst))
    print("Unique items:", unique)
    item = input("Add an item to the list: ").strip()
    if item:
        lst.append(item)
        print("Added! List is now:", lst)
    rem = input("Remove an item (leave empty to skip): ").strip()
    if rem and rem in lst:
        lst.remove(rem)
        print("Removed! List is now:", lst)
    query = input("Enter value to count occurrences: ").strip()
    if query:
        print(f"Count of {query!r}: {lst.count(query)}")
    data = Counter(lst)
    print("List stats: length =", len(lst), "| unique =", len(set(lst)))
    print("Top 3 items by frequency:", data.most_common(3))

if __name__ == "__main__":
    try:
        list_organizer()
    except EOFError:
        # No stdin (e.g., in automated runs, use default)
        print("(No user input. Using demo scenario)")
        import sys
        sys.stdin = open('/dev/null')
        from io import StringIO
        input = lambda _: ""
        list_organizer()

'''
------------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (PYTHON LIST)
------------------------------------------------------------------

Q1: What is the difference between list and tuple in Python?
A1: Lists are mutable (you can change, add, remove elements), whereas tuples are immutable. Example:
lst = [1,2,3]; lst[0]=5  # OK
tup = (1,2,3); tup[0]=5  # TypeError

Q2: Show how slicing works on lists and what happens with negative indices.
A2: Slicing extracts parts of a list.
lst = [10, 20, 30, 40, 50]
lst[1:4] -> [20, 30, 40]
lst[-3:-1] -> [30, 40]

Q3: How can you remove all duplicates from a Python list while preserving order?
A3:
lst = [1,2,2,3,4,3]
res = []
for x in lst:
    if x not in res:
        res.append(x)
# res -> [1, 2, 3, 4]

Q4: What is list comprehension? Give an example filtering items.
A4: It's a concise way to create lists.
nums = [1,2,3,4,5]
odds = [x for x in nums if x%2==1]  # [1,3,5]

Q5: How can you reverse a list “in-place”? How about creating a new reversed list?
A5:
lst = [1,2,3]
lst.reverse()     # In-place
rev = lst[::-1]   # New reversed list

Q6: How do you find the second largest element in a list?
A6:
lst = [10,20,4,45,99]
res = list(set(lst))
res.sort()
second_largest = res[-2]  # 45

Q7: How can you flatten a nested list or list of lists?
A7:
from itertools import chain
nested = [[1,2],[3,4]]
flat = list(chain.from_iterable(nested))  # [1,2,3,4]

Q8: What's the difference between ".append()" and ".extend()" methods?
A8:
.append(x) adds one item to the end: [1,2].append([3,4]) -> [1,2,[3,4]]
.extend(x) adds all elements: [1,2].extend([3,4]) -> [1,2,3,4]

Q9: How do you count the number of occurrences of each element in a list?
A9:
from collections import Counter
lst = [1,2,2,3]
Counter(lst)  # Counter({2: 2, 1: 1, 3: 1})

Q10: Give a one-liner to generate a list of squares of even numbers between 1-10.
A10:
[x**2 for x in range(1,11) if x%2==0]   # [4, 16, 36, 64, 100]

------------------------------------------------------------------
'''
