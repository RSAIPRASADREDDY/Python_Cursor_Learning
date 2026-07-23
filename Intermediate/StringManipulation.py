"""
Python String Manipulation: Concepts, Methods, Syntax, Examples, Mini-Project, and Interview Q&A

Definition:
-----------
A string in Python is an immutable sequence of characters used to store text data. String manipulation refers to the process of changing, parsing, searching, formatting, or analyzing these text sequences.

Methods and Usage:
------------------
- Accessing characters and substrings (indexing, slicing)
- Concatenation
- Repetition
- Case conversion (upper, lower, title, capitalize, swapcase)
- Stripping whitespace (strip, lstrip, rstrip)
- Searching (find, index, count, startswith, endswith)
- Replace substrings
- Splitting and joining
- Alignment and formatting (center, ljust, rjust, zfill, format, f-strings)
- Validation (isalpha, isdigit, isalnum, isspace, isnumeric, islower, isupper, istitle)
- Encoding/decoding

Syntax:
-------
# String creation
s = 'Hello'
t = "World"
multiline = '''Triple-quoted supports
multiple lines'''

# String indexing and slicing
first = s[0]
last = s[-1]
sub = s[1:4]        # 'ell'

# Concatenation and repetition
result = s + ' ' + t
echo = s * 3

# Method usage
upperc = s.upper()
words = "a,b,c".split(',')
joined = '-'.join(words)
"""

# -----------------------------------------------
# Beginner Level Examples
# -----------------------------------------------

# Creating strings 
name = "Sai"
greet = 'Hello'
multiline = """This is a 
multiline string."""

print(name)
print(greet)
print(multiline)

# Indexing
print(name[0])       # 'S'
print(name[-1])      # 'i'

# Slicing
print(name[1:3])     # 'ai'
print(name[:2])      # 'Sa'
print(name[2:])      # 'i'

# Concatenation
fullname = greet + " " + name
print(fullname)      # 'Hello Sai'

# Repetition
repeat = (greet + "! ") * 2
print(repeat)        # 'Hello! Hello! '

# Iteration
for char in name:
    print(char, end="-")
print()

# String length
print(len(name))     # 3

# -----------------------------------------------
# Intermediate Level Examples
# -----------------------------------------------

# Case conversion
s = "pYtHon stRinG"
print(s.upper())         # 'PYTHON STRING'
print(s.lower())         # 'python string'
print(s.title())         # 'Python String'
print(s.capitalize())    # 'Python string'
print(s.swapcase())      # 'PyThON STrINg'

# Whitespace stripping
messy = "   Hello Sai   "
print(messy.strip())     # 'Hello Sai'
print(messy.lstrip())    # 'Hello Sai   '
print(messy.rstrip())    # '   Hello Sai'

# Searching and counting
text = "banana"
print(text.find('a'))    # 1 (first occurrence)
print(text.rfind('a'))   # 5 (last occurrence)
print(text.count('a'))   # 3
print(text.startswith("ba"))   # True
print(text.endswith("na"))    # True

# Replacement
sentence = "I like apples"
print(sentence.replace("apples", "oranges"))    # 'I like oranges'

# Splitting and joining
csv = "red,green,blue"
colors = csv.split(",")
print(colors)                 # ['red', 'green', 'blue']
joined = "|".join(colors)
print(joined)                 # 'red|green|blue'

# Formatting
age = 25
city = "Bangalore"
print("My age is {} and I live in {}".format(age, city))
print(f"My age is {age} and I live in {city}")

# Alignment and filling
word = "cat"
print(word.center(10, "*"))     # '***cat****'
print(word.ljust(10, "-"))      # 'cat-------'
print(word.rjust(10, "."))      # '.......cat'
print("123".zfill(6))           # '000123'

# Validation
id1 = "Sai21"
print(id1.isalnum())    # True
print(id1.isalpha())    # False
print("123".isdigit())  # True
print("abc".islower())  # True
print("ABC".isupper())  # True
print(" ".isspace())    # True


# -----------------------------------------------
# Advanced Level Examples
# -----------------------------------------------

# Reversing a string
s = "Python"
reversed_s = s[::-1]
print(reversed_s)           # 'nohtyP'

# Palindrome check
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))   # True
print(is_palindrome("python"))  # False

# Remove all punctuation using str.translate
import string
data = "Hello, World! What is Python?"
table = str.maketrans('', '', string.punctuation)
clean = data.translate(table)
print(clean)        # 'Hello World What is Python'

# Extract all digits from a string
mix = "The number is 42 and code is 007."
digits = ''.join([ch for ch in mix if ch.isdigit()])
print(digits)       # '42007'

