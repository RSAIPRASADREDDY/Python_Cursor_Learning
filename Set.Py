"""
Python Set: Concepts, Methods, Examples, Mini-project, and Interview Q&A

Definition:
-----------
A set in Python is an unordered collection of unique and immutable elements. Sets are mutable themselves (you can add/remove elements), but the elements must be hashable (such as numbers, strings, or tuples of immutable objects).

Set Methods and Concepts:
--------------------------
- Creation & Initialization
- Basic methods: add(), update(), remove(), discard(), pop(), clear()
- Membership testing
- Mathematical operations: union (|), intersection (&), difference (-), symmetric_difference (^)
- Set relations: issubset(), issuperset(), isdisjoint()
- Copying sets
- Removing duplicates from iterables
- Built-in set() constructor
- Set comprehension

Syntax:
-------
# Creation
s = {1, 2, 3}
s2 = set([1, 2, 3, 4])
empty = set()   # not {} (that’s a dict)

# Adding elements
s.add(4)
s.update([5, 6])

# Removing elements
s.remove(2)         # KeyError if 2 not found
s.discard(10)       # No error if 10 not found
s.pop()             # Removes arbitrary element

# Set operations
a | b         # union
a & b         # intersection
a - b         # difference
a ^ b         # symmetric difference

# Membership
if 5 in s:
    print("Found!")
"""

# -----------------------------------------------
# Beginner Level Examples
# -----------------------------------------------

# Creating sets
fruits = {'apple', 'banana', 'cherry'}
print(fruits)  # Unordered, may print: {'banana', 'cherry', 'apple'}

# Creating set from a list (removes duplicates)
nums = set([1, 2, 2, 3, 4, 4])
print(nums)  # {1, 2, 3, 4}

# Adding and removing elements
colors = set()
colors.add('red')
colors.add('blue')
colors.discard('green')  # No error even if not present
print(colors)  # {'red', 'blue'}

# Membership test
print('apple' in fruits)     # True
print('orange' not in fruits)  # True

# -----------------------------------------------
# Intermediate Level Examples
# -----------------------------------------------

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)    # Union: {1, 2, 3, 4, 5}
print(a & b)    # Intersection: {3}
print(a - b)    # Difference: {1, 2}
print(a ^ b)    # Symmetric difference: {1, 2, 4, 5}

# Update methods
a.update([6, 7])
print(a)        # {1, 2, 3, 6, 7}

# Remove vs discard
a.remove(3)     # Removes 3
# a.remove(99)  # KeyError!
a.discard(99)   # Safe: does nothing if not present

# pop() removes arbitrary element
removed = a.pop()
print(f"Removed: {removed}, Remaining: {a}")

# Clear a set
b.clear()
print(b)        # set()

# Set comprehension
squares = {x*x for x in range(1, 6)}
print(squares)  # {1, 4, 9, 16, 25}

# -----------------------------------------------
# Advanced Level Examples
# -----------------------------------------------

# Removing duplicates from string using set
text = "abracadabra"
unique_letters = set(text)
print(unique_letters)  # set of unique letters

# Set relations
A = {1,2,3}
B = {1,2,3,4,5}
C = {10, 11}
print(A.issubset(B))     # True
print(B.issuperset(A))   # True
print(A.isdisjoint(C))   # True

# Frozenset: immutable set
fs = frozenset([1,2,2,3])
print(fs)                # frozenset({1, 2, 3})
# fs.add(4)  # AttributeError

# Iterating sets
for element in unique_letters:
    print(element, end=' ')
print()

# Set from list of tuples
coords = {(1,2), (3,4), (1,2)}   # duplicates removed
print(coords)    # {(1,2), (3,4)}

# Set difference update
A = {1,2,3,4}
B = {3,4,5}
A.difference_update(B)
print(A)         # {1, 2}

# -----------------------------------------------
# Mini Project: Unique Word Extractor & Analyzer
# -----------------------------------------------

def unique_word_analyzer(text):
    """Analyze unique words in a given text using sets."""
    words = text.lower().split()
    word_set = set(words)
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(word_set)}")
    print(f"Unique (sorted): {sorted(word_set)}")

    # Words occurring once
    from collections import Counter
    freq = Counter(words)
    singletons = {w for w in word_set if freq[w] == 1}
    print(f"Words that occur only once: {singletons}")
    print()
    # Find common words with another sentence
    another = "python is easy to use but powerful"
    other_words = set(another.split())
    print(f"Common words with '{another}': {word_set & other_words}")

if __name__ == "__main__":
    sample = "Python is great and Python is easy and powerful"
    print(">>> Mini Project: Unique Word Analyzer <<<")
    unique_word_analyzer(sample)


'''
------------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (PYTHON SET)
------------------------------------------------------------------

Q1: What is the difference between a set and a list in Python? When would you use a set?
A1: Sets are unordered collections of unique elements; lists are ordered and can have duplicates. Use a set for fast membership testing, removing duplicates, or when order is not important.

Q2: How do you remove duplicates from a list? Explain efficiency compared to preserving order.
A2:
lst = [1,2,2,3,3,4]
unique = set(lst)      # Removes duplicates but order lost (O(n))
Preserve order:
res = []
seen = set()
for x in lst:
    if x not in seen:
        res.append(x)
        seen.add(x)
# res = [1,2,3,4]
Using a set is faster for large data.

Q3: Explain difference between remove(), discard(), and pop() methods in sets.
A3:
- remove(x): Removes element x, raises KeyError if x not present.
- discard(x): Removes element x if present, does nothing if not.
- pop(): Removes and returns arbitrary element (not by index/key).
Example:
s = {1,2}
s.remove(1)  # OK
s.discard(3) # OK (does nothing)
s.pop()      # Removes some element

Q4: How can you find common, unique, or differing elements in two sets?
A4:
a = {1, 2, 3}
b = {2, 3, 4}
Common: a & b           # {2,3}
Unique to a: a - b      # {1}
Unique to both: a ^ b   # {1,4}
Union: a | b            # {1,2,3,4}

Q5: What is a frozenset and how does it differ from a normal set? When is it useful?
A5: frozenset is an immutable set; elements can't be added/removed after creation. Useful as keys in dicts, or for storing sets inside other sets.

Q6: How does Python determine uniqueness in a set? What happens if you add a list to a set?
A6: Python uses the hash of each element. Mutable items like lists cannot be added (TypeError: unhashable type).
Example:
s = set()
s.add([1,2])  # TypeError

Q7: How would you check if one set is a subset/superset of another? Give a code example.
A7:
a = {1,2}
b = {1,2,3}
print(a.issubset(b))    # True
print(b.issuperset(a))  # True

Q8: Demonstrate set comprehension with a conditional.
A8:
evens = {x for x in range(10) if x % 2 == 0}        # {0, 2, 4, 6, 8}

Q9: Can you sort a set? Why or why not? How to get a sorted version?
A9: Sets are unordered and cannot be sorted in-place. Use sorted(s) to get a list of sorted elements.

Q10: Suppose you have two sets: all students and those who submitted an assignment.
How do you get a set of students who did NOT submit?
A10:
all_students = {"Alice", "Bob", "Chris"}
submitted = {"Bob"}
not_submitted = all_students - submitted     # {"Alice", "Chris"}

------------------------------------------------------------------
'''
