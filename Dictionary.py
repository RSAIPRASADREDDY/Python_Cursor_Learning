"""
Python Dictionary: Concepts, Methods, Examples, Mini-project, and Interview Q&A

Definition:
-----------
A dictionary in Python is an unordered, mutable collection of key-value pairs. 
Keys must be unique and immutable (strings, numbers, tuples), while values can be of any type.

Dictionary Methods and Concepts:
-------------------------------
- Creation & Initialization
- Accessing elements by key
- Adding, Updating, and Removing items
- Built-in Functions: len(), dict(), sorted(), keys(), values(), items(), etc.
- Dictionary Methods: .get(), .pop(), .popitem(), .setdefault(), .update(), .clear(), .copy(), .fromkeys()
- Iterating dictionaries
- Membership ("key in dict")
- Dictionary comprehensions
- Nested dictionaries

Syntax:
-------
# Creating a dictionary
my_dict = {'name': 'Sai', 'age': 21}
empty = {}
"""

# -----------------------------------------------
# Beginner Level Examples
# -----------------------------------------------

# Creating dictionaries
from multiprocessing import Value


d = {'name': 'Sai', 'age': 21, 'city': 'Bangalore'}
print(d)    # {'name': 'Sai', 'age': 21, 'city': 'Hyderabad'}


# Accessing values
print(d['name'])     # Sai

# Adding new key-value pairs
d['country'] = 'India'
print(d)             # {'name': ..., 'age': ..., 'city': ..., 'country': 'India'}

# Modifying a value
d['age'] = 22
print(d['age'])      # 22
print(d) 

# Removing a key
del d['city']
print(d)             # {'name': ..., 'age': ..., 'country': ...}

# Using .get() to access (avoids KeyError)
print(d.get('email'))      # None (because 'email' key does not exist)
print(d.get('email', 'N/A'))  # N/A

# Length of a dictionary
print(len(d))         # 3

# -----------------------------------------------
# Intermediate Level Examples
# -----------------------------------------------

# Iterating over dictionary
student = {"name": "Amy", "grade": 95,"city": "Bangalore"}
for key in student:
    print(key, student[key])
    #print(key, value)

for value in student.values():
    print(value)

for k, v in student.items():
    print(f"{k} => {v}")

# Checking if key exists
if "grade" in student:
    print("Grade available.")

# Removing items
removed_grade = student.pop("grade")
print(removed_grade)  # 95
print(student)        # {'name': 'Amy'}

# popitem() removes last inserted (Python >=3.7)
pair = student.popitem()
print(pair)           # ('name', 'Amy')
print(student)        # {}

# clear() empties the dictionary
mydict = {'a': 1, 'b': 2}
mydict.clear()
print(mydict)         # {}

# Re-creating with dict() and fromkeys()
d = dict(x=10, y=20)
print(d)              # {'x': 10, 'y': 20}
keys = ['alpha', 'beta', 'gamma']
init = dict.fromkeys(keys, 0)
print(init)           # {'alpha': 0, 'beta': 0, 'gamma': 0}

# Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)        # {1:1, 2:4, 3:9, 4:16, 5:25}

# -----------------------------------------------
# Advanced Level Examples
# -----------------------------------------------

# Nested dictionaries
team = {
    "Alice": {"role": "dev", "skills": ["python", "sql"]},
    "Bob":   {"role": "manager", "skills": ["excel", "ppt"]}
}
print(team["Alice"]["skills"])    # ['python', 'sql']

# Merging two dicts (Python 3.5+)
d1 = {'a': 100, 'b': 200}
d2 = {'b': 999, 'c': 300}
d1.update(d2)
print(d1)   # {'a': 100, 'b': 999, 'c': 300}

# Dictionary view objects are dynamic
orig = {"x": 1}
keys_view = orig.keys()
print(keys_view)      # dict_keys(['x'])
orig['y'] = 2
print(keys_view)      # dict_keys(['x', 'y'])