# Advanced: Encoding and decoding
s = "Café"
utf_bytes = s.encode('utf-8')
print(utf_bytes)         # b'Caf\xc3\xa9'
decoded = utf_bytes.decode('utf-8')
print(decoded)           # 'Café'

# Format with dictionary
info = {"name": "Sai", "score": 92}
print("Name: {name}, Score: {score}".format(**info))


# -----------------------------------------------
# Mini Project: Email Analyzer
# -----------------------------------------------
# Features:
# - Parses a given email string
# - Extracts username and domain
# - Validates format
# - Checks allowed domains
# - Masks user for privacy


def analyze_email(email, allowed_domains=None):
    allowed_domains = allowed_domains or {"gmail.com", "outlook.com", "yahoo.com"}

    # Basic validation
    if "@" not in email or email.count("@") != 1:
        print("Invalid email format.")
        return

    username, domain = email.split("@")

    print(f"Username: {username}")
    print(f"Domain: {domain}")

    # Privacy mask (show only first & last char, rest as '*')
    if len(username) > 2:
        masked = username[0] + '*'*(len(username)-2) + username[-1]
    else:
        masked = username
    print("Masked user for privacy:", masked)

    # Domain validation
    if domain in allowed_domains:
        print(f"Email domain '{domain}' is allowed.")
    else:
        print(f"Email domain '{domain}' is NOT allowed.")

    # Advanced: Check if username is alphanumeric
    if username.isalnum():
        print("Username is alphanumeric.")
    else:
        print("Username contains special characters.")

# Demo
print("-- Email Analyzer Demo --")
test_emails = [
    "sai21@gmail.com",
    "amy_max!@outlook.com",
    "user@invalidsite.net"
]
for em in test_emails:
    print(f"\nTesting: {em}")
    analyze_email(em)

'''
------------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS (PYTHON STRING MANIPULATION)
------------------------------------------------------------

Q1: How are strings stored in Python and why are they immutable?
A1: Strings in Python are sequences of Unicode characters backed by immutable arrays; immutability means once created, their content can't change. This allows string objects to be hashable, used as dict keys, and ensures thread safety. For modifications, Python creates new string objects.

Q2: Describe how you would reverse the words in a sentence. (Not the characters!)
A2:
sentence = "Python is awesome"
words = sentence.split()
rev = " ".join(reversed(words))
print(rev)   # 'awesome is Python'

Q3: How do you efficiently build a large string from components, and why is "'+'.join(list)" preferred over repeated concatenation?
A3: Repeating 's += part' is inefficient as each step creates a new string in memory. Using 'separator.join(list_of_strings)' constructs the result in one go.
parts = ["a", "b", "c"]
print(".".join(parts))   # 'a.b.c'

Q4: How can you count the frequency of each character in a string?
A4:
from collections import Counter
s = "banana"
freq = Counter(s)
print(freq)  # Counter({'a':3, 'b':1, 'n':2})

Q5: Give an example of using regular expressions for string manipulation.
A5:
import re
s = "Contact: +91-999-888-7777, Email: user@mail.com"
phones = re.findall(r'\+\d{2}-\d{3}-\d{3}-\d{4}', s)
print(phones)  # ['+91-999-888-7777']

Q6: Given the string "  Python, Java  , C++ ,Go  ", write code to collect all languages as a clean list.
A6:
langs = "  Python, Java  , C++ ,Go  "
lst = [lang.strip() for lang in langs.split(",")]
print(lst)   # ['Python', 'Java', 'C++', 'Go']

Q7: Is the expression s[::-1] always valid for reversing a Unicode string? Any issues?
A7: For most cases, yes, but it may break apart user-perceived characters if they are composed of multiple code points (like emoji with skin tone modifiers or some accented letters), leading to incorrect visual results.

Q8: How would you detect if a string is a numeric integer (not float) using string methods?
A8:
s = "12345"
print(s.isdigit())      # True
print("12.5".isdigit()) # False

Q9: How can you remove all vowels from a string (case-insensitive)?
A9:
import re
s = "Hello World"
no_vowels = re.sub(r'(?i)[aeiou]', '', s)
print(no_vowels)   # 'Hll Wrld'

Q10: Given a CSV string line, how would you safely parse its fields if they may contain commas within quoted strings?
A10:
import csv
from io import StringIO
line = '"Sai, Kumar",21,"Bangalore, IN"'
reader = csv.reader(StringIO(line))
fields = next(reader)
print(fields)  # ['Sai, Kumar', '21', 'Bangalore, IN']

------------------------------------------------------------
'''
