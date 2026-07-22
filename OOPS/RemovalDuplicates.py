'''
Removing Duplicates in Python
-----------------------------

Definition:
-----------
Removing duplicates refers to eliminating repeated elements from collections such as lists, strings, or other iterables in Python, so that each element appears only once.

Why Important?
--------------
- Useful in data cleaning, deduplication of emails, phone numbers, user IDs, etc.
- Helps maintain uniqueness constraints.

Common Methods for Removing Duplicates:
---------------------------------------
1. Using set()        : Unordered, all duplicates removed.
2. Using dict.fromkeys(): Preserves insertion order (Python 3.7+).
3. List Comprehension : Can be used with additional logic for more control.
4. Using collections.OrderedDict (Py <3.7): To preserve order.
5. For strings: set(), "".join(), or custom logic for order.

Syntax Examples:
----------------
# Using set()
unique_list = list(set(original_list))

# Using dict.fromkeys() for order preservation
unique_list = list(dict.fromkeys(original_list))

# List comprehension + seen set
seen = set()
unique_list = [x for x in original_list if not (x in seen or seen.add(x))]
'''

# -------------------
# Beginner Level Example: Remove duplicates from a simple list
print("Beginner Example:")
nums = [1, 2, 3, 2, 4, 1, 5, 3]
unique_nums = list(set(nums))
print("Unique Numbers (unordered):", unique_nums)
print()

'''
Note: Using set() is simple, but does NOT preserve original order.
'''


# -------------------
# Intermediate Level Example: Remove duplicates while preserving list order

print("Intermediate Example:")
names = ["Alice", "Bob", "Alice", "Eve", "Bob", "David"]
unique_names = list(dict.fromkeys(names))
print("Unique Names (order preserved):", unique_names)
print()

# Another variant: Remove duplicates from string, keep order
s = "bananas"
unique_chars = "".join(dict.fromkeys(s))
print("Unique characters from 'bananas':", unique_chars)
print()

# -------------------
# Advanced Level Example: Remove duplicates from list of dictionaries, based on a specific key

print("Advanced Example: Remove duplicate dicts based on 'id' field")
users = [
    {"id": 1, "name": "Tom"},
    {"id": 2, "name": "Sam"},
    {"id": 1, "name": "Tommy"},
    {"id": 3, "name": "Bob"},
    {"id": 2, "name": "Sam"},
]

def dedup_dicts_by_key(items, key):
    seen = set()
    result = []
    for d in items:
        k = d[key]
        if k not in seen:
            seen.add(k)
            result.append(d)
    return result

unique_users = dedup_dicts_by_key(users, "id")
print(unique_users)
print()

# -------------------
# Advanced: Remove duplicates from a nested list

print("Advanced Example: Remove duplicate nested lists/tuples")

nested = [(1,2), (3,4), (1,2), (5,6), (3,4)]
unique_nested = list(dict.fromkeys(nested))
print("Unique nested tuples:", unique_nested)
print()

# For lists that are unhashable (lists inside list), need to convert to tuple for hashing
nested_lists = [[1,2], [3,4], [1,2], [5,6], [3,4]]
unique_nested_lists = []
seen = set()
for sublist in nested_lists:
    t = tuple(sublist)
    if t not in seen:
        seen.add(t)
        unique_nested_lists.append(sublist)
print("Unique nested lists:", unique_nested_lists)
print()

# -------------------
# Advanced: Remove duplicates from a list of custom objects

print("Advanced Example: Remove duplicates from custom objects")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name and self.age == other.age
    def __hash__(self):
        return hash((self.name, self.age))
    def __repr__(self):
        return f"Person({self.name!r}, {self.age})"

people = [Person("Alice", 30), Person("Bob", 25), Person("Alice", 30), Person("Bob", 27)]
unique_people = list(set(people))
print(unique_people)
print()

# -------------------
'''
MINI PROJECT: Email Deduplication Utility

Create a reusable function/class that reads a list of email addresses (possibly with repeated entries, with varying casing and whitespace), removes duplicates, normalizes them (strip space, lowercase), and prints the unique emails, in original appearance order!
'''

