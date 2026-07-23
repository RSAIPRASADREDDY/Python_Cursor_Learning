# --- Python Datatypes: Concepts, Syntax, Examples, Mini-Project, and Interview Q&A ---

# Definition:
# In Python, a "datatype" (or data type) refers to the kind or category of value a variable can hold.
# Datatypes determine what kind of operations can be performed on a value and how much space it takes in memory.
# Common built-in datatypes: int, float, str, bool, list, tuple, set, dict, NoneType.

# --- Types of Datatypes in Python ---

# 1. Numeric Types: int, float, complex
# 2. Sequence Types: str, list, tuple, range
# 3. Mapping Type: dict
# 4. Set Types: set, frozenset
# 5. Boolean Type: bool
# 6. None Type: NoneType

# --- Syntax: Declaring and Checking Datatypes ---

x = 5           # int
y = 3.14        # float
z = "Hello"     # str
flag = True     # bool
nums = [1, 2, 3]  # list
points = (2, 4)    # tuple
prefs = {"theme": "dark"}  # dict
unique = {1, 2, 3} # set
nothing = None     # NoneType

print(type(x), type(y), type(z), type(flag), type(nums), type(points), type(prefs), type(unique), type(nothing))

# --- Beginner Level: Basic Examples ---

# Numeric types: int, float
a = 10                    # int
b = 2.5                   # float
print(a, type(a))         # 10 <class 'int'>
print(b, type(b))         # 2.5 <class 'float'>

# String type
greeting = "Hello, World!"
print(greeting, type(greeting))

# Boolean type
is_valid = False
print(is_valid, type(is_valid))

# Sequence types: list, tuple
fruits = ["apple", "banana", "cherry"]    # list
print(fruits, type(fruits))
dimensions = (1920, 1080)                 # tuple
print(dimensions, type(dimensions))

# Set type (no duplicates)
colors = {"red", "green", "blue", "red"}
print(colors, type(colors))       # set removes duplicates

# Dictionary type
student = {'name': "Sai", 'age': 19}
print(student, type(student))

# NoneType
empty_var = None
print(empty_var, type(empty_var))


# --- Intermediate Level: Mutability and Operations ---

# Lists are mutable (values can be changed)
numbers = [1, 2, 3]
numbers.append(4)
numbers[0] = 10
print("Modified list:", numbers)


# Tuples are immutable (cannot change after creation)
tup = (1, 2, 3)
#tup[0] = 10  # This would raise a TypeError
print(tup,type(tup))

# Sets: only unique, unordered
myset = {1, 2, 3}
myset.add(2)
myset.add(4)
print("Set after operations:", myset)


# Dictionaries: key-value, keys are unique
student_info = {"name": "Alice", "age": 21}
student_info["email"] = "alice@mail.com"
print("Updated dict:", student_info)


# String operations
sentence = "Python is fun"
words = sentence.split()
print(words)
joined = "-".join(words)
print(joined)


# Type conversions
num_str = "100"
num_int = int(num_str)
f = float("22.3")
s = str(12345)
print(num_int, type(num_int), "|", f, type(f), "|", s, type(s))

# Type checking: isinstance() and type()
print(isinstance(numbers, list))    # True
print(isinstance(sentence, int))    # False


# --- Advanced Level: Nesting, Custom Types, and Dynamic Typing ---

# Nesting: A list of dictionaries, tuple of sets, etc.
users = [
    {"name": "Bob", "id": 1},
    {"name": "Ann", "id": 2}
]
print("List of dicts:", users)


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Matrix (list of lists):", matrix)

# Dynamic Typing: A variable can change type
val = 10              # int
print(val, type(val))
val = "Now I'm a string"
print(val, type(val))
val = [7, 8, 9]       # list
print(val, type(val))

# Frozenset (immutable set)
immutable_set = frozenset([1, 2, 3, 2])
print("Frozenset:", immutable_set, type(immutable_set))


# Range object (sequence)
r = range(5)
print("Range as list:", list(r), type(r))



# --- Mini Project: Personal Data Analyzer (Datatypes Demonstration) ---

"""
Mini Project: Personal Data Analyzer

- Stores user profile with various datatypes
- Shows types and performs simple manipulations
"""

def data_analyzer():
    print("\n--- Personal Data Analyzer ---")
    profile = {
        "name": input("Enter your name: "),                  # str
        "age": int(input("Enter your age: ")),               # int
        "height": float(input("Enter your height (cm): ")),  # float
        "hobbies": input("Enter hobbies (comma-separated): ").split(","),  # list
        "marks": (90, 85, 78),   # tuple of ints
        "active": True,          # bool
        "skills": {"python", "communication", "python"},    # set
        "address": None          # NoneType (not provided)
    }
    print("\nProfile Data:", profile)
    print("Field Types:")
    for k, v in profile.items():
        print(f" - {k}: {type(v)}")

    # Modify some values (showing mutability)
    profile["hobbies"][0] = profile["hobbies"][0].strip().capitalize()
    profile["skills"].add("problem-solving")
    print("\nUpdated Hobbies and Skills:", profile["hobbies"], profile["skills"])

    # Count hobbies (list), Highest marks (tuple), Number of skills (set)
    print(f"Number of hobbies: {len(profile['hobbies'])}")
    print(f"Highest marks: {max(profile['marks'])}")
    print(f"Number of skills: {len(profile['skills'])}")

    # Convert age to string and check types
    age_str = str(profile["age"])
    print(f"Age as string: {age_str} ({type(age_str)})")

    # Try to update address if user wants
    if profile["address"] is None:
        new_addr = input("Enter your address (optional, press Enter to skip): ")
        if new_addr:
            profile["address"] = new_addr
    print("Final profile:", profile)

if __name__ == "__main__":
    # Uncomment next line to run the mini-project
    # data_analyzer()
    pass



'''
    # --- Interview Q&A: Python Datatypes ---

    Q: What is a datatype in Python?
    A: A datatype is the classification of data which tells the Python interpreter what kind of value a variable holds and what operations can be performed on it.

    Q: Name five built-in datatypes in Python.
    A: int, float, str, list, dict

    Q: What is the difference between a list and a tuple?
    A: Lists are mutable and dynamic (can be changed), while tuples are immutable (cannot be changed after creation).

    Q: Can you store different types of values in a single list?
    A: Yes, Python lists are heterogeneous; they can store values of any datatype.

    Q: What is the NoneType in Python?
    A: NoneType is the type of the special value None, which signifies 'no value' or 'null'.

    Q: How do you check the type of a variable in Python?
    A: Use type(variable) or isinstance(variable, datatype).

    Q: What is a dictionary? How is it different from a list?
    A: A dictionary stores key-value pairs and is unordered (as of Python 3.6+ insertion ordered); lists store ordered values accessed by index, while dicts use keys.

    Q: Are sets ordered or unordered? Can they contain duplicate items?
    A: Sets are unordered collections and cannot contain duplicate elements.

    Q: Explain dynamic typing in the context of Python datatypes.
    A: In Python, variables can change their datatype at runtime because Python is dynamically typed.

    Q: What will be the output of bool("") and bool("False")?
    A: bool("") is False (empty string is falsy), bool("False") is True (any non-empty string is truthy).

    Q: What happens if you try to change an element in a tuple?
    A: It raises a TypeError because tuples are immutable.
'''
