"""
Python filter() Function: Concept, Methods, Syntax, Examples, Mini-Project, and Interview Q&A

Definition:
-----------
The `filter()` function in Python constructs an iterator from elements of an iterable for which a function returns True. It is typically used to extract, select, or filter out values from a collection according to some condition.

Methods and Usage:
------------------
- `filter(function, iterable)` – Applies the given function to each element in the iterable and returns only those elements for which the function evaluates to True.
- The result is a filter object (an iterator); commonly converted to a list or tuple for display/use: `list(filter(...))` or `tuple(filter(...))`.

Syntax:
-------
filter(function, iterable)

# function: Function that returns True or False for each element.
# iterable: Sequence or collection (like list, tuple, string, set, etc.)

# Example: Filter all even numbers from a list
evens = list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5]))
"""

# -----------------------------------------------
# Beginner Level Examples for filter()
# -----------------------------------------------

# Example 1: Using filter() with a built-in function (None)
nums = [0, 1, 2, 0, 5, '', 'hello', None]
non_zeros = list(filter(None, nums))
print(non_zeros)  # [1, 2, 5, 'hello']

# Example 2: Using filter() with a lambda to filter even numbers
numbers = [1, 4, 5, 6, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [4, 6, 10]

# Example 3: Filtering strings by length
names = ["Amy", "Ben", "Sai", "A", "Bob", "Elke"]
long_names = list(filter(lambda name: len(name) > 2, names))
print(long_names)  # ['Amy', 'Ben', 'Sai', 'Bob', 'Elke']

# -----------------------------------------------
# Intermediate Level Examples for filter()
# -----------------------------------------------

# Example 4: Filtering with user-defined function
def is_positive(n):
    return n > 0

nums = [-3, -2, -1, 0, 1, 2, 3]
positives = list(filter(is_positive, nums))
print(positives)  # [1, 2, 3]

# Example 5: Extract only vowels from a string
s = "Hello World!"
vowels = list(filter(lambda ch: ch.lower() in 'aeiou', s))
print(vowels)  # ['e', 'o', 'o']

# Example 6: Filtering a list of tuples
data = [("Sai", 80), ("Amy", 55), ("Bob", 95)]
passed = list(filter(lambda tup: tup[1] >= 60, data))
print(passed)  # [('Sai', 80), ('Bob', 95)]

# Example 7: Filtering dictionary keys based on values
d = {"a": 3, "b": 8, "c": 0, "d": 5}
high = list(filter(lambda k: d[k] > 5, d))
print(high)   # ['b']

# -----------------------------------------------
# Advanced Level Examples for filter()
# -----------------------------------------------

# Example 8: Filter palindromic words
words = ["level", "python", "radar", "filter", "civic"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print(palindromes)  # ['level', 'radar', 'civic']

# Example 9: Filtering prime numbers in a list
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = list(range(1, 20))
primes = list(filter(is_prime, nums))
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19]

# Example 10: Removing empty strings from a list
arr = ['Sai', '', 'Amy', '', 'Data', None]
non_empty = list(filter(None, arr))
print(non_empty)  # ['Sai', 'Amy', 'Data']

# Example 11: Filter students scoring distinction
students = [
    {"name": "Sai", "score": 92},
    {"name": "Amy", "score": 75},
    {"name": "Bob", "score": 88},
    {"name": "Zara", "score": 99}
]
distinction = list(filter(lambda s: s['score'] >= 90, students))
print(distinction)  # [{'name': 'Sai', 'score': 92}, {'name': 'Zara', 'score': 99}]

# Example 12: filter with multiple iterables (with zip + filter)
pairs = [(1, 3), (2, 4), (6, 2), (7, 7)]
same = list(filter(lambda t: t[0] == t[1], pairs))
print(same)  # [(7, 7)]

# -----------------------------------------------
# Mini-Project: Filter Emails by Domain using filter()
# -----------------------------------------------

def email_filter_project():
    """
    Simple mini-project that filters a list of email addresses by a specified domain using filter().
    """
    print("=== Filter Emails by Domain ===")
    emails = input("Enter emails (comma-separated): ").split(",")
    domain = input("Enter domain to filter (e.g. gmail.com): ").strip()

    # Function to check if email contains the domain
    def has_domain(email):
        return email.strip().endswith("@" + domain)
    
    filtered = list(filter(has_domain, emails))

    print(f"\n--- Emails with @{domain} domain ---")
    if filtered:
        for e in map(str.strip, filtered):
            print(e)
    else:
        print("No emails found for the given domain.")

# Uncomment below to run the mini-project:
# email_filter_project()


'''
------------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (PYTHON FILTER FUNCTION)
------------------------------------------------------------------

Q1: What is the filter() function in Python and what does it return?
A1: The filter() function selects elements from an iterable for which a provided function returns True. It returns a filter object (iterator), which can be converted to list or tuple, containing only the filtered elements.

Example:
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

Q2: How does filter() differ from map()? Can you give a use case for both together?
A2: map() transforms each element; filter() selects a subset of elements. You can use them together to transform only selected items.

Example:
nums = [1, 2, 3, 4]
squared_evens = list(map(lambda x: x**2, filter(lambda n: n % 2 == 0, nums)))
# Output: [4, 16]  # squares of 2 and 4

Q3: Explain what happens if you pass None as the function to filter().
A3: If function is None, filter() removes all "falsy" values from the iterable (such as 0, '', None, False, []). Only truthy values remain.

Example:
vals = [None, 1, '', 3, 0]
print(list(filter(None, vals)))  # [1, 3]

Q4: How would you filter for unique elements in a list using filter()?
A4: You must use a helper set to track seen items during filtering.

Example:
lst = [1, 2, 2, 3, 1, 4]
seen = set()
unique = list(filter(lambda x: not (x in seen or seen.add(x)), lst))
print(unique)  # [1, 2, 3, 4]

Q5: Given a dictionary of employees and salaries, how do you use filter() to get only those earning above 50,000?
A5:
salaries = {"Sai": 47000, "Amy": 65000, "Zara": 80000}
result = list(filter(lambda key: salaries[key] > 50000, salaries))
print(result)  # ['Amy', 'Zara']

Q6: Can you use filter() with custom classes or objects? Give an example.
A6: Yes. Any object can be filtered as long as the function returns True or False for it.

Example:
class Student:
    def __init__(self, name, marks): self.name, self.marks = name, marks

lst = [Student("Sai", 92), Student("Amy", 75)]
topper = list(filter(lambda s: s.marks > 90, lst))
print([s.name for s in topper])  # ['Sai']

Q7: How can you filter for items at even indexes in a list using filter()?
A7:
lst = ['a', 'b', 'c', 'd', 'e']
result = list(filter(lambda x: lst.index(x) % 2 == 0, lst))
print(result)  # ['a', 'c', 'e']  # Note: This approach retrieves first occurrence only.

Q8: Explain how filter() behaves with strings. Can you filter characters?
A8: Yes, since a string is iterable, filter() can be used to select certain characters.

Example:
s = "filter123"
letters = list(filter(str.isalpha, s))
print(letters)  # ['f', 'i', 'l', 't', 'e', 'r']

Q9: How to filter nested lists for sublists containing a specific value?
A9:
data = [[1,2], [4,5], [2,3], [7,8]]
filtered = list(filter(lambda sub: 2 in sub, data))
print(filtered)  # [[1, 2], [2, 3]]

Q10: What happens if the function you pass to filter() raises an Exception? How is this handled?
A10: If the function raises an exception for any element during filtering, the filtering stops and the error propagates upward—no automatic handling. You can use try/except inside the function to skip problematic entries.

------------------------------------------------------------------
'''