# Sorting dictionaries by key
grades = {'Sai': 85, 'Amy': 92, 'Bob': 78}
for k in sorted(grades):
    print(f"{k}: {grades[k]}")   # Amy, Bob, Sai order

# Reversing keys and values
inv = {v: k for k, v in grades.items()}
print(inv)             # {85: 'Sai', 92: 'Amy', 78: 'Bob'}

# Using setdefault()
d = {}
for ch in "banana":
    d.setdefault(ch, 0)
    d[ch] += 1
print(d)   # {'b': 1, 'a': 3, 'n': 2}

# Making a frequency counter (alternative way)
from collections import Counter
print(Counter("mississippi"))  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})


# -----------------------------------------------
# Mini-Project: Simple Phonebook using Dictionary
# -----------------------------------------------

def phonebook():
    print("=== Phonebook Mini Project ===")
    pb = {}
    while True:
        print("\n1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. List Contacts\n5. Exit")
        choice = input("Choose option: ")
        if choice == '1':
            name = input("Contact name: ")
            number = input("Phone number: ")
            pb[name] = number
            print("Contact saved.")
        elif choice == '2':
            name = input("Name to search: ")
            if name in pb:
                print(f"{name}'s number: {pb[name]}")
            else:
                print("Contact not found.")
        elif choice == '3':
            name = input("Name to delete: ")
            if pb.pop(name, None):
                print("Deleted.")
            else:
                print("Contact not found.")
        elif choice == '4':
            if not pb:
                print("Phonebook empty.")
            else:
                for n, num in pb.items():
                    print(f"{n}: {num}")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid. Try again.")

# Uncomment to run the mini-project:
# phonebook()

'''
------------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (PYTHON DICTIONARY)
------------------------------------------------------------------

Q1: What is the primary difference between a list and a dictionary?
A1: List stores values with numeric indices, while dictionary stores key-value pairs with unique, typically non-numeric keys.

Q2: Can a dictionary key be mutable? Why or why not?
A2: No, if you try to use a mutable type (e.g., list) as a dictionary key, Python raises a TypeError. Only immutable types like string, number, or tuple can be dictionary keys, because dictionary keys must be hashable.

Q3: How can you loop over both keys and values of a dictionary?
A3:
d = {"a": 1, "b": 2}
for k, v in d.items():
    print(k, v)

Q4: What is .get()? Why use it over d[key]?
A4: .get() safely fetches a value; returns None (or a default) if key is missing, avoiding KeyError. d[key] raises KeyError if key is absent.

Q5: How do you merge two dictionaries? What happens with overlapping keys?
A5: Use .update() or {**d1, **d2} (for Python 3.5+). Overlapping keys: values from the last dict overwrite earlier ones.

Q6: How can you create a dictionary from lists of keys and values?
A6:
keys = ['a', 'b']
values = [1, 2]
d = dict(zip(keys, values))   # {'a':1, 'b':2}

Q7: Explain the result of d = {}; d['x'] = d. Is this allowed?
A7: Allowed, creates a self-reference; {'x': {...}}. Printing it shows {...: {...}}, which means recursion. Use with care (often source of bugs).

Q8: Give an example of dictionary comprehension with condition.
A8:
nums = [1,2,3,4]
squares_even = {x: x*x for x in nums if x%2==0}  # {2:4, 4:16}

Q9: How do you make a dictionary “read only”?
A9: There's no built-in read-only dict, but you can use collections.ChainMap, types.MappingProxyType, or custom objects for this.

Q10: How to count word frequency in a sentence using a dictionary (without Counter)?
A10:
s = "to be or not to be"
counter = {}
for word in s.split():
    counter[word] = counter.get(word, 0) + 1
# counter => {'to': 2, 'be': 2, 'or': 1, 'not': 1}

------------------------------------------------------------------
'''