print("Mini Project: Email Deduplication Utility")

def clean_and_deduplicate_emails(email_list):
    seen = set()
    result = []
    for email in email_list:
        cleaned = email.strip().lower()
        if cleaned not in seen:
            seen.add(cleaned)
            result.append(cleaned)
    return result

# Sample email list with duplicates, mixed case, extra spaces
raw_emails = [
    "alice@Example.com", " bob@example.com ", "alice@example.com",
    "CHARLIE@EXAMPLE.COM", "bob@example.com", "charlie@example.com",
    "Alice@EXAMPLE.com"
]

unique_clean_emails = clean_and_deduplicate_emails(raw_emails)
print("Unique, cleaned emails:")
for email in unique_clean_emails:
    print(email)
print()


'''
---------------------
Interview Questions & Answers: Duplicate Removal in Python
---------------------
'''

# Q1. What’s the difference between using set() and dict.fromkeys() for duplicate removal?
'''
A1: set() removes duplicates but does NOT preserve order. dict.fromkeys() both removes duplicates and retains the order in which elements first appeared (Python 3.7+).
'''

# Q2. Given a list of lists, can you use set() directly to remove duplicates? Why or why not? How do you solve this?
'''
A2: No, because lists are unhashable and cannot be added to a set. Solution: Convert inner lists to tuples for use as set keys or with dict.fromkeys(). Example:
    nested_lists = [[1,2], [2,3], [1,2]]
    unique = list(map(list, dict.fromkeys(tuple(l) for l in nested_lists)))
'''

# Q3. How do you remove duplicates from a list of dictionaries based on multiple keys?
'''
A3: Use a tuple of selected keys as a composite key for each dict, track seen keys in a set, and collect only unique ones.

Example:
    lst = [{"a":1,"b":2}, {"a":1,"b":3}, {"a":1,"b":2}]
    seen = set()
    result = []
    for d in lst:
        key = (d['a'], d['b'])
        if key not in seen:
            seen.add(key)
            result.append(d)
'''

# Q4. What are the trade-offs between using a comprehension with a seen set and dict.fromkeys()?
'''
A4: dict.fromkeys() is concise and preserves order, but only works for hashable elements.
A set-tracking comprehension gives more flexibility (such as custom key functions for partial duplicate logic) and can process unhashable elements if you customize the key.
'''

# Q5. How to remove duplicates from a string while keeping the original order?
'''
A5: Use dict.fromkeys()
    s = "abracadabra"
    unique = "".join(dict.fromkeys(s))
    print(unique)   # 'abrcd'
'''

# Q6. How would you deduplicate usernames in a login system in a case-insensitive way preserving the original case for display?
'''
A6:
- Track a set of lowercased usernames for deduplication.
- Store/display the original version for user-facing, but only allow one version.
Example:
    usernames = ["Alice", "bob", "alice", "Bob"]
    seen = set()
    result = []
    for name in usernames:
        low = name.lower()
        if low not in seen:
            seen.add(low)
            result.append(name)
    print(result)  # ['Alice', 'bob']
'''

# Q7. Can you remove duplicates from a sequence without extra memory? When is that possible/feasible in Python?
'''
A7: In-place removal with O(1) memory is only feasible if:
   - You can mutate the sequence (lists), and
   - You can tolerate O(n^2) time (by checking all prior elements).
   For large datasets, extra memory (sets, dicts) is more efficient. For small data, you can pop/iterate and check forward/back.
'''

# Q8. Write a function that removes duplicates from a list while keeping only the *last* occurrence.
'''
A8:
def remove_keep_last(lst):
    seen = set()
    result = []
    for item in reversed(lst):
        if item not in seen:
            seen.add(item)
            result.append(item)
    return list(reversed(result))

# Sample
lst = [1,2,3,2,4,1,5,3]
print(remove_keep_last(lst))  # [4,1,5,3,2]
'''
